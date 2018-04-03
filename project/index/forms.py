from django import forms

class InputForm(forms.Form):
	Ingredient1 = forms.CharField(label='Ingredient', max_length=100)
	Ingredient2	= forms.CharField(label='Ingredient', max_length=100)
	Ingredient3	= forms.CharField(label='Ingredient', max_length=100)
	Ingredient4	= forms.CharField(label='Ingredient', max_length=100)
	Ingredient5	= forms.CharField(label='Ingredient', max_length=100)

