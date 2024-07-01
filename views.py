from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def doctor_details(request):
    first_name = request.GET.get("first_name", "default")
    first_name = first_name
    last_name = request.GET.get("last_name", "default")
    last_name = last_name
    address_line1 = request.GET.get("address_line1", "default")
    address_line1 = address_line1
    city = request.GET.get("city", "default")
    city = city
    state = request.GET.get("state", "default")
    state = state
    username = request.GET.get("state", "default")
    username = username
    pincode = request.GET.get("pincode", "default")
    pincode = pincode
    Mobilenumber = request.GET.get("Mobilenumber", "default")
    Mobilenumber = Mobilenumber
    Email = request.GET.get("Email", "default")
    Email = Email
    Password = request.GET.get("Password", "default")
    Password = Password
    ConfirmPassword = request.GET.get("ConfirmPassword", "default")
    ConfirmPassword = ConfirmPassword
    Image = request.GET.get("Image", "default")
    Image = Image
    if Password != ConfirmPassword:
        return HttpResponse("Passwords and confirm password are not matched.")
    params = {'first_name':first_name,'last_name' : last_name,'address_line1' : address_line1,'city': city,'state' : state, 'pincode' : pincode, 'username' : username,'Mobilenumber':Mobilenumber,'Email':Email,'Password':Password,'ConfirmPassword' : ConfirmPassword,'Image':Image}
    return render(request,'doctor_details.html',params)
def doctor_signup(request):
    return render(request, 'doctor_signup.html')
def patients_details(request):
    first_name = request.GET.get("first_name", "default")
    first_name = first_name
    last_name = request.GET.get("last_name", "default")
    last_name = last_name
    address_line1 = request.GET.get("address_line1", "default")
    address_line1 = address_line1
    city = request.GET.get("city", "default")
    city = city
    state = request.GET.get("state", "default")
    state = state
    username = request.GET.get("state", "default")
    username = username
    pincode = request.GET.get("pincode", "default")
    pincode = pincode
    Mobilenumber = request.GET.get("Mobilenumber", "default")
    Mobilenumber = Mobilenumber
    Email = request.GET.get("Email", "default")
    Email = Email
    Password = request.GET.get("Password", "default")
    Password = Password
    ConfirmPassword = request.GET.get("ConfirmPassword", "default")
    ConfirmPassword = ConfirmPassword
    Image = request.GET.get("Image", "default")
    Image = Image
    params = {'first_name': first_name, 'last_name': last_name, 'address_line1': address_line1, 'city': city,
              'state': state, 'pincode': pincode, 'username': username, 'Mobilenumber': Mobilenumber, 'Email': Email,
              'Password': Password, 'ConfirmPassword': ConfirmPassword, 'Image': Image}
    return render(request, 'patients_details.html', params)
def patient_signup(request):
    return render(request, 'patient_signup.html')