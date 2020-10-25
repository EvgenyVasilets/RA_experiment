from numpy import random
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
import pandas as pd
import random

author = 'Evgeny Vasilets'

doc = """
This is the experiment investigating the nature of loss-aversion.
"""


class Constants(BaseConstants):
    name_in_url = 'risk_aversion'
    players_per_group = None
    num_trial_rounds = 42
    num_practice_rounds = 3
    num_rounds = num_trial_rounds + num_practice_rounds


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # assign prolific id
# variables that are saved for each participant
    # demographic questions
    consent = models.IntegerField(choices=[
        [1, 'I agree to the conditions and want to participate in the study.'],
         [2, 'I do not agree to participate.']
    ], widget=widgets.RadioSelect)
    demography_age = models.IntegerField(label="Your age", max=99, min=5)
    demography_country = models.StringField(label="What country do you live in now?")
    demography_gender = models.IntegerField( label="Which gender do you identify most with?", choices=[
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Other'],
        [4, 'Prefer not to say']
    ])
    strategy = models.LongStringField(label="Could you explain how did you decide to accept or reject the gambles in each trial?")
    # anwers to the questions checking the understanding of instructions
    q1 = models.StringField(label="How many decisions are you going to make (without counting the practice trials)?", blank = True)
    q2 = models.StringField(label = "How many outcomes will affect your payment?", blank = True)
    q3 = models.IntegerField(
        label="To accept a lottery, you need to press:",
        choices=[
            [1, '↑'],
            [2, '↓']
        ],
        blank = True
    )
    q4 = models.IntegerField(
        label="Can the lottery, selected in the end, come from the first 3 trials?",
        choices=[
            [1, 'Yes'],
            [2, 'No']
        ],
        blank = True
    )
    # random generated int that defines randomisation order for each participant
    confidence = models.IntegerField(blank=True)
    prolific_id = models.StringField()
    rand_int = models.IntegerField()
    # Long or short
    fixations = models.StringField()
    # Condition numbers: 1 - equal, 2 - gains are longer, 3 - gains are super longer, 4 - losses are longer, 5 - losses are super longer
    condition_number = models.IntegerField()
    # number of a trial in a non-randomised data-frame
    original_trial_num = models.IntegerField()
    # 1 = accepted, 0 = rejected, -1 = no decision was made
    decision = models.IntegerField(blank=True)
    # smaller,equal,larger
    longer_exposure_to = models.StringField()
    # values in ECU
    lose_value = models.IntegerField()
    gain_value = models.IntegerField()
    # binary: 0 - real trials, 1 - training trials
    practice_trial = models.IntegerField()
    # win or lose
    row_number = models.IntegerField()
    # how much a participant wins/loses
    lottery_result = models.IntegerField(blank=True)
    # time per decision in ms
    decision_time_ms = models.IntegerField()
    # write down gains and loss conditions (high or low)
    gain_condition = models.StringField()
    loss_condition = models.StringField()
    fixation_time_gain = models.IntegerField()
    fixation_time_loss = models.IntegerField()
    # record the number of fixations for losses and gains
    fixation_number_gains = models.IntegerField(blank=True)
    fixation_number_losses = models.IntegerField(blank=True)
    def lottery(self):
    # this function defines how much a participant wins or loses at the end of the experiment.
        values = []
        for ind in range(Constants.num_rounds):
            rnd_num = ind+1
            if (self.in_round(rnd_num).decision == 1) & (self.in_round(rnd_num).practice_trials() == 0):
                win_value = random.choice([self.in_round(rnd_num).gain_value, self.in_round(rnd_num).lose_value])
                values.append(win_value)
        if not values:
            final_value = 0
        else:
            final_value = random.choice(values)
        return final_value

    def treatments_player(self):
        self.prolific_id = self.participant.label
        # create the dictionary with the variables
        treatments_dic = {
            'original_trial_num': [],
            'condition_number': [],
            'condition_name': [],
            'lose_value': [],
            'gain_value': [],
            'gain_condition':[],
            'loss_condition':[],
            'fixation_time_loss': [],
            'fixation_time_gain': [],
        }


        condition_names = ['losses_are_longer', 'losses_are_super_longer', 'equal', 'gains_are_longer', 'gains_are_super_longer']  # -1 - losses, 0 - equal, 1 - gains (used to be last_fix_longer)
        # Losses
        low_losses = list(range(-10, -20, -1))
        high_losses = list(range(-20, -30, -1))
        losses_lists = [high_losses, low_losses]
        # Gains
        low_gains = list(range(20, 30, 1))
        high_gains = list(range(30, 40, 1))
        gains_lists = [low_gains, high_gains]
        # Duration of long and short fixations (in ms)
        fixation_duration = 400
        fixation_duration_long = 600
        fixation_duration_super_long = 800
        # Counter of the rows in the treatment table
        count = 1
        # Create a dictionary with all conditions
        # Each condition will be repeated 2 times
        for round in range(2):
            for condition_name in condition_names:
                for losses in losses_lists:
                    for gains in gains_lists:
                        gain = random.choice(gains)
                        lose = random.choice(losses)
                        treatments_dic['original_trial_num'].append(count)
                        treatments_dic['condition_name'].append(condition_name)
                        treatments_dic['lose_value'].append(lose)
                        treatments_dic['gain_value'].append(gain)
                        # Define the value conditions
                        if gains == low_gains:
                            treatments_dic['gain_condition'].append('low_gains')
                        elif gains == high_gains:
                            treatments_dic['gain_condition'].append('high_gains')
                        if losses == high_losses:
                            treatments_dic['loss_condition'].append('high_losses')
                        elif losses == low_losses:
                            treatments_dic['loss_condition'].append('low_losses')
                        # Define fixation times for gains and losses in the trial (depends on fixation and longer exposure to)
                        def fix_times_gains_and_losses(condition_name):
                            # The function returns 3 values: first one is gain, the second one is the loss fixation time and the third is the condition number
                            return {
                                'losses_are_longer': [fixation_duration, fixation_duration_long, 4],
                                'losses_are_super_longer': [fixation_duration, fixation_duration_super_long, 5],
                                'gains_are_longer': [fixation_duration_long, fixation_duration, 2],
                                'gains_are_super_longer': [fixation_duration_super_long, fixation_duration, 3],
                                'equal': [fixation_duration, fixation_duration, 1],
                            }[condition_name]
                        fixation_time_gain, fixation_time_loss, condition_number = fix_times_gains_and_losses(condition_name)
                        treatments_dic['fixation_time_gain'].append(fixation_time_gain)
                        treatments_dic['fixation_time_loss'].append(fixation_time_loss)
                        treatments_dic['condition_number'].append(condition_number)

        # add 2 more fixations (0, -30 and 0, 40)
        extra_fixations = [[-30, 0], [0, 40]]
        for pair in extra_fixations:
            treatments_dic['original_trial_num'].append(count)
            treatments_dic['condition_name'].append('check_question')
            treatments_dic['lose_value'].append(pair[0])
            treatments_dic['gain_value'].append(pair[1])
            treatments_dic['gain_condition'].append(None)
            treatments_dic['loss_condition'].append(None)
            treatments_dic['fixation_time_loss'].append(fixation_duration)
            treatments_dic['fixation_time_gain'].append(fixation_duration)
            treatments_dic['condition_number'].append(99)
            count += 1
        treatments_df = pd.DataFrame(treatments_dic)
        # randomize the table using a randomly generated number (which will be the same for all trials for a specific participant)
        randomized = treatments_df.sample(frac=1, random_state=self.in_round(1).rand_int)
        # re-index the new table in order so we could present the new randomized table from start to the end
        randomized['new_indexing'] = list(range(0, len(randomized)))
        randomized = randomized.set_index(randomized['new_indexing'])
        # Check whether the trials are practice to decide whether to show random or
        # ordered rows from the randomized table
        pt = self.practice_trials()
        if pt == 0:
            row_number = self.round_number - 1 - Constants.num_practice_rounds
        elif pt == 1:
            # select random trials from trials with equal and not equal fixations
            if  self.round_number % 2 == 0:
                appropriate_trials = randomized[randomized['condition_name'] == 'equal']
            else:
                appropriate_trials = randomized[randomized['condition_name'] != 'equal']
            row_number = int(appropriate_trials.sample().index[0])

        # write down the data for the participant for each row so we can see it during the data analysis
        self.original_trial_num = randomized.loc[row_number, 'original_trial_num']
        self.lose_value = randomized.loc[row_number, 'lose_value']
        self.gain_value = randomized.loc[row_number, 'gain_value']
        self.longer_exposure_to = randomized.loc[row_number, 'condition_name']
        self.row_number = row_number
        self.gain_condition = randomized.loc[row_number, 'gain_condition']
        self.loss_condition = randomized.loc[row_number, 'loss_condition']
        self.fixation_time_loss = randomized.loc[row_number, 'fixation_time_loss']
        self.fixation_time_gain = randomized.loc[row_number, 'fixation_time_gain']
        self.condition_number = randomized.loc[row_number, 'condition_number']

        return randomized
    def practice_trials(self):
        # this function defines whether these trials are training or test
        if self.round_number > Constants.num_practice_rounds:
            self.practice_trial = 0
            return 0
        else:
            self.practice_trial = 1
            return 1


