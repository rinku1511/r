from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Person,Reg,contact,Donor,Vol,Supportus
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'index.html')
##########################
def register(request):
	if request.method =="POST":
		name = request.POST['name']
		email = request.POST['email']
		number = request.POST['phone']
		
		a1 = Reg(name=name,email=email,phone_no=number)
		a1.save()

		value = True
		messages.success(request, 'Registration successful')
		return render(request,'index.html',{'value':value})
	else:
		value = False
		return render(request,'index.html',{'value':value})	
#		return redirect('index')
#	else:
#		return render(request, 'index.html')

def signup(request):
	if request.method == "POST":
		f_name = request.POST['f_name']
		l_name = request.POST['l_name']
		gender = request.POST['gender']
		email = request.POST['email']
		password = request.POST['password']
		phone_no = request.POST['phone']
		blood_group = request.POST['blood_group']
		age = request.POST['age']
		s1 = Person(f_name=f_name,l_name=l_name,gender=gender,email=email,password=password,phone_no=phone_no,blood_group=blood_group,age=age)
		s1.save()

		value = True
		messages.success(request, 'Signup successful')
		return render(request,'signup.html',{'value':value})
	else:
		value = False
		return render(request,'signup.html',{'value':value})	

#		return redirect('signup')
#	else:
#		return render(request, 'signup.html')

def contactus(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		contactnum = request.POST['contactnum']
		messege = request.POST['msg']
		c1 = contact(name=name,email=email,contactnum=contactnum,messege=messege)
		c1.save()
		value = True
		messages.success(request, 'Message sent successfully')
		return render(request,'contactus.html',{'value':value})
	else:
		value = False
		return render(request,'contactus.html',{'value':value})	

def donateblood(request):
	return render(request,'donate-blood.html')

def donorcenter(request):
	return render(request,'donor-center-locations.html')
    
def aboutus(request):
	return render(request,'about-us.html')

def supportus(request):
	return render(request,'support-us.html')

def appointment(request):
	if request.method == "POST":
		name = request.POST['name']
		phone_no = request.POST['phone']
		date = request.POST['date']
		time = request.POST['time']
		d1 = Donor(name=name,phone_no=phone_no,date=date,time=time)
		d1.save()
		value = True
		messages.success(request, 'Appointment booked!')
		return render(request,'appointment.html',{'value':value})
	else:
		value = False
		return render(request,'appointment.html',{'value':value})

def login(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		try:
			v=Person.objects.get(email=email)
			if v.password == password:
				request.session['user']=email
				return redirect('index')
			else:
				return redirect('login')
		except:
			return redirect('login')
	else:
		return render(request,'login.html')		

def logout(request):
	if 'user' in request.session:
		del request.session['user']
		return redirect('login')
	return redirect('login')

def vol(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		messege = request.POST['messege']
		print(name,email,phone,messege)
		b1 = Vol(name=name,email=email,phone=str(phone),messege=messege)
		b1.save()
		value = True
		messages.success(request, 'Form submission successful')
		return render(request,'support-us.html',{'value':value})
	else:
		value = False
		return render(request,'support-us.html',{'value':value})	


		
#		return redirect('supportus')
#	else:
#		return render(request,'support-us.html')

def supportus(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		location = request.POST['location']
		drive_date = request.POST['drive_date']
		messege = request.POST['messege']
		e1 = Supportus(name=name,email=email,phone=phone,location=location,drive_date=drive_date,messege=messege)
		e1.save()
		value = True
		messages.success(request, 'Form submission successful')
		return render(request,'support-us.html',{'value':value})
	else:
		value = False
		return render(request,'support-us.html',{'value':value})	



