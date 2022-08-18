from django.shortcuts import render

def inputdata(request):
    return render(request, 'program/inputdata.html')

# 아무런 처리를 안해도 result.html 문서로 리턴함
def result(request):
    lis=[]
    lis.append(request.GET['a'])
    lis.append(request.GET['b'])
    
    sum = 0
    for l in lis :
        sum += int(l)
    ans = sum

    return render(request, 'program/result.html', {'ans':ans, 'lis':lis})
    # return render(request, 'program/result.html'