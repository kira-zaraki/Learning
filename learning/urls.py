from django.urls import path
from . import views

'''appname='learning'''''
urlpatterns=[
    path('', views.index, name='index'),
    path('data',views.data, name='data'),
    path('detail/<int:id>', views.cours_detail, name='cours_detail'),
    path('accounts/signup', views.signup ,name='signup'),
    path('accounts/profile', views.profile ,name='profile'),
    path('cours/<int:id>/edite', views.edit_cours,name='edit_cours'),
    path('section/<int:section_id>/edite', views.page,name='dashboard_cours'),



    path('live', views.live, name='live'),
    path('get_stream', views.get_stream, name='get_stream'),
    path('server', views.server, name='server'),
    path('live/<str:room_name>/', views.room, name='room'),
    path('webrtc', views.webrtc, name='webrtc')
]