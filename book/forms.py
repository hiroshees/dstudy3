from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator

from .models import Book

class BookUpdateForm(ModelForm):
    """
    書籍更新用フォーム
    """
    class Meta:
        model = Book
        fields = ('title','price', 'author','category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    title = forms.CharField(
        label="本の名前",
        error_messages={
            "required" : "本名を入力してください"
        },
        validators=[
            MinLengthValidator(4, "4文字以上にしてね"),
        ],
        help_text="4文字以上で入力してください",
    )
    
    price = forms.IntegerField(
        label="本の金額",
        #min_value=1,
        #max_value=2000,
        validators=[
            MinValueValidator(100,"100以上にしてね"),
            MaxValueValidator(2000,"2000以下にしてね")
        ],
    )
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if title == "aaa" :
            raise ValidationError("「aaa」はだめだよ")
        return title

    def clean(self):
        cleaned_data = super().clean()
        
        price = cleaned_data.get('price')
        if price != None and price % 2 == 1 :
            self.add_error('price','奇数の金額はダメだよ')

