from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ChatBotPromptForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    
    def __init__(self, *args, **kwargs):
        super(ChatBotPromptForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Generate Text'))