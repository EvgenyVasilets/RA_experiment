from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent']
    def is_displayed(self):
        return self.round_number == 1

class ConsentIfFalse(Page):
    def is_displayed(self):
        return (self.player.in_round(1).consent == 2) and (self.round_number == 1)

class Instructions(Page):
    form_model = 'player'
    form_fields = ['rand_int', 'q1', 'q2', 'q3', 'q4']
    def is_displayed(self):
        return (self.round_number == 1) and (self.player.in_round(1).consent == 1)
    def error_message(self, values):
        if (values['q1'] != "44") or (values['q2'] != "1") or (values['q3'] != 1) or (values['q4'] != 2) and (self.round_number == 1):
            return 'Some of your answers contain an error'

class Instructions2(Page):
    def is_displayed(self):
            return (self.round_number == Constants.num_practice_rounds + 1) and (self.player.in_round(1).consent == 1)

class Attention(Page):
    def is_displayed(self):
        return (self.round_number == 1) and (self.player.in_round(1).consent == 1)
            
class Trial_and_decision(Page):
    form_model = 'player'
    form_fields = ['decision', 'decision_time_ms', 'fixation_number_gains', 'fixation_number_losses']
    def vars_for_template(self):
        randomized_table = self.player.treatments_player()
        row_for_the_trial = randomized_table.iloc[self.player.row_number]
        return dict(
            original_trial_num = row_for_the_trial['original_trial_num'],
            fixation_time_gain = row_for_the_trial['fixation_time_gain'],
            fixation_time_loss = row_for_the_trial['fixation_time_loss'],
            lose_value = row_for_the_trial['lose_value'],
            gain_value = row_for_the_trial['gain_value']
        )
    def is_displayed(self):
        return self.player.in_round(1).consent == 1

class Feedback(Page):
    def vars_for_template(self):
        return dict(
            decision = self.player.decision,
        )
    def is_displayed(self):
        return self.player.in_round(1).consent == 1

class Confidence(Page):
    form_model = 'player'
    form_fields = ['confidence']
    def is_displayed(self):
        decision = self.player.decision
        return (decision != -1) and (self.player.in_round(1).consent == 1)

class ResultsWaitPage(WaitPage):
    pass

class Middle_page(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_practice_rounds + (Constants.num_trial_rounds/2)) and (self.player.in_round(1).consent == 1)

class Demographics(Page):
    form_model='player'
    form_fields = ['demography_country', 'demography_age', 'demography_gender', 'demography_nationality', 'q_statistics', 'q_study', 'q_purpose', 'q_strategy_binary', 'strategy', 'q_other_exp', 'q_improve', 'q_own_corona_concern', 'q_relat_corona_concern', 'q_own_corona_likelihood', 'q_relat_corona_likelihood']
    def is_displayed(self):
        return (self.round_number == Constants.num_rounds) and (self.player.in_round(1).consent == 1)
    def error_message(self, values):
        # Write a message if some of the inputs are empty
        if (not values['q_study']) or (not values['demography_nationality']) or (not values['demography_country']):
            return "Please, fill the Nationality, Country and Subject fields"
        countries = ["My country is not listed", "Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua & Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia & Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central Arfrican Republic","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauro","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre & Miquelon","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","St Kitts & Nevis","St Lucia","St Vincent","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Turks & Caicos","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
        countries_lower = [country.lower() for country in countries]
        if not values['demography_country'].lower() in countries_lower:
            return "Please, choose the country name from the suggested list. If your country is not in a list, type 'My country is not listed'."
        if not values['demography_nationality'].lower() in countries_lower:
            return "Please, choose the nationality from the suggested list. If your nationality is not in a list, type 'My country is not listed'."
        subjects = ["Other", "Accounting and Finance", "Agriculture & Forestry", "Anatomy & Physiology", "Anthropology", "Archaeology", "Architecture", "Area Studies", "Art & Design", "Astronomy", "Biological Sciences", "Built Environment", "Business & Management Studies", "Chemistry", "Classics & Ancient History", "Communication and Media Studies", "Computer Science and Information Systems", "Dentistry", "Development Studies", "Earth and Marine Sciences", "Economics and Econometrics", "Education and Training", "Engineering - Aeronautical", "Engineering - Chemical", "Engineering - Civil and Structural", "Engineering - Electrical and Electronic", "Engineering - General", "Engineering - Manufacturing & Production", "Engineering - Mechanical", "Engineering - Mineral & Mining", "Engineering - Petroleum", "Engineering Management", "English Language and Literature", "Environmental Studies", "Ethnicity, Gender and Diversity", "Finance", "Geography", "Geology", "Geophysics", "Hospitality & Leisure Management", "Human Resources Management", "International Relations/Studies/Affairs", "Journalism", "Law and Legal Studies", "Library & Information Management", "Linguistics", "Logistics / Supply Chain Management", "Marketing", "Materials Sciences", "Mathematics", "Medicine", "Medicine Related Studies", "Modern Languages", "Nursing", "Performing Arts", "Pharmacology", "Pharmacy & Pharmacology", "Philosophy", "Physics & Astronomy", "Politics", "Psychology", "Public Policy", "Sociology", "Sports-related Courses", "Statistics and Operational Research", "Theology, Divinity & Religious Studies", "Urban Planning", "Veterinary Science", "Zoology"]
        subjects_lower = [subject.lower() for subject in subjects]
        if not values['q_study'].lower() in subjects_lower:
            return "Please, choose the subject name from the suggested list. If your subject is not in a list, type 'Other'."


class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['QT1', 'QT2', 'QT3', 'QT4', 'QT5', 'QT6', 'QT7', 'QT8', 'QT9', 'QT10', 'QT11', 'QT12', 'QT13', 'QT14', 'QT15', 'QT16', 'QT17', 'QT18', 'QT19', 'QT20', 'QT21', 'QT22', 'QT23', 'QT24', 'QT25', 'QT26', 'QT27', 'QT28', 'QT29', 'QT30', 'QT_check']
    def is_displayed(self):
        return (self.round_number == Constants.num_rounds) and (self.player.in_round(1).consent == 1)

class Results(Page):
    form_model = 'player'
    form_fields = ['lottery_result']
    def js_vars(self):
        self.session.vars['TEST'] = 12
        lottery_result, round_number_lottery, decision_in_winning_round = self.player.lottery()
        return dict(
            lottery_result = lottery_result,
            round_number_lottery = round_number_lottery,
            decision_in_winning_round = decision_in_winning_round
        )
    def is_displayed(self):
        return (self.round_number == Constants.num_rounds) and (self.player.in_round(1).consent == 1)


page_sequence = [ConsentForm, ConsentIfFalse, Instructions, Instructions2, Attention, Trial_and_decision, Feedback, Confidence, Middle_page, Demographics, Questionnaire,  Results]
# real page sequence
# page_sequence = [ConsentForm, ConsentIfFalse, Instructions, Instructions2, Attention, Trial_and_decision, Feedback, Confidence, Middle_page, Demographics, Questionnaire,  Results]