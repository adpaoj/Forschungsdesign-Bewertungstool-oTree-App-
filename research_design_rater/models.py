from otree.api import *
import os
import random

APP_DIR = os.path.dirname(__file__)
DESIGNS_DIR = os.path.join(APP_DIR, "designs")

def load_designs():
    designs = []
    if os.path.exists(DESIGNS_DIR):
        files = sorted(f for f in os.listdir(DESIGNS_DIR) if f.endswith(".txt"))
        for f in files:
            id_str = os.path.splitext(f)[0]   # "1.txt" -> "1"
            with open(os.path.join(DESIGNS_DIR, f), encoding="utf-8") as fh:
                text = fh.read().strip()
            designs.append({
                "id": int(id_str),
                "text": text
            })
    return designs


DESIGNS = load_designs()


class C(BaseConstants):
    NAME_IN_URL = 'research_design_rater'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = len(DESIGNS)


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            order = list(range(C.NUM_ROUNDS))
            random.shuffle(order)  # random order per participant
            p.participant.vars['design_order'] = order


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    design_id = models.IntegerField()
    design_text = models.LongStringField()
    
    rating = models.IntegerField(label="Rating (1–7)", min=1, max=7)
    comment = models.LongStringField(blank=True, label="Comment (optional)")

    def current_design(self):
        order = self.participant.vars['design_order']
        idx = order[self.round_number - 1]  # convert 1-indexed to 0
        return DESIGNS[idx]
