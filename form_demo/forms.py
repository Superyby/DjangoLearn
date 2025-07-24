from django import forms
from django.core.validators import RegexValidator
from form_demo.models import *


# 留言板表单
class MessageForm(forms.Form):
    title = forms.CharField(max_length=25, min_length=1, label='Title',
                            error_messages={'min_length': '标题最小长度为1', 'max_length': '标题最大长度为25'})
    content = forms.CharField(widget=forms.Textarea, label='Content')
    email = forms.EmailField(label='Email')


class RegisterForm(forms.Form):
    telephone = forms.CharField(validators=[RegexValidator(r'^1[3-9]\d{9}', '手机号码格式错误')], label='Telephone')
    pwd1 = forms.CharField(min_length=6, max_length=100)
    pwd2 = forms.CharField(min_length=6, max_length=100)

    # clean_[Field]
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # if User.objects.filter(telephone=telephone).exists():
        #     raise forms.ValidationError('手机号码已存在')
        if telephone == '13333333333':
            raise forms.ValidationError('手机号码已存在')
        else:
            return telephone

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("pwd1")
        pw2 = cleaned_data.get("pwd2")
        if pw1 != pw2:
            raise forms.ValidationError("密码不一致")
        else:
            return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ['title', 'content']
        fields = "__all__"
        # 相反，排除
        # exclude = ['create_time']
        error_messages = {
            'category': {
                'required': 'category 不可以为空'
            }
        }
