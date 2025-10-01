# backend_api/views.py
from django.http import JsonResponse

def ping(request):
    return JsonResponse({"ok": True, "msg": "pong"})
