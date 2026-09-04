from django.urls import path

from . import views

urlpatterns = [
    # Código 1 — view síncrona (bloqueante) que devolve JSON
    path("api/", views.api, name="api"),
    # Código 3 — view síncrona que faz chamadas HTTP bloqueantes
    path("sync/", views.sync_view, name="sync_view"),
    # Código 2/3 — view assíncrona fire-and-forget (da aula)
    path("async/", views.async_view, name="async_view"),
]
