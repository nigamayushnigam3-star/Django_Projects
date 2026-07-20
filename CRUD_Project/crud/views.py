from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import StudentRegistration
from .models import User 

# Create your views here.
def base(request):
    return render(request , 'crud/base.html')

#This Function will Add new Item and Show All items 
def add(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['name']
           em = fm.cleaned_data['email'] 
           pw = fm.cleaned_data['password'] 
           reg = User(name=nm , email=em , password=pw) 
           reg.save()
        #    ek issue aa rha h jb summit h ja rha form tbbhi name email show ho rha h uske liye hm ye krnege 
        fm = StudentRegistration()

    else:
     fm = StudentRegistration()
    stud = User.objects.all() 
    return render(request , 'crud/addandshow.html' ,{'form':fm , 'stu':stud})



# This Function will delete the record 
# pk = primary Key 
def delete_data(request,id):
   if request.method == 'POST':
      pi = User.objects.get(pk=id) 
      pi.delete()
      return HttpResponseRedirect(reverse('add'))
   

# This Function will Update/Edit
def update(request, id):
    pi = User.objects.get(pk=id)
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('add'))
    else:
        fm = StudentRegistration()
    return render(request, 'crud/update.html', {'form': fm, 'stu': pi})
    