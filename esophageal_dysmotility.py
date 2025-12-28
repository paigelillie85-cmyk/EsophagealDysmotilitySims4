import random
from sims4 import services
from event_testing.test_events import TestEvent

TRAIT_ED = 991000000001
BUFF_PAIN = 991000000002
BUFF_FATIGUE = 991000000003
BUFF_MEDICATED = 991000000004

def on_interaction_complete(event):
    sim = event.sim
    if sim is None:
        return

    sim_info = sim.sim_info

    if not sim_info.has_trait(TRAIT_ED):
        return

    # Medication reduces symptoms
    if sim_info.has_buff(BUFF_MEDICATED):
        flare_chance = 0.15
    else:
        flare_chance = 0.4

    if "Eat" in str(event.interaction):
        if random.random() < flare_chance:
            sim_info.add_buff(BUFF_PAIN)
            if random.random() < 0.5:
                sim_info.add_buff(BUFF_FATIGUE)

def register():
    services.get_event_manager().register_single_event(
        on_interaction_complete,
        TestEvent.InteractionComplete
    )

register()