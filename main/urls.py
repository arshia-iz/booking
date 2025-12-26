from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("register/",views.register,name="register"),
    path("create_reservation/",views.create_reservation,name="create_reservation"),
    path('logout/', views.user_logout, name='logout'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),

]
