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
    num_trial_rounds = 44
    num_practice_rounds = 3
    num_rounds = num_trial_rounds + num_practice_rounds


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # variables for Questionnaire
    QT1 = models.IntegerField(label=' I plan tasks carefully.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT2 = models.IntegerField(label=' I do things without thinking.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT3 = models.IntegerField(label=' I make-up my mind quickly.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT4 = models.IntegerField(label=' I am happy-go-lucky.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT5 = models.IntegerField(label=' I don’t “pay attention.”',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT6 = models.IntegerField(label=' I have “racing” thoughts.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT7 = models.IntegerField(label=' I plan trips well ahead of time.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT8 = models.IntegerField(label=' I am self controlled.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT9 = models.IntegerField(label=' I concentrate easily.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT10 = models.IntegerField(label=' I save regularly.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT11 = models.IntegerField(label=' I “squirm” at plays or lectures.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT12 = models.IntegerField(label=' I am a careful thinker.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT13 = models.IntegerField(label=' I plan for job security.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT14 = models.IntegerField(label=' I say things without thinking.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT15 = models.IntegerField(label=' I like to think about complex problems.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT16 = models.IntegerField(label=' I change jobs.', choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                                                 [4, 'Almost Always/Always']],
                               widget=widgets.RadioSelectHorizontal)
    QT17 = models.IntegerField(label=' I act “on impulse.”',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT18 = models.IntegerField(label=' I get easily bored when solving thought problems.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT19 = models.IntegerField(label=' I act on the spur of the moment.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT20 = models.IntegerField(label=' I am a steady thinker.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT21 = models.IntegerField(label=' I change residences.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT22 = models.IntegerField(label=' I buy things on impulse.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT23 = models.IntegerField(label=' I can only think about one thing at a time.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT24 = models.IntegerField(label=' I change hobbies.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT25 = models.IntegerField(label=' I spend or charge more than I earn.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT26 = models.IntegerField(label=' I often have extraneous thoughts when thinking.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT27 = models.IntegerField(label=' I am more interested in the present than the future.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT28 = models.IntegerField(label=' I am restless at the theater or lectures.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT29 = models.IntegerField(label=' I like puzzles.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT30 = models.IntegerField(label=' I am future oriented.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT_check = models.IntegerField(label='Please indicate "Often" in this question.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    # demographic questions
    consent = models.IntegerField(choices=[
        [1, 'I agree to the conditions and want to participate in the study.'],
        [2, 'I do not agree to participate.']
    ], widget=widgets.RadioSelect)
    demography_age = models.IntegerField(label="Your age", max=99, min=5)
    demography_country = models.StringField(label="What country do you live in now?", blank=True)
    demography_gender = models.IntegerField(label="Which gender do you identify most with?", choices=[
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Other'],
        [4, 'Prefer not to say']
    ])
    demography_nationality = models.StringField(label= "Nationality", blank=True)
    q_statistics = models.IntegerField(label = "Have you ever been instructed in Statistics and/or Calculus?", choices = [
        [1, 'Yes'],
        [2, 'No'],
        [3, 'Do not know']
    ], widget = widgets.RadioSelect)
    q_study = models.StringField(label = "What did you study?", blank=True)
    q_purpose = models.LongStringField(label = "What do you think it was the purpose of this study?", blank=True)
    q_strategy_binary = models.IntegerField(label = "Did you use a specific strategy?", choices = [
        [1, "Yes"],
        [2, "No"]
    ], widget = widgets.RadioSelect)
    strategy = models.LongStringField(label="Could you explain how did you decide to accept or reject the gambles in each trial? (max - 250 characters)", max_length=250, blank=True)
    q_other_exp = models.IntegerField(label = "Have you ever participated in an incentivized economic experiment like this one?", choices = [
        [1, "Yes"],
        [2, "No"],
        [3, "Do not know"]
    ], widget=widgets.RadioSelect)
    q_improve = models.LongStringField(label = "Please help us improve our previous studies. Was there something that was not clear in the instructions? (max - 250 characters)", max_length=250, blank=True)
    q_own_corona_concern = models.IntegerField(label = "Are you concerned about your own health due to the novel coronavirus?", choices = [
        [1, "Very concerned"],
        [2, "Concerned"],
        [3, "Neither concerned nor unconcerned"],
        [4, "Unconcerned"],
        [5, "Very Unconcerned"]
    ], widget=widgets.RadioSelect)
    q_relat_corona_concern = models.IntegerField(label = "Are you concerned about the health of your family members due to the novel coronavirus?", choices = [
        [1, "Very concerned"],
        [2, "Concerned"],
        [3, "Neither concerned nor unconcerned"],
        [4, "Unconcerned"],
        [5, "Very Unconcerned"]
    ], widget=widgets.RadioSelect)
    q_own_corona_likelihood = models.IntegerField(label = "How likely do you think it is, that you will get infected by Covid-19 and experience serious health problems before the end of 2021?", choices = [
        [1, "Very Unlikely"],
        [2, "Unlikely"],
        [3, "Neither unlikely nor likely"],
        [4, "Likely"],
        [5, "Very Likely"]
    ], widget=widgets.RadioSelect)
    q_relat_corona_likelihood = models.IntegerField(label = "How likely do you think it is, that someone you know will die from Covid-19 before the end of 2021?", choices = [
        [1, "Very Unlikely"],
        [2, "Unlikely"],
        [3, "Neither unlikely nor likely"],
        [4, "Likely"],
        [5, "Very Likely"]
    ], widget=widgets.RadioSelect)
    # anwers to the questions checking the understanding of instructions
    q1 = models.StringField(label="How many decisions are you going to make (without counting the practice trials)?", blank = True)
    q2 = models.StringField(label = "How many outcomes will be selected for payment?", blank = True)
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
    # Condition numbers: 1 - equal, 2 - gains are longer, 3 - gains are super longer, 4 - losses are longer, 5 - losses are super longer
    condition_number = models.IntegerField()
    # number of a trial in a non-randomised data-frame
    original_trial_num = models.IntegerField()
    # 1 = accepted, 0 = rejected, -1 = no decision was made
    decision = models.IntegerField(blank=True)
    # smaller,equal,larger
    condition_name = models.StringField()
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
    # each condition is repeated 2 times, so the repetition variable tracks this
    repetition = models.IntegerField()
    def lottery(self):
        random.seed(self.in_round(1).rand_int)
        winning_round = random.choice(range(1, Constants.num_rounds+1))
        winning_value_gain = self.in_round(winning_round).gain_value
        winning_value_loss = self.in_round(winning_round).lose_value
        decision_in_winning_round = self.in_round(winning_round).decision
        if decision_in_winning_round == 1:
            random.seed(self.in_round(1).rand_int)
            final_value = random.choice([winning_value_loss, winning_value_gain])
        elif decision_in_winning_round == -1:
            final_value = winning_value_loss
        else:
            final_value = 0
        final_value_and_lottery = [final_value, winning_round, decision_in_winning_round]
        return final_value_and_lottery



    def treatments_player(self):
        self.prolific_id = self.participant.label
        # create the dictionary with the variables
        treatments_dic = {
            'repetition': [],
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
        for repetition in range(2):
            for condition_name in condition_names:
                for losses in losses_lists:
                    for gains in gains_lists:
                        gain = random.choice(gains)
                        lose = random.choice(losses)
                        treatments_dic['original_trial_num'].append(count)
                        treatments_dic['condition_name'].append(condition_name)
                        treatments_dic['lose_value'].append(lose)
                        treatments_dic['gain_value'].append(gain)
                        treatments_dic['repetition'].append(repetition)
                        # Define the value conditions
                        if gains == low_gains:
                            treatments_dic['gain_condition'].append('low_gains')
                        elif gains == high_gains:
                            treatments_dic['gain_condition'].append('high_gains')
                        if losses == high_losses:
                            treatments_dic['loss_condition'].append('high_losses')
                        elif losses == low_losses:
                            treatments_dic['loss_condition'].append('low_losses')
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
                        treatments_dic['fixation_time_gain'].append(fixation_time_gain)
                        treatments_dic['fixation_time_loss'].append(fixation_time_loss)
                        treatments_dic['condition_number'].append(condition_number)
                        count+= 1
        # add 2 more fixations (0, -30 and 0, 40)
        extra_fixations = [[-30, 0], [0, 40]]
        for repetition in range(2):
            for pair in extra_fixations:
                treatments_dic['original_trial_num'].append(count)
                treatments_dic['condition_name'].append('attention_check')
                treatments_dic['lose_value'].append(pair[0])
                treatments_dic['gain_value'].append(pair[1])
                treatments_dic['gain_condition'].append(None)
                treatments_dic['loss_condition'].append(None)
                treatments_dic['fixation_time_loss'].append(fixation_duration)
                treatments_dic['fixation_time_gain'].append(fixation_duration)
                treatments_dic['condition_number'].append(99)
                treatments_dic['repetition'].append(repetition)
                count += 1
        treatments_df = pd.DataFrame(treatments_dic)
        # randomize the table using a randomly generated number (which will be the same for all trials for a specific participant)
        randomized_mixed_repetitions = treatments_df.sample(frac=1, random_state=self.in_round(1).rand_int)
        # make sure that first repetition is shown on the first half and the second is on the second half
        randomized = randomized_mixed_repetitions.set_index('repetition', drop=False).sort_index()
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
            if self.round_number % 2 == 0:
                appropriate_trials = randomized[randomized['condition_name'] == 'equal']
            else:
                appropriate_trials = randomized[randomized['condition_name'] != 'equal']
            row_number = int(appropriate_trials.sample().index[0])

        # write down the data for the participant for each row so we can see it during the data analysis
        self.original_trial_num = randomized.loc[row_number, 'original_trial_num']
        self.lose_value = randomized.loc[row_number, 'lose_value']
        self.gain_value = randomized.loc[row_number, 'gain_value']
        self.condition_name = randomized.loc[row_number, 'condition_name']
        self.row_number = row_number
        self.gain_condition = randomized.loc[row_number, 'gain_condition']
        self.loss_condition = randomized.loc[row_number, 'loss_condition']
        self.fixation_time_loss = randomized.loc[row_number, 'fixation_time_loss']
        self.fixation_time_gain = randomized.loc[row_number, 'fixation_time_gain']
        self.condition_number = randomized.loc[row_number, 'condition_number']
        self.repetition = randomized.loc[row_number, 'repetition']
        self.session.vars['TEST'] = 20
        return randomized
    def practice_trials(self):
        # this function defines whether these trials are training or test
        if self.round_number > Constants.num_practice_rounds:
            self.practice_trial = 0
            return 0
        else:
            self.practice_trial = 1
            return 1