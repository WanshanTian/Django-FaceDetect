from django import forms
class faceform(forms.Form):
    img = forms.ImageField(label='请上传一张待检测的图片')
