from django import forms


# 留言板表单
class MessageForm(forms.Form):
    title = forms.CharField(max_length=25, min_length=1, label='Title',
                            error_messages={'min_length': '标题最小长度为1', 'max_length': '标题最大长度为25'})
    content = forms.CharField(widget=forms.Textarea, label='Content')
    email = forms.EmailField(label='Email')
