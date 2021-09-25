
from django.shortcuts import render, redirect
from .models import Group, Message,Userinfo
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import CreateTodo

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