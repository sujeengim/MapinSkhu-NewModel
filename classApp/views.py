from django.shortcuts import render, get_object_or_404
from .models import Classes, Room
from django.utils import timezone
from django.db.models import Q, F

# Create your views here.
def test(request):
    days = ['토', '일', '월', '화', '수', '목', '금', ]
    now = timezone.now()
    now_date = now.date()
    now_time = now.time()
    weekday = now.weekday()
    now_weekday = days[weekday]
    
    rooms = Room.objects.filter(Q(kwan_name = "정보과학관"))
    classes = Classes.objects.filter(Q(kwan_name = "정보과학관") & (Q(date1 = now_weekday) | Q(date2 = now_weekday)) & (Q(start__lte = now_time) & Q(end__gte = now_time)))

    rooms_list = []
    classes_list = []

    for r in rooms:
        rooms_list.append(r.room)
        for c in classes:
            if r.room == c.room:
                classes_list.append(c)
                if len(classes_list) < 1:
                    room_type = "사용가능"
                else:
                    room_type = "사용불가"

    return render(request, 'test.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday,
    'rooms': rooms, 'classes': classes, 'room_type': room_type, 'rooms_list': rooms_list, 'classes_list': classes_list})

def classroom(request, room, id): #unit==unit_id==Class.room_id, id==classroom.id
    rooms = get_object_or_404(Room, room = room, id = id)
    classes = Classes.objects.all().order_by('end')
    
    days = ['월', '화', '수', '목', '금', '토', '일']
    now = timezone.now()
    now_date = now.date()
    now_time = now.time()
    weekday = now.weekday()
    now_weekday = days[weekday]

    return render(request, 'classroom.html', 
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday,
    'classes': classes, 'rooms': rooms})