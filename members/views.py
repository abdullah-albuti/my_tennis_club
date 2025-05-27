from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

@login_required
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
@login_required
def testing(request):
  mydata = Member.objects.filter(Q(firstname='s') | Q(firstname__startswith='N')).values()
  mymembers = Member.objects.all().order_by('-lastname').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
    'fruits': ['Apple', 'Banana', 'Cherry'],  
    'cars': ['toyota  ', 'honda', 'gmc'],   
    'firstname':'Mr.abdullah',
     'mydata': mydata,
  }
  return HttpResponse(template.render(context, request))

@login_required
def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully!")
  return redirect("main.html")
  