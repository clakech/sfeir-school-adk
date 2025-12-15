from google.adk.agents.callback_context import CallbackContext

from .schemas import TravelRequest


def validate_and_log(callback_context: CallbackContext):
    """Callback exécuté avant l'agent"""
    input_data = callback_context._invocation_context.user_content.parts[0].text
    input_data = TravelRequest.model_validate_json(input_data)

    if input_data.budget < 200:
        print("⚠️ ATTENTION: Budget très limité, l'agent devra être créatif!")

    daily_budget = input_data.budget / input_data.days
    if daily_budget < 50:
        print(
            f"⚠️ Budget journalier: {daily_budget:.2f}€/jour - recommandations économiques nécessaires"
        )

    if input_data.budget < 100:
        raise ValueError(
            "Le budget total doit être au moins de 100€ pour planifier un voyage."
        )
