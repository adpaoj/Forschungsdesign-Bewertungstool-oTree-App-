from otree.api import *
from .models import C

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class RateDesign(Page):
    form_model = 'player'
    form_fields = ['rating', 'comment']

    def vars_for_template(self):
        # Use the participant-specific shuffled list
        pdf_file = self.player.participant.vars['pdf_order'][self.round_number - 1]
        self.player.experiment_title = pdf_file

        return {
            'pdf_path': f"research_design_rater/designs/{pdf_file}",
            'current': self.round_number,
            'total': C.NUM_ROUNDS
        }

class ThankYou(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS

page_sequence = [
    Introduction,
    RateDesign,
    ThankYou
]
