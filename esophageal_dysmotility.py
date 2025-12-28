import random
from sims4 import services
from event_testing.test_events import TestEvent

TRAIT_ED = 1111111111
BUFF_PAIN = 2222222222
BUFF_FATIGUE = 3333333333

def on_interaction_complete(event):
    sim = event.sim
    if sim is None:
        return

    if not sim.sim_info.has_trait(TRAIT_ED):
        return

    if "Eat" in str(event.interaction):
        if random.random() < 0.4:
            sim.sim_info.add_buff(BUFF_PAIN)
            if random.random() < 0.5:
                sim.sim_info.add_buff(BUFF_FATIGUE)

def register():
    services.get_event_manager().register_single_event(
        on_interaction_complete,
        TestEvent.InteractionComplete
    )

register()