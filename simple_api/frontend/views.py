from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.conf import settings


def serve_frontend(request):
    if not settings.DEBUG:
        raise Http404
    print(request.path)
    return render(request, "index.html", context={})


@require_http_methods(["POST"])
def unsecure_relog(request):
    if not settings.DEBUG:
        raise Http404
    username = request.POST.get('username', None)
    data = {
        'Success': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
