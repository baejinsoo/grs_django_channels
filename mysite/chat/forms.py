from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_id','user_name', 'user_email', 'user_rank', 'birth', 'user_pic')
        TAG_CHOICES = (
            ("", "Select Tag"),
            ("0", "사원"),
            ("1", "대리"),
            ("2", "팀장"),
            ("3", "과장"),
            ("4", "부장"),
            ("5", "사장"),
        )
        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.TextInput(attrs={'class': 'form-control'}),
            # 'user_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'user_rank': forms.Select(choices=TAG_CHOICES, attrs={'class': 'form-control'}),
            'birth': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'user_id': '사번',
            'user_name': '이름',
            'user_email': '이메일',
            'thumbnail': '이미지',
            'user_rank': '직책',
            'birth': '생일',
            'user_pic': '사진등록'
        }