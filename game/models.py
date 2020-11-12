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
    name_in_url = 'RAE'
    players_per_group = None
    num_trial_rounds = 44
    num_practice_rounds = 3
    num_rounds = num_trial_rounds + num_practice_rounds


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    prolific_id = models.StringField()
    # Condition numbers: 1 - equal, 2 - gains are longer, 3 - gains are super longer, 4 - losses are longer, 5 - losses are super longer
    condition_number_X = models.IntegerField()
    # number of a trial in a non-randomised data-frame
    original_trial_num_X = models.IntegerField()
    # 1 = accepted, 0 = rejected, -1 = no decision was made
    decision_X = models.IntegerField(blank=True)
    # smaller,equal,larger
    condition_name_X = models.StringField()
    # values in ECU
    lose_value_X = models.IntegerField()
    gain_value_X = models.IntegerField()
    # binary: 0 - real trials, 1 - training trials
    practice_trial = models.IntegerField()
    # win or lose
    row_number = models.IntegerField()
    # time per decision in ms
    decision_time_ms_X = models.IntegerField()
    # write down gains and loss conditions (high or low)
    gain_condition_X = models.IntegerField()
    loss_condition_X = models.IntegerField()
    fixation_time_gain_X = models.IntegerField()
    fixation_time_loss_X = models.IntegerField()
    # record the number of fixations for losses and gains
    fixation_number_gains_X = models.IntegerField(blank=True)
    fixation_number_losses_X = models.IntegerField(blank=True)
    # each condition is repeated 2 times, so the repetition variable tracks this
    repetition = models.IntegerField()

    # -1 - left was loss, 1 - left was gain
    left_X = models.IntegerField()
    # -1 - first was loss, 1 - first was gain
    first_X = models.IntegerField()
    # -1 - last was loss, 1 - last was gain
    last_screen_X = models.IntegerField(blank=True)

    confidence_X = models.IntegerField(blank=True)
    # RT in ms
    confidence_reaction_time_X = models.IntegerField(blank=True)



    def treatments_player(self):
        self.prolific_id = self.participant.label
        # create the dictionary with the variables
        treatments_dic = {
            'repetition': [],
            'original_trial_num_X': [],
            'condition_number_X': [],
            'condition_name_X': [],
            'lose_value_X': [],
            'gain_value_X': [],
            'gain_condition_X':[],
            'loss_condition_X':[],
            'fixation_time_loss_X': [],
            'fixation_time_gain_X': [],
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
        for repetition in range(2):
            for condition_name in condition_names:
                for losses in losses_lists:
                    for gains in gains_lists:
                        gain = random.choice(gains)
                        lose = random.choice(losses)
                        treatments_dic['original_trial_num_X'].append(count)
                        treatments_dic['condition_name_X'].append(condition_name)
                        treatments_dic['lose_value_X'].append(lose)
                        treatments_dic['gain_value_X'].append(gain)
                        treatments_dic['repetition'].append(repetition)
                        # Define the value conditions
                        if gains == low_gains:
                            treatments_dic['gain_condition_X'].append(1)
                        elif gains == high_gains:
                            treatments_dic['gain_condition_X'].append(2)
                        if losses == high_losses:
                            treatments_dic['loss_condition_X'].append(2)
                        elif losses == low_losses:
                            treatments_dic['loss_condition_X'].append(1)
                        # Define fixation times for gains and losses in the trial
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
                        treatments_dic['fixation_time_gain_X'].append(fixation_time_gain)
                        treatments_dic['fixation_time_loss_X'].append(fixation_time_loss)
                        treatments_dic['condition_number_X'].append(condition_number)
                        count+= 1
        # add 2 more fixations (0, -30 and 0, 40)
        extra_fixations = [[-30, 0], [0, 40]]
        for repetition in range(2):
            for pair in extra_fixations:
                treatments_dic['original_trial_num_X'].append(count)
                treatments_dic['condition_name_X'].append('attention_check')
                treatments_dic['lose_value_X'].append(pair[0])
                treatments_dic['gain_value_X'].append(pair[1])
                treatments_dic['gain_condition_X'].append(0)
                treatments_dic['loss_condition_X'].append(0)
                treatments_dic['fixation_time_loss_X'].append(fixation_duration)
                treatments_dic['fixation_time_gain_X'].append(fixation_duration)
                treatments_dic['condition_number_X'].append(1)
                treatments_dic['repetition'].append(repetition)
                count += 1
        treatments_df = pd.DataFrame(treatments_dic)
        # randomize the table using a randomly generated number (which will be the same for all trials for a specific participant)
        randomized_mixed_repetitions = treatments_df.sample(frac=1, random_state=self.participant.vars['rand_int'])
        # make sure that first repetition is shown on the first half and the second is on the second half
        randomized = randomized_mixed_repetitions.set_index('repetition', drop=False).sort_index()
        # re-index the new table in order so we could present the new randomized table from start to the end
        randomized['new_indexing_X'] = list(range(0, len(randomized)))
        randomized = randomized.set_index(randomized['new_indexing_X'])
        # Check whether the trials are practice to decide whether to show random or
        # ordered rows from the randomized table
        pt = self.practice_trials()
        if pt == 0:
            row_number = self.round_number - 1 - Constants.num_practice_rounds
        elif pt == 1:
            # select random trials from trials with equal and not equal fixations
            if self.round_number % 2 == 0:
                appropriate_trials = randomized[randomized['condition_name_X'] == 'equal']
            else:
                appropriate_trials = randomized[randomized['condition_name_X'] != 'equal']
            row_number = int(appropriate_trials.sample().index[0])

        # write down the data for the participant for each row so we can see it during the data analysis
        self.original_trial_num_X = randomized.loc[row_number, 'original_trial_num_X']
        self.lose_value_X = randomized.loc[row_number, 'lose_value_X']
        self.gain_value_X = randomized.loc[row_number, 'gain_value_X']
        self.condition_name_X = randomized.loc[row_number, 'condition_name_X']
        self.row_number = row_number
        self.gain_condition_X = randomized.loc[row_number, 'gain_condition_X']
        self.loss_condition_X = randomized.loc[row_number, 'loss_condition_X']
        self.fixation_time_loss_X = randomized.loc[row_number, 'fixation_time_loss_X']
        self.fixation_time_gain_X = randomized.loc[row_number, 'fixation_time_gain_X']
        self.condition_number_X = randomized.loc[row_number, 'condition_number_X']
        self.repetition = randomized.loc[row_number, 'repetition']
        return randomized
    def practice_trials(self):
        # this function defines whether these trials are training or test
        if self.round_number > Constants.num_practice_rounds:
            self.practice_trial = 0
            return 0
        else:
            self.practice_trial = 1
            return 1