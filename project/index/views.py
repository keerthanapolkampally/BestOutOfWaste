from django.shortcuts import render
from .forms import InputForm
from django.views.decorators.csrf import csrf_exempt
import os
import json
from django.conf import settings
# Create your views here.
def index(request):
	return render(request,'index.html')


@csrf_exempt
def app(request):
	if request.method == 'POST':
		form = InputForm(request.POST)

		if form.is_valid():
			z = json.loads(open(os.path.join(settings.PROJECT_ROOT, 'c.json')).read())
			h=list()
			for i in range(51):
				h.append(0)
			y=[]
			y.append(form.cleaned_data['Ingredient1'])
			y.append(form.cleaned_data['Ingredient2'])
			y.append(form.cleaned_data['Ingredient3'])
			y.append(form.cleaned_data['Ingredient4'])
			y.append(form.cleaned_data['Ingredient5'])
			
			#print 'ARRAY: ',y
			for i in y:
				for j in z:
					for k in j[u'ingredients']:
					#if i in j[u'ingredients']:
						if i in k:
							h[j[u'id']] = h[j[u'id']]+1;
			#print h
			m = max(h)
			n = 999999
			for i in range(len(h)):
				#print h[i]
				if h[i]==m:
					#print len(z[i][u'ingredients'])
					r = len(z[i][u'ingredients']) - h[i]

					if r<n:
						n=r
						pos = i
			ing = list()
			for i in z[pos][u'ingredients']:
				ing.append(i)
			for i in y:
				if i in ing:
					ing.remove(i)
			ingredients=list()
			name = z[pos][u'recipe']
			ingredients = z[pos][u'ingredients']
			cuisine = z[pos][u'cuisine']
			return render(request,'recipe.html',{'name' : name, 'ingredients' : ingredients, 'cuisine' : cuisine,'ing' : ing})

	else:
		form = InputForm()

	return render(request, 'index.html',{'form':form})	
			