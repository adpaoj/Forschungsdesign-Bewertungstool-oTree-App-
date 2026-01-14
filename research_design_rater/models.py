from otree.api import *
import os, random

class C(BaseConstants):
    NAME_IN_URL = 'research_design_rater'
    PLAYERS_PER_GROUP = None
    base_dir = os.path.dirname(__file__)
    pdf_dir = os.path.join(base_dir, 'static/research_design_rater/designs')
    NUM_ROUNDS = len([f for f in os.listdir(pdf_dir) if f.endswith('.pdf')])

class Subsession(BaseSubsession):
    def creating_session(self):
        base_dir = os.path.dirname(__file__)
        pdf_dir = os.path.join(base_dir, 'static/research_design_rater/designs')
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

        # Shuffle per participant
        for p in self.get_players():
            shuffled = pdf_files.copy()
            random.shuffle(shuffled)
            p.participant.vars['pdf_order'] = shuffled

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    experiment_title = models.StringField()
    rating = models.IntegerField(
        min=1,
        max=5,
        label="Bewertung (1 = sehr schlecht, 5 = sehr gut)"
    )
    comment = models.LongStringField(
        blank=True,
        label="Kommentar (optional)"
    )

