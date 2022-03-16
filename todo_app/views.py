from django.shortcuts import render,redirect
from .models import ReminderThings
from .forms import ReminderForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def reminder(request):
    form = ReminderForm()
    data = ReminderThings.objects.filter(user=request.user)
    if request.method == "POST":
        form = ReminderForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('reminder')
    else:
        all_rem = ReminderThings.objects.filter(user=request.user)
        return render(request, 'reminder.html', {'form':form, 'data':data, 'all_rem':all_rem})

@login_required
def delete(request, id):
    thing = ReminderThings.objects.get(pk=id)
    thing.delete()
    return redirect('reminder')

@login_required
def complete(request, id):
    thing = ReminderThings.objects.get(pk=id)
    thing.status = True
    thing.save()

    return redirect('reminder')

@login_required
def pending(request, id):
    thing = ReminderThings.objects.get(pk=id)
    thing.status = False
    thing.save()
    
    return redirect('reminder')


@login_required
def edit(request, id):
    thing = ReminderThings.objects.get(id=id)
    if request.method == "POST":
        rem_form = ReminderForm(request.POST or None, instance=thing)
        if rem_form.is_valid():
            rem_form.save()
        return redirect('reminder')
    else:
        rem_form = ReminderForm(request.POST or None, instance=thing)
        edit_rem = ReminderThings.objects.get(id=id)
        return render(request, 'edit.html', {'edit_rem':edit_rem, 'rem_form':rem_form})
