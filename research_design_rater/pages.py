from otree.api import Page
from .models import C, DESIGNS

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class RateDesign(Page):
    form_model = 'player'
    form_fields = ['rating', 'comment']

    def vars_for_template(self):
        design = self.player.current_design()
        return dict(
            design_text=design["text"],
            current=self.round_number,
            total=C.NUM_ROUNDS
        )

    
    def before_next_page(self):
        d = self.player.current_design()
        self.player.design_id = d["id"]
        self.player.design_text = d["text"]
    
class ThankYou(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS

page_sequence = [Introduction, RateDesign, ThankYou]