from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from .models import Uploads
from datetime import datetime

def format_uploads(ups):
	real_names = []
	for up in ups:
		real_name = up.upload_file.name.split('/')[-1]
		real_names.append(real_name)
	return real_names

@login_required(login_url='/login/')
def index(request):
	user = request.user.id
	uploads = Uploads.objects.filter(user=User.objects.filter(id=user))
	real_names = format_uploads(uploads)
	zip_uploads = zip(uploads, real_names)

	return render(request, 'cloud/index.html', {'uploads': zip_uploads})

@login_required(login_url='/login/')
def upload(request):
	user = request.user.id
	if request.method=='POST' and request.FILES['upload_file']:
		_file = request.FILES['upload_file']

		upload = Uploads()
		upload.user = User.objects.filter(id=user)[0]
		upload.upload_file = _file

		upload.save()

	return HttpResponseRedirect('/cloud/')

def signup(request):
	if request.method=="POST":
		uname = request.POST['username']
		passw = request.POST['password']
		fname = request.POST['first_name']
		lname = request.POST['last_name']

		u = User()
		u.username = uname
		u.set_password(passw)
		u.first_name = fname
		u.last_name = lname
		
		u.save()

		return HttpResponseRedirect('/login/')
	else:
		users = User.objects.all().values('username')

		signupform = SignUpForm()

	return render(request, 'cloud/signup.html', {'signupform': signupform, 'usernames': users})
