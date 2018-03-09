from django import forms
from .models import School
class LoginForm(forms.Form):
    username=forms.CharField(label="用户名",max_length=20,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入用户名"}))
    password=forms.CharField(label="密码",max_length=50,min_length=6,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请输入密码"}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入用户名"}))
    password = forms.CharField(label="密码", max_length=50, min_length=6,widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码"}))

class RzuserForm(forms.Form):
    gender=((x.id,x.name) for x in School.objects.all().select_related())
    name=forms.CharField(label="姓名",max_length=5,min_length=2,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入姓名"}))
    school=forms.ChoiceField(label="学校",choices=gender,widget=forms.Select(attrs={"class": "form-control"}))
    couser=forms.CharField(label="学信网账号",max_length=50,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入学信网账号"}))
    sex=forms.ChoiceField(label="性别",choices=(("men","男"),("women","女")),initial="women",widget=forms.RadioSelect())
    YEAR_LIST=[str(i) for i in range(2014,2018)]
    sctime=forms.DateField(label="入学时间",widget=forms.SelectDateWidget(years=YEAR_LIST))