
from django.shortcuts import render, redirect
from .models import Group, Message,Userinfo
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import CreateTodo
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django_email_verification import send_email
from .models import Userinfo
from .forms import createUserForm, UserinfoForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        usr_eml = request.POST.get('email')
        phone = request.POST.get('phnum')
        message = request.POST['msg']
        # send_mail(subject, message, from-email, receiver, fail silently)
        send_mail(fname,
                    "User Phone:-  "+phone+"\n"+"User Email:- "+usr_eml+"\n"+message,
                    "ss.blognchat@gmail.com",
                    ['ss.blognchat@gmail.com'],
                    fail_silently=True)
        messages.success(request, 'Thank you for the message! We\'ll respond to you shortly!!')    


    return render(request, 'index.html')

@login_required(login_url='/sin')
def chat(request):
    return render(request,'page.html')

@login_required(login_url='/sin')
def room(request, room):
    username = request.user.username
    room_details = Group.objects.get(name=room)
    return render(request, 'group.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

@login_required(login_url='/sin')
def checkview(request):
    room = request.POST['room_name']
    username = request.user.username
    if Group.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        messages.error(request, 'No such grp found!!')
        return render(request, 'page.html')
        #new_room = Room.objects.create(name=room)
        #new_room.save()
        #return redirect('/'+room+'/?username='+username)

@login_required(login_url='/sin')
def mynewroom(request):
    room = request.POST['room_name']
    username = request.user.username
    if Group.objects.filter(name=room).exists():
        messages.error(request, 'Already a group exists by this name. Please choose another name!!')
        return render(request, 'page.html')
    else:
        new_room=Group.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
 
@login_required(login_url='/sin')
def send(request):
    message = request.POST['message']
    username = request.user.username
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message has been sent successfully')

@login_required(login_url='/sin')
def getMessages(request, room):
    room_details = Group.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


# Create your views here.
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
                return redirect("index")
            else:
                messages.error(request, 'Verify your email to log in !!')    

        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password!')    
            return render(request, 'sgin.html')

    return render(request, 'sgin.html')

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
            return redirect("email_sent")
    else:
        form = createUserForm()
        profile_form = UserinfoForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)

def blog(request):
    return render(request, 'blog.html')

@login_required(login_url='/sin')
def change_pass(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Password changed successfully!')    
            update_session_auth_hash(request, fm.user)
            return redirect("index")
    else:
        fm = PasswordChangeForm(user = request.user)
            
    return render(request, 'change_pass.html', {'form':fm})

class TaskList(LoginRequiredMixin, ListView):
    model = CreateTodo
    context_object_name = 'task_list'
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(complete=False).count()
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = CreateTodo
    fields = ['title', 'descr', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = CreateTodo
    fields = ['title', 'descr', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'task_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate, self).form_valid(form)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = CreateTodo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'task_delete.html'