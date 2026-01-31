import asyncio
from aiohttp import web
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    TurnContext,
)
from botbuilder.schema import Activity
from bot import MyBot

# 1. Configuración (Vacío para local)
SETTINGS = BotFrameworkAdapterSettings("", "")
ADAPTER = BotFrameworkAdapter(SETTINGS)
BOT = MyBot()

# 2. Manejador de mensajes
async def messages(req: web.Request) -> web.Response:
    # Verificamos que sea un JSON
    body = await req.json()
    
    # Convertimos el JSON crudo en un objeto Activity de Bot Framework
    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")

    try:
        # Procesamos la actividad
        await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
        return web.Response(status=201)
    except Exception as e:
        print(f"Error en el procesamiento: {e}")
        return web.Response(status=500)

# 3. Configuración del Servidor
APP = web.Application()
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    print("Bot corriendo en http://localhost:3978/api/messages")
    web.run_app(APP, host="localhost", port=3978)
