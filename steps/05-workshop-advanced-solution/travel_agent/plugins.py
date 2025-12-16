from google.adk.agents import InvocationContext
from google.adk.plugins import BasePlugin
from google.genai import types

from .schemas import TravelRequest


class TravelAuditPlugin(BasePlugin):
    """Plugin pour auditer toutes les interactions du système de voyage"""

    def __init__(self):
        super().__init__(name="TravelAuditPlugin")
        self.request_count = 0

    async def on_user_message_callback(
        self, invocation_context: InvocationContext, user_message: types.Content
    ) -> None:
        """Callback exécuté à chaque message utilisateur"""
        user_request = user_message.parts[0].text
        input_data = TravelRequest.model_validate_json(user_request)
        self.request_count += 1
        log_entry = f"\n=== Request #{self.request_count} ===\n"
        log_entry += f"Agent: {invocation_context.agent.name}\n"
        log_entry += f"Destination: {input_data.destination}\n"
        log_entry += f"Budget: {input_data.budget}€\n"
        print(f"Plugin's log entry:\n{log_entry}")
        # En production, vous écririez dans un fichier ou BigQuery
