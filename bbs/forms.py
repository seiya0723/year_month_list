from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

from .models import Topic

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ["comment"]

#モデルを継承しないフォームクラス
class YearMonthForm(forms.Form):
    year    = forms.IntegerField()
    month   = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])



