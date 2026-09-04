# mysite_async

Projeto Django base da aula de **Async Views**.

## Instalação

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

## Rodando o projeto

```bash
python manage.py runserver
# ou, para ASGI de verdade:
uvicorn mysite.asgi:application --reload
```

## Rotas disponíveis

| Rota      | Tipo | Descrição                                                                 |
|-----------|------|-----------------------------------------------------------------------------|
| `/api/`   | sync | Código 1 da aula — `time.sleep(1)` e devolve JSON                          |
| `/sync/`  | sync | Faz requisições HTTP de forma bloqueante                                    |
| `/async/` | async| Dispara `http_call_async()` como task e responde na hora (fire-and-forget) |

## Correções feitas no código enviado (Código 2 e 3)

O "Código 3" da aula estava sem os `import`s (`asyncio`, `httpx`, `time`) e
com uma indentação incorreta em `http_call_async`: o bloco
`async with httpx.AsyncClient()` tinha saído de dentro da função por engano
(ficava no mesmo nível do `for`, quebrando a função). Isso foi corrigido em
`core/views.py`.
