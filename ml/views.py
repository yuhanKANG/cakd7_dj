from django.shortcuts import render
import joblib
import pandas as pd


def inputdata(request):
    return render(request, 'ml/inputdata.html')

def ml_result(request):
    cls = joblib.load('ml/tcl_model_homework.pkl')

    df = pd.DataFrame(columns=['age_cat', 'sex_female', 'sex_male',
       'embarked_C', 'embarked_Q', 'embarked_S'])

    lis = []

    lis.append(request.GET['age_cat'])
    lis.append(request.GET['sex_female'])
    lis.append(request.GET['sex_male'])
    lis.append(request.GET['embarked_C'])
    lis.append(request.GET['embarked_Q'])
    lis.append(request.GET['embarked_S'])

    df.loc[0,:] = lis
    ans = cls.predict(df)
    if ans == 0 :
        ans = "꽥."
    else :
        ans = "Survived"
    return render(request, "ml/ml_result.html",{'lis':lis,'ans':ans})

