from django.db import DatabaseError, connection
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_safe


@require_safe
def home(request):
    return HttpResponse(
        "SALTY — development scaffold\n\n"
        "The application is running. Health: /health/\n"
        "Next: sample identities and an academic archive.\n"
        "No school accounts, student data, or live integrations are connected.\n",
        content_type="text/plain; charset=utf-8",
    )


@require_safe
@never_cache
def health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM django_migrations")
            if cursor.fetchone()[0] < 1:
                return JsonResponse({"status": "unavailable"}, status=503)
    except DatabaseError:
        return JsonResponse({"status": "unavailable"}, status=503)
    return JsonResponse({"status": "ok"})
