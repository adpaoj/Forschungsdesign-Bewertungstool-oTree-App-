from otree.api import *
import os, random

class C(BaseConstants):
    NAME_IN_URL = 'research_design_rater'
    PLAYERS_PER_GROUP = None

    # Base directory for static PDFs
    base_dir = os.path.dirname(__file__)
    pdf_dir_de = os.path.join(base_dir, 'static/research_design_rater/designs/pdf_de')
    pdf_dir_en = os.path.join(base_dir, 'static/research_design_rater/designs/pdf_en')

    # Count total PDFs
    NUM_ROUNDS = len([f for f in os.listdir(pdf_dir_de) if f.endswith('.pdf')]) + \
                 len([f for f in os.listdir(pdf_dir_en) if f.endswith('.pdf')])

class Subsession(BaseSubsession):
    def creating_session(self):
        # Read PDFs from both folders
        pdf_files_de = [os.path.join('pdf_de', f) for f in os.listdir(C.pdf_dir_de) if f.endswith('.pdf')]
        pdf_files_en = [os.path.join('pdf_en', f) for f in os.listdir(C.pdf_dir_en) if f.endswith('.pdf')]

        # Combine both languages
        all_pdfs = pdf_files_de + pdf_files_en

        # Shuffle per participant
        for p in self.get_players():
            shuffled = all_pdfs.copy()
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
