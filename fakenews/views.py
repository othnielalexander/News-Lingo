from django.shortcuts import render

import os
from .forms import NewsForm
import pandas as pd
import numpy as np
import pickle

# Create your views here.

operate = 0


def fakenews(request):
    operate = 0
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.cleaned_data['news']
            operate = 1
            BASE_DIR = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))
            # trainModel = joblib.load( os.path.join(BASE_DIR,'fakenews/final_model.sav'))

            load_model = pickle.load(
                open(os.path.join(BASE_DIR, 'fakenews/final_model.sav'), 'rb'))
            prediction = load_model.predict([news])
            prob = load_model.predict_proba([news])

            pred = str(prediction[0])
            print(pred)
            prob = str(prob[0][1])
            print(prob)
            result = "The given statement is " + pred + \
                " The truth probability score is " + prob

            print(result)

            return render(request, 'form.html', {'result': result, 'operate': operate, 'form': form})

    form = NewsForm()
    return render(request, 'form.html', {'form': form, 'operate': operate})
