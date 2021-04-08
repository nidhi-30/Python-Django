from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

def predict(request):
	return render(request, 'predict.html')

def predict_chances(request):
	if request.POST.get('action') == 'post':
		mean_radius = float(request.POST.get('mean_radius'))
		mean_texture = float(request.POST.get('mean_texture'))
		mean_perimeter = float(request.POST.get('mean_perimeter'))
		mean_area = float(request.POST.get('mean_area'))
		mean_smoothness = float(request.POST.get('mean_smoothness'))

		# Unpickle the model
		model = pd.read_pickle(r"D:\\Python\\cancer_detection\\new_model.pickle")
		result = model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])

		classification = result[0]

		PredResults.objects.create(mean_radius = mean_radius, mean_texture = mean_texture, mean_perimeter = mean_perimeter,
		 mean_area = mean_area, mean_smoothness = mean_smoothness, classification = classification)

		return JsonResponse({ 'result' : classification, 'mean_radius' : mean_radius, 'mean_texture' : mean_texture, 
			'mean_perimeter' : mean_perimeter, 'mean_area' : mean_area, 'mean_smoothness' : mean_smoothness}, safe = False)

def view_results(request):
	data = { "dataset" : PredResults.objects.all() }
	return render(request, "results.html", data)