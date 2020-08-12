from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from .models import Cours, Sections, Pages, Expoilted
from .forms import SingupForm, ExloitedForm, CoursForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import  login_required
import socket
import cv2
import json
# Create your views here.


def index(request):
    cours = Cours.objects.all()
    return render(request, 'learn/index.html',{'cours':cours})


def data(request):
    section_list = []
    # page_list = []
    # f = open('data.json', 'r')
    # for i in json.load(f):
    #     Cour = Cours(free=i['free'], title=i['title'],
    #                  available_seats=i['available_seats'], schedule=i['schedule'],
    #                  objectives=i['objectives'],eligibility=i['eligibility'])
    #     Cour.save()
    #     for s in i['section']:
    #         section = Sections(title=s['title'], detail=s['detail'], cour=Cour)
    #         section.save()
    #         # section_list.append(s)
    #         for p in s['page']:
    #             Page = Pages(title=p['title'], content=p['content'],
    #                          section=section)
    #             Page.save()
    # return HttpResponse(page_list)
    '''trainer-free-available_seats-schedule-picture-objectives-eligibility'''
        # Cour = Cours(free=i['free'],title=i['title'],
        #              available_seats=i['available_seats'], schedule=i['schedule'],
        #              objectives=i['objectives'],eligibility=i['eligibility'])
        # Cour.save()
        #
        # '''title-detail-cour'''
        # section = Sections(title=i['section'][0]['title'], detail=i['section'][0]['detail'],cour= Cour)
        # section.save()
        #
        # '''title-detail-section'''
        # Page = Pages(title=i['section'][0]['page'][0]['title'], content=i['section'][0]['page'][0]['content'], section= section)
        # Page.save()

    data = Cours.objects.all()

    return HttpResponse(data[0].free)




def cours_detail(request,id):
    cour = Cours.objects.get(id=id)

    # all_section = []
    # return HttpResponse(cour.sections_set.all())

    return render(request,'learn/cours_detail.html', {'cour': cour})



def signup(request):

    form = SingupForm()
    if request.POST:
        form = SingupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'registration/sign_up.html', {'form': form})



@login_required
def profile(request):
    user = request.user
    expoilted= user.exploited
    print(user.cours.all())
    # expoilted = Expoilted.objects.get(user = user)
    # print(expoilted)
    # user_e = user.expoilted_set.count()
    form = ExloitedForm(instance=expoilted)
    if request.POST:
        form = ExloitedForm(instance=expoilted, data=request.POST)
        if form.is_valid():
            form.save()
            user_e = form.save(commit=False)
            # user_e.user = user
            # user_e.user.add(user)
            # user.Expoilted = user_e

            # user_e.save()
            print('ok')


    return render(request,'registration/profile.html', {'User': request.user, 'form' : form})

@login_required
def edit_cours(request, id):
    cour = Cours.objects.get(id=id)
    form = CoursForm(instance=cour)
    if request.POST:
        form = CoursForm(request.POST, request.FILES, instance=cour)
        if form.is_valid():
            form.save()
            # return render(request, 'learn/dashboard_cours.html', {'form': form, 'cour': cour})
    return render(request, 'learn/edit_cours.html', {'form': form})

def page(request, section_id):
    section = Sections.objects.get(pk = section_id)

    return render(request, 'learn/dashboard_cours.html', {'section': section})


def server(request):
    # cap = cv2.VideoCapture(0)
    #
    # # while(True):
    # ret, frame = cap.read()
    #
    # ret, jpeg = cv2.imencode('.jpg', frame)
    # string = jpeg.tostring()
    # yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+string+b'\r\n')

    host = '127.0.0.1'

    port = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host,port))
        s.listen(1)

        conn, addr  = s.accept()
        print('s')
        while True:
            # conn.send("stream()")
            conn.send('test')
        s.close()

def get_stream(request):

    host = '127.0.0.1'
    port = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        # conn, addr = s.accept()
        while 1:
            print("d")
            d = s.recv(1024)
            print(d)

        s.close()
    return StreamingHttpResponse(get_servcer(),content_type='multipart/x-mixed-replace; boundary=frame')


def live(request):
    # return StreamingHttpResponse(stream(),content_type='multipart/x-mixed-replace; boundary=frame')
    return render(request, 'live/live.html')

def room(request, room_name):
    return render(request, 'live/room.html', {
        'room_name': room_name
    })


def webrtc(request):
    return render(request,'live/webrtc.html')