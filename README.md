# mysite_async

Projeto Django baseado no exemplo da aula de **Async Views**, com uma nova
view assíncrona de contador de tempo.

## Instalação

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

## Rodando o projeto

Como o objetivo é testar código **assíncrono de verdade**, rode com um
servidor ASGI (o `runserver` padrão do Django também funciona a partir da
versão 3.1, mas o Uvicorn deixa mais evidente o comportamento non-blocking):

```bash
# opção 1: servidor de desenvolvimento do Django (mais simples)
python manage.py runserver

# opção 2: ASGI de verdade com Uvicorn
uvicorn mysite.asgi:application --reload
```

## Rotas disponíveis

| Rota                              | Tipo             | Descrição                                                                 |
|-----------------------------------|------------------|-----------------------------------------------------------------------------|
| `/api/`                           | sync             | Código 1 da aula — `time.sleep(1)` e devolve JSON                          |
| `/sync/`                          | sync             | Faz requisições HTTP de forma bloqueante                                    |
| `/async/`                         | async            | Dispara `http_call_async()` como task e responde na hora (fire-and-forget) |
| `/async-counter/`                 | **async (novo)** | Conta de 1 a N segundos com `asyncio.sleep`, aguarda e retorna JSON no fim |
| `/async-counter-background/`      | **async (novo)** | Mesmo contador, mas em background — resposta é imediata                    |

Parâmetros de query aceitos em `/async-counter/` e `/async-counter-background/`:

- `?seconds=10` — quantos segundos contar (padrão 5, máximo 30)
- `?task_id=abc123` — é ecoado de volta no JSON de resposta (igual ao Código 1)

## O que a nova view (`async_counter_view`) demonstra

- Ela usa `await asyncio.sleep(1)` em vez de `time.sleep(1)`. A diferença é
  que `asyncio.sleep` **libera o event loop** durante a espera, então o
  servidor pode atender outras requisições enquanto essa está "contando".
  Com `time.sleep` (síncrono), a thread inteira fica travada.
- Para comprovar isso na prática, abra dois terminais e rode ao mesmo tempo:

  ```bash
  curl "http://127.0.0.1:8000/async-counter/?seconds=8"
  curl "http://127.0.0.1:8000/api/"
  ```

  Repare que o `/api/` (síncrono) responde rapidamente mesmo com o contador
  assíncrono ainda rodando — em vez de ficar na fila atrás dele (isso é mais
  visível ainda rodando via Uvicorn/ASGI com múltiplas requisições
  simultâneas, ou usando uma ferramenta de teste de carga como `hey` ou
  `ab`).

## Correções feitas no código enviado (Código 2 e 3)

O "Código 3" da aula estava sem os `import`s (`asyncio`, `httpx`, `time`) e
com uma indentação incorreta em `http_call_async`: o bloco
`async with httpx.AsyncClient()` tinha saído de dentro da função por engano
(ficava no mesmo nível do `for`, quebrando a função). Isso foi corrigido em
`core/views.py`.
