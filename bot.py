from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

class MyBot(ActivityHandler):
    # Este método se activa cuando alguien entra al chat
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("¡Hola! Soy tu portero digital. 24/7 a tu servicio.")
                await turn_context.send_activity("¿Te gustaría: 1. Ver servicios, 2. Hablar con humano?")

    # Este método procesa lo que el usuario escribe
    async def on_message_activity(self, turn_context: TurnContext):
        text = turn_context.activity.text.lower()
        if "1" in text:
            await turn_context.send_activity("Ofrecemos desarrollo de IA y Cloud en Azure.")
        elif "2" in text:
            await turn_context.send_activity("Conectando con un agente... (Simulado)")
        else:
            await turn_context.send_activity(f"Dijiste: '{turn_context.activity.text}'. Elige 1 o 2.")
