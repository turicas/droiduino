from django.http import HttpResponse
from models import FanState
import time


def fan(request):
    try:
        fan_state = FanState.objects.all()[0]
    except IndexError:
        fan_state = FanState()

    if request.GET.get('arduino', 0):
        fan_state.last_call = time.time()
    fan_state.update_availability()
    if not fan_state.available:
        fan_state.save()
        return HttpResponse('Fan is not available', status=503)

    if request.method == 'GET':
        fan_state.save()
        return HttpResponse(str(fan_state.speed))

    elif request.method == 'POST':
        new_speed = request.POST.get('speed', None)

        try:
            new_speed = int(new_speed)
            if not 0 <= new_speed <= 3:
                raise ValueError
        except (TypeError, ValueError):
            fan_state.save()
            return HttpResponse('Invalid speed', status=400)

        fan_state.speed = new_speed
        fan_state.save()
        return HttpResponse(str(fan_state.speed))
