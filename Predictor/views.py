from django.shortcuts import render, redirect, get_object_or_404
from .forms import PredictionForm
from .models import Prediction
from .pricing_data import calculate_price


def home(request):
    return render(request, 'predictor/home.html')


def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            price = calculate_price(
                data['location'],
                data['area'],
                data['bhk'],
                data['bathrooms'],
                data['property_age'],
                data['furnishing'],
            )

            prediction = Prediction.objects.create(
                location=data['location'],
                area=data['area'],
                bhk=data['bhk'],
                bathrooms=data['bathrooms'],
                property_age=data['property_age'],
                furnishing=data['furnishing'],
                estimated_price=price,
            )

            return redirect('result', prediction_id=prediction.id)
    else:
        form = PredictionForm()

    return render(request, 'Predictor/predict.html', {'form': form})


def result(request, prediction_id):
    prediction = get_object_or_404(Prediction, id=prediction_id)
    return render(request, 'Predictor/result.html', {'prediction': prediction})

def history(request):
    predictions = Prediction.objects.all().order_by('-created_at')
    return render(request, 'Predictor/history.html', {'predictions': predictions})