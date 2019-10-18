# Create your views here.
from .models import MyTable
import json
from django.shortcuts import render_to_response


def home(request):
    content = {'blog': MyTable.objects.filter().values()}
    content = json.dumps(str(content))
    return render_to_response('home.html', locals())
