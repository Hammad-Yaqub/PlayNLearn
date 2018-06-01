from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from PlayNLearn.forms import signUpForm


def signUp(request):
    if(request.method=='POST'):
        form=signUpForm(request.POST or None)
        if(form.is_valid()):
            form.save()
    else:
        form=signUpForm()
    return render(request,'PlayNLearn/signUp.html',{'form':form})

def home(request):
    if(request.method=='POST'):
        form = signUpForm(request.POST or None)
        if (form.is_valid()):
            signUp_item = form.save(commit=False)
            signUp_item.save()
        #name=request.POST['U_Name']
        #context = {
        #    'uname': name
        #}
        return render(request, 'PlayNLearn/home.html')

def login(request):
    if(request.method=='POST'):
        form = AuthenticationForm(data=request.POST)
        if (form.is_valid()):
            return render(request, 'PlayNLearn/home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'PlayNLearn/login.html', {'form':form})