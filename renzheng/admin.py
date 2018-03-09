from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(School)
class SchollAdmin(admin.ModelAdmin):
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Rzuser)
class Rzuser(admin.ModelAdmin):
    list_display = ["username","name","school","sctime","couser","pubtime","iscode"]
    list_editable = ["iscode"]
    ordering = ["-pubtime",]
    date_hierarchy = 'pubtime'
    list_filter = ["pubtime","iscode"]
    actions = ["make_code","make_nocode"]
    search_fields = ["school__name"]
    def make_code(self, request, queryset):
        rows_updated=queryset.update(iscode=1)
        message_bit = "%s 条认证信息被审核通过" % rows_updated
        self.message_user(request,message_bit)

    make_code.short_description = "批量审核通过"
    def make_nocode(self,request,queryset):
        rows_updated=queryset.update(iscode=2)
        message_bit = "%s 条认证信息审核被拒绝" % rows_updated
        self.message_user(request, message_bit)

    make_nocode.short_description = "批量审核拒绝"