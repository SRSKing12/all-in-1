
from django.shortcuts import render, redirect
# from django.views.generic.detail import T
from .models import Group, Message,Userinfo
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import CreateTodo
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django_email_verification import send_email
from .models import Userinfo
from .forms import createUserForm, UserinfoForm

# Create your views here.
def home(request):
    return render(request,'page.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Group.objects.get(name=room)
    return render(request, 'group.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Group.objects.filter(name=room).exists():
        messages.success(request, '...grp found!!')
        return redirect('/'+room+'/?username='+username)
    else:
        messages.success(request, '...No such grp found!!')
        return render(request, 'page.html')
        #new_room = Room.objects.create(name=room)
        #new_room.save()
        #return redirect('/'+room+'/?username='+username)

def mynewroom(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Group.objects.filter(name=room).exists():
        messages.success(request, '...Already grp existing by this name...plz select another name for grp!!')
        return render(request, 'page.html')
    else:
        new_room=Group.objects.create(name=room)
        new_room.save()
        messages.success(request, '...Creating new group!!')
        return redirect('/'+room+'/?username='+username)
 

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message has been sent successfully')

def getMessages(request, room):
    room_details = Group.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


# Create your views here.
def index(request):
    todo = CreateTodo.objects.all()
    if request.method == 'POST':
        new_todo = CreateTodo(
            title = request.POST['title'], 
            descr = request.POST['descr'],
        )
        new_todo.save()
        return redirect('/kk')

    return render(request, 'index.html', {'todos': todo})

def deleteTodo(request, pk):
    todo = CreateTodo.objects.get(id=pk)
    todo.delete()
    return redirect('/kk')

# Sign In & Sign out
def sout(request):
    logout(request)
    return render(request, 'index.html')

def sgin(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            if user.is_active == True:
                login(request, user)
                return redirect("sginpg")
        else:
            # No backend authenticated the credentials
            return render(request, 'sgin.html')

    return render(request, 'sgin.html')

def sginpg(request):
    return render(request, 'sginpg.html')

# def regst(request):
#     if request.method == "POST":
#         name = request.POST.get('fname')
#         phone = request.POST.get('phnum')
#         email = request.POST.get('email')
#         state = request.POST.get('state')
#         addr = request.POST.get('address')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         u = User.objects.create_user(username=username, email=email, password=password, first_name=name)
#         u.is_active = False 
#         u.save()
#         send_email(u)
#         usr = Userinfo(full_Name=name, phone=phone, email=email, state=state, address=addr, username=username)
#         usr.save()
#         return render(request, 'email_sent.html')

#     return render(request, 'register.html')

def email_sent(request):
    return render(request, 'email_sent.html')

def regst(request):
    if request.method == 'POST':
        form = createUserForm(request.POST)
        profile_form = UserinfoForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            send_email(user)
            messages.success(request,  'Your account has been successfully created!')
            return redirect("email_sent")
    else:
        form = createUserForm()
        profile_form = UserinfoForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)