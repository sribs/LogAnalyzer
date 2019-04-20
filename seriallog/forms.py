from django import forms

class UpdateErrorKeywordsForm():
    issue = forms.Textarea()
    cause = forms.TextInput()
