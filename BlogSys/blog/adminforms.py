from django import forms


# sv新增的文件413
# 用于后台管理的form的自定义

class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, label='摘要',
                                  required=False)

