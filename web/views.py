from django.shortcuts import render
from utils.auth import check_login
# Create your views here.

@check_login
def index(request):
    print(request.session.get('user_info'))
    return render(request,"index.html")