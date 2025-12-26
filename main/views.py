from django.shortcuts import render,redirect
from reservation.models import Reservation
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from service.models import Service
from timeslot.models import Timeslot
from reservation.models import Reservation
from django.contrib.auth import logout
# Create your views here.



#home
def home (request):
    return render (request,"main/home.html")


@login_required
def dashboard(request):
    user = request.user
    reservations = Reservation.objects.filter(user = user )
    context = {
        "user":user,
        "reservations": reservations,
    }
    return render(request, 'main/dashboard.html',context)

#register
def register(request):

    
    if request.method =="POST":
         
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")
        
    else:
        form = CustomUserCreationForm()
    return render(request,"registration/register.html",{"form":form})


#creat_reservation

@login_required
def create_reservation(request):
    if request.method == 'POST':
        service_id = request.POST.get('service')
        time_slot_id = request.POST.get('time_slot')
        service = Service.objects.get(id=service_id)
        time_slot = Timeslot.objects.get(id=time_slot_id)

        if Reservation.objects.filter(user=request.user, service=service, time_slot=time_slot).exists():
            return render(request, 'main/create_reservation.html', {'error': 'این زمان قبلاً رزرو شده است.'})

        
        reservation = Reservation.objects.create(
            user=request.user,
            service=service,
            time_slot=time_slot,
            status='pending'
        )

        
        time_slot.is_available = False
        time_slot.save()

        return redirect('/dashboard/')
    else:
        from datetime import date
        services = Service.objects.all()
    
        time_slots = Timeslot.objects.filter(is_available=True, date__gte=date.today())
        return render(request, 'main/create_reservation.html', {'services': services, 'time_slots': time_slots})




#delit reservarion

@login_required
def delete_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id, user=request.user)
        reservation.time_slot.is_available = True  
        reservation.time_slot.save()
        reservation.delete()
    except Reservation.DoesNotExist:
        pass
    return redirect('dashboard')


def user_logout(request):
    logout(request)
    return redirect('home') 