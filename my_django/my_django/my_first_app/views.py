# Create your views here.
from  .models import MY_TABLE
import json
from django.shortcuts import render_to_response,render
def home(request):
    content = {'blog':MY_TABLE.objects.filter().values()}
    content=json.dumps(str(content))
    return render_to_response('home.html',locals())
