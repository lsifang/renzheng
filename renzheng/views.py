from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def register(request):
    message = "请牢记你的用户名和密码"
    if request.session.get("is_login",None):
        return redirect("/login/")
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            same_name_user = User.objects.filter(username=username)
            if same_name_user:
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'register.html', locals())
            new_user=User.objects.create()
            new_user.username=username
            new_user.password=password
            new_user.save()
            return redirect('/login/')
    form=RegisterForm()
    return render(request,'register.html',locals())

def login(request):
    if request.session.get('is_login', None):
        return redirect("/code/")
    if request.method=="POST":
        form=LoginForm(request.POST)
        username = form['username']
        password = form['password']
        if username and password:
            try:
                m = User.objects.get(username=request.POST["username"])
                if m.password==request.POST['password']:
                    request.session["is_login"]=True
                    request.session["username"] = m.username
                    request.session["member_id"]=m.id
                    return redirect("/code/")
                else:
                    message="密码不正确"
                    return render(request,'login.html',locals())
            except:
                message = "用户名不存在！"
                return render(request,'login.html',locals())
        else:
            message="请填写完整信息"
            return render(request,'login.html',locals())
    form=LoginForm()
    return render(request,'login.html',locals())

def code(request):
    if not request.session.get("is_login",None):
        return redirect("/login")
    if  User.objects.get(pk=request.session["member_id"]).rzuser_set.all():
        return redirect("/coded/")
    if request.method=="POST":
        form=RzuserForm(request.POST)
        if form.is_valid():
            couser = form.cleaned_data['couser']
            name = form.cleaned_data['name']
            sex = form.cleaned_data['sex']
            sctime = form.cleaned_data['sctime']
            school_id= form.cleaned_data['school']
            username_id = request.session["member_id"]
            iscode = "0"
            same_couser=Rzuser.objects.filter(couser=couser)
            if same_couser:
                message="该学信网账号已被提交,请联系管理员qq524582427"
                return render(request,'code.html',locals())
            try:
                new_rzuser=Rzuser.objects.create(couser=couser,name=name,sex=sex,sctime=sctime,school_id=school_id,username_id=username_id)
                return redirect('/coded/')
            except:
                message="提交失败，请重新填写"
                return render(request,'code.html',locals())
    form=RzuserForm()
    message="请认真填写以下内容"
    return render(request,'code.html',locals())

def coded(request):
    if not request.session.get("is_login",None):
        return redirect("/login")
    if not User.objects.get(pk=request.session["member_id"]).rzuser_set.all():
        return redirect('/code/')
    rzxinxi=User.objects.get(pk=request.session["member_id"]).rzuser_set.get(username_id=request.session["member_id"])
    is_code=rzxinxi.iscode
    if is_code==0:
        message="您的信息已提交，正在审核......"
    elif is_code==1:
        message="您的信息已认证成功"
    elif is_code==2:
        message="审核未通过，点击下方按钮重新认证"
        if request.method == "POST":
            rzxinxi.delete()
            return redirect('/code/')
        return render(request, 'coded.html', locals())
    return render(request,'coded.html',{"message":message,"rzxinxi":rzxinxi})

def logout(request):
    if not request.session.get("is_login",None):
        return redirect("/login/")
    request.session.flush()
    return redirect('/login/')
