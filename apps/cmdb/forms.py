from django import forms

from .models import Code


class CodeCreateForm(forms.ModelForm):

    class Meta:
        model = Code
        fields = '__all__'

        error_messages = {
            'key': {'required': 'key不能为空'},
            'value': {'required': 'value不能为空'}
        }

    def clean(self):
        cleaned_data = super(CodeCreateForm, self).clean()
        key = cleaned_data.get('key')
        value = cleaned_data.get('value')

        if Code.objects.filter(key=key).count():
            raise forms.ValidationError('key：{}已存在'.format(key))

        if Code.objects.filter(value=value).count():
            raise forms.ValidationError('value: {}已存在'.format(value))
