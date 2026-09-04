import asyncio
import time

import httpx
from django.http import HttpResponse, JsonResponse


# ---------------------------------------------------------------------------
# Código 1 (da aula) — view SÍNCRONA que "trava" a thread por 1 segundo.
# ---------------------------------------------------------------------------
def api(request):
    time.sleep(1)
    payload = {"message": "Hello, World!"}

    if "task_id" in request.GET:
        payload["task_id"] = request.GET["task_id"]
    return JsonResponse(payload)


# ---------------------------------------------------------------------------
# Código 2/3 (da aula) — corrigidos: faltavam os imports (asyncio, httpx,
# time) e a indentação de `http_call_async` estava errada (o `async with`
# tinha saído do `for`).
# ---------------------------------------------------------------------------
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


def http_call_sync():
    for num in range(1, 6):
        time.sleep(1)
        print(num)

    r = httpx.get("https://httpbin.org/")
    print(r)


async def async_view(request):
    """Dispara a tarefa em segundo plano e responde na hora (non-blocking)."""
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


def sync_view(request):
    """Bloqueia a thread inteira até `http_call_sync` terminar."""
    http_call_sync()
    return HttpResponse("Blocking HTTP request")


