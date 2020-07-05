from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = 'player'
    form_fields = ['rand_int', 'q1', 'q2', 'q3', 'q4']
    def vars_for_template(self):
        if self.round_number == 1:
            instruction_type = 0
        else:
            instruction_type = 1
        return dict (
            instruction_type = instruction_type
        )
    def is_displayed(self):
        if self.round_number == 1:
            return True
    def error_message(self, values):
        if (values['q1'] != "24") or (values['q2'] != "1") or (values['q3'] != 1) or (values['q4'] != 2) and (self.round_number == 1):
            return 'Some of your answers contain an error'

class Instructions2(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_practice_rounds + 1:
            return True

class Attention(Page):
    def is_displayed(self):
        return self.round_number == 1
            
class Trial(Page):
    def vars_for_template(self):
        randomized_table = self.player.treatments_player()
        row_for_the_trial = randomized_table.iloc[self.player.row_number]
        return dict(
            original_trial_num = row_for_the_trial['original_trial_num'],
            first_fix_value = row_for_the_trial['first_fix_value'],
            last_fix_value = row_for_the_trial['last_fix_value'],
            number_of_fixations = row_for_the_trial['number_of_fixations'],
            lose_time_1 = self.player.lose_time_1,
            lose_time_2 = self.player.lose_time_2,
            lose_time_3 = self.player.lose_time_3,
            lose_time_4 = self.player.lose_time_4,
            lose_time_5 = self.player.lose_time_5,
            gain_time_1 = self.player.gain_time_1,
            gain_time_2 = self.player.gain_time_2,
            gain_time_3 = self.player.gain_time_3,
            gain_time_4 = self.player.gain_time_4,
            gain_time_5 = self.player.gain_time_5,
            lose_value = row_for_the_trial['lose_value'],
            gain_value = row_for_the_trial['gain_value']
        )

    def js_vars(self):
        randomized_table = self.player.treatments_player()
        row_for_the_trial = randomized_table.iloc[self.player.row_number]
        return dict(
            first_fix_value=row_for_the_trial['first_fix_value']
        )
class Decision(Page):
    form_model = 'player'
    form_fields = ['decision', 'decision_time_ms']
    # def js_vars(self):
    #     if self.round_number > 1:
    #         current_ecu = self.player.in_round(self.round_number - 1).ECU
    #     else:
    #         current_ecu = self.player.in_round(self.round_number).ECU
    #     lose_val = self.player.lose_value
    #     gain_val = self.player.gain_value
    #     return dict(
    #         ECU_if_win = current_ecu + gain_val,
    #         ECU_if_lose = current_ecu + lose_val,
    #         ECU_no_change = current_ecu
    #     )

class ResultsWaitPage(WaitPage):
    pass

class Middle_page(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_practice_rounds + (Constants.num_trial_rounds//2)

class Results(Page):
    form_model = 'player'
    form_fields = ['lottery_result']
    def js_vars(self):
        return dict(
            lottery_result = self.player.lottery()
        )
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [Instructions, Instructions2, Attention, Trial, Decision, Middle_page, Results]
