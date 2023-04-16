from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now() # get the current datetime
    return render(request, 'index.html', {'now': now})