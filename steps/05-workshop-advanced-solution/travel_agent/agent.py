from google.adk.agents.context_cache_config import ContextCacheConfig
from google.adk.agents.llm_agent import Agent
from google.adk.apps import App
from google.adk.apps.app import EventsCompactionConfig

from .callbacks import validate_and_log
from .plugins import TravelAuditPlugin
from .schemas import TravelRequest, TravelResponse

TRAVEL_GUIDE = """
# Guide de Voyage Détaillé

## Paris
- Monuments: Tour Eiffel (25€), Louvre (17€), Arc de Triomphe (13€)
- Restaurants: Budget 15-80€/repas selon standing
- Transport: Navigo semaine 30€, ticket unique 2.10€
- Hébergement: Auberge 25-40€, Hôtel 2* 60-100€, Hôtel 4* 150-300€

## Londres
- Monuments: British Museum (gratuit), Tower of London (34£), London Eye (32£)
- Transport: Oyster card zones 1-2 ~40£/semaine
- Hébergement: Auberge 30-50£, Hôtel 80-200£

## Rome
- Monuments: Colisée (18€), Vatican (17€), Fontaine de Trevi (gratuit)
- Restaurants: 10-50€/repas
- Transport: Pass 7 jours 24€
- Hébergement: Auberge 20-35€, Hôtel 60-150€

## Barcelone
- Monuments: Sagrada Familia (26€), Park Güell (10€), Casa Batlló (25€)
- Restaurants: Tapas 3-8€, restaurant 15-40€
- Transport: T-10 (10 trajets) 11.35€
- Hébergement: Auberge 20-40€, Hôtel 70-180€
"""

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction=f"""
        You are an expert travel planning assistant with access to detailed city guides.

        {TRAVEL_GUIDE}

        Based on the user's destination, budget, days, and interests:
        1. Use the guide data to provide accurate pricing
        2. Calculate realistic daily budgets
        3. Suggest activities that match their interests and budget
        4. Recommend appropriate accommodation
        5. Provide a total cost estimate

        Always stay within the user's budget and be creative with free/low-cost activities if needed.
    """,
    input_schema=TravelRequest,
    output_schema=TravelResponse,
    before_agent_callback=validate_and_log,
)

context_cache_config = ContextCacheConfig(
    min_tokens=2048,  # Cache si > 2048 tokens
    ttl_seconds=3600,  # Cache valide 1h
    cache_intervals=5,  # Mise à jour tous les 5 appels
)

event_compaction_config = EventsCompactionConfig(
    compaction_interval=3,  # Compacter après chaque 3 invocations uniques
    overlap_size=1,  # Chevauchement de 1 invocation entre compactages
)
app = App(
    name="travel_agent",
    root_agent=root_agent,
    plugins=[TravelAuditPlugin()],
    context_cache_config=context_cache_config,
)
