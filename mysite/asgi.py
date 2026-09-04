"""
Configuração ASGI do projeto mysite.

O ASGI é o que permite que as views assíncronas (async def) realmente
rodem em um event loop, aproveitando o não-bloqueio de I/O.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()
