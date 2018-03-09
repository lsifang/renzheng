from django.db import models

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class User(models.Model):
    username=models.CharField(max_length=20,verbose_name="用户名")
    password=models.CharField(max_length=50,verbose_name="密码")

    def __str__(self):
        return self.username

class Rzuser(models.Model):
    gender=(
        ("men","男"),
        ("women","女")
    )
    code=(
        (0,"审核中"),
        (1,"审核通过"),
        (2,"审核未通过")
    )
    username=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="账户")
    school=models.ForeignKey(School,on_delete=models.PROTECT,verbose_name="学校")
    couser=models.CharField(max_length=30,unique=True,verbose_name="学信网账号")
    name=models.CharField(max_length=20,verbose_name="姓名")
    sex=models.CharField(max_length=10,choices=gender,default="men",verbose_name="性别")
    sctime=models.DateField(verbose_name="入学时间",null=True,blank=True)
    pubtime=models.DateField(auto_now_add=True,verbose_name="提交时间")
    iscode=models.IntegerField(choices=code,default=0,verbose_name="审核状态")
    def __str__(self):
        return self.name
    class Meta:
        ordering=["-pubtime"]
        verbose_name="认证信息"
        verbose_name_plural="认证信息"