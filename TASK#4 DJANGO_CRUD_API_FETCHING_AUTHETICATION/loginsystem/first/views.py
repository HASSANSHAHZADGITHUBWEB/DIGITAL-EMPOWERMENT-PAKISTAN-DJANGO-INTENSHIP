from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from first.models import user
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            checkdb = user.objects.get(email=email)
        except user.DoesNotExist:
            return HttpResponse("WRONG EMAIL AND PASSWORD")
        
        # Check if the email and password match
        if checkdb.password == password:
            username = checkdb.name  # Save the username to a variable
            # Pass the username to the dashboard
            return redirect('dashboard', username=username)
        else:
            return HttpResponse("WRONG EMAIL AND PASSWORD")
    return render(request, "index2.html")

def dashboard(request, username):
    col=user.objects.filter(name=username).values('name', 'email', 'phno', 'dob')
    col2=list(col)
    if request.method=="POST":
        pre=request.POST.get("prepassword")
        new=request.POST.get("newpassword")
        checkdb = user.objects.get(email=col2[0]['email'])
        if checkdb.password!=pre:
            return HttpResponse("PREVIOUS PASSWORD IS WRONG")
        else:
            user.objects.filter(email=col2[0]['email']).update(password=new)
            return HttpResponse("PASSSWORD UPDATED")

    context = {'username': username,"col2":col2}
    return render(request, 'dashboard.html', context)



def reg(request):
  if request.method=="POST":
    ac=user()
    name=request.POST.get("username")
    password=request.POST.get("password")
    email=request.POST.get("email").lower()
    phno=request.POST.get('phone')
    dob=request.POST.get('dob')
    print(name,dob)
    ac.name=name
    ac.email=email
    ac.password=password
    ac.phno=phno
    ac.dob=dob
    ac.save()
    return redirect('login')  
  return render(request,"registeration.html")
