from django import forms

CHOICES = list()


class ScraperForm(forms.Form):

    query = forms.CharField(label = 'Enter the Search Keyword: ', max_length = 50)

    