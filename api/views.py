from django.http import HttpResponse
from django.shortcuts import render
from api.models import ObjectType, ResourceType, Country,Object, Website,Result
import datetime
from django.contrib.auth.models import User
import json

def index(request):
    all_objects=Website.objects.all().count();
    verified=Website.objects.filter(verified=True).count();
    results=Result.objects.all().count()
    g_res=Result.objects.filter(positive=True).count()
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    c_all_objects=Website.objects.filter(created_at__range=[start_week, end_week]).count();
    c_verified=Website.objects.filter(verified=True,created_at__range=[start_week, end_week]).count();
    c_results=Result.objects.filter(created_at__range=[start_week, end_week]).count()
    c_g_res=Result.objects.filter(positive=True,created_at__range=[start_week, end_week]).count()
    users=User.objects.all()
    user_results=[]
    for user in users:
    	user_results.append(User.objects.filter(result__positive=True,pk=user.id).count())
    users=zip(users,user_results)


    today = datetime.datetime.now()
    web_month=[]
    web_month.append(Website.objects.filter(created_at__month=today.month-1).count())
    web_month.append(Website.objects.filter(created_at__month=today.month).count())
    web_month.append(Website.objects.filter(created_at__month=today.month+1).count())
    web_month.append(Website.objects.filter(created_at__month=today.month+2).count())
    web_month.append(Website.objects.filter(created_at__month=today.month+3).count())
    web_month.append(Website.objects.filter(created_at__month=today.month+4).count())
    web_month.append(Website.objects.filter(created_at__month=today.month+5).count())

    res_month=[]
    res_month.append(Result.objects.filter(positive=True,created_at__month=today.month-1).count())
    res_month.append(Result.objects.filter(positive=True,created_at__month=today.month).count())
    res_month.append(Result.objects.filter(positive=True,created_at__month=today.month+1).count())
    res_month.append(Result.objects.filter(positive=True,created_at__month=today.month+2).count())
    res_month.append(Result.objects.filter(positive=True,created_at__month=today.month+3).count())
    res_month.append(Result.objects.filter(positive=True,created_at__month=today.month+4).count())
    res_month.append(Result.objects.filter(positive=True,created_at__month=today.month+5).count())
    data_month=zip(web_month,res_month)
    web_month=json.dumps(web_month)
    res_month=json.dumps(res_month)
    return render(request, 'api/index.html',{
        'ob_count':all_objects,
        'verified':verified,
        'results':results,
        'g_res':g_res,
        'user':request.user,
        'c_ob_count':c_all_objects,
        'c_verified':c_verified,
        'c_results':c_results,
        'c_g_res':c_g_res,
        'users':users,
        'data_month':data_month,
        'web_month':web_month,
        'res_month':res_month

    })
