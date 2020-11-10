from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions2(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_practice_rounds + 1)

    def before_next_page(self):
        self.participant.vars['number_of_all_rounds'] = Constants.num_rounds
        self.participant.vars['number_of_practice_rounds'] = Constants.num_practice_rounds

class Attention(Page):
    def is_displayed(self):
        return (self.round_number == 1)
            
class Trial_and_decision(Page):
    form_model = 'player'
    form_fields = ['decision_X', 'decision_time_ms_X', 'fixation_number_gains_X', 'fixation_number_losses_X', 'left_X', 'first_X', 'last_screen_X']
    def vars_for_template(self):
        randomized_table = self.player.treatments_player()
        row_for_the_trial = randomized_table.iloc[self.player.row_number]
        return dict(
            original_trial_num = row_for_the_trial['original_trial_num_X'],
            fixation_time_gain = row_for_the_trial['fixation_time_gain_X'],
            fixation_time_loss = row_for_the_trial['fixation_time_loss_X'],
            lose_value = row_for_the_trial['lose_value_X'],
            gain_value = row_for_the_trial['gain_value_X']
        )
    def is_displayed(self):
        return self.round_number <= Constants.num_rounds #True
    def before_next_page(self):
        self.participant.vars[str(self.round_number)] = [self.player.decision_X, self.player.gain_value_X, self.player.lose_value_X]

class Feedback(Page):
    def vars_for_template(self):
        return dict(
            decision_X = self.player.decision_X,
        )
    def is_displayed(self):
        return self.round_number <= Constants.num_rounds #True

class Confidence(Page):
    form_model = 'player'
    form_fields = ['confidence_X', 'confidence_reaction_time_X']
    def is_displayed(self):
        decision_X = self.player.decision_X
        return (decision_X != -1) and (self.round_number <= Constants.num_rounds) #True

class ResultsWaitPage(WaitPage):
    pass

class Middle_page(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_practice_rounds + (Constants.num_trial_rounds//2))



page_sequence = [Instructions2, Attention, Trial_and_decision, Feedback, Confidence, Middle_page]
# real page sequence
# page_sequence = [ConsentForm, ConsentIfFalse, Instructions, Instructions2, Attention, Trial_and_decision, Feedback, Confidence, Middle_page, Demographics, Questionnaire,  Results]