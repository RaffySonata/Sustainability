from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.IntegerField(label="Berapa usia Anda?")
    gender = models.StringField(
        choices=['Laki-laki', 'Perempuan', 'Lainnya'],
        label="Apa jenis kelamin Anda?",
        widget=widgets.RadioSelect
    )
    education = models.StringField(
        choices=[
            'Sekolah Dasar',
            'Sekolah Menengah Pertama',
            'Sekolah Menengah Atas',
            'Diploma',
            'Sarjana',
            'Magister',
            'Doktoral'
        ],
        label="Apa tingkat pendidikan terakhir Anda?",
        widget=widgets.RadioSelect
    )

class Instruction1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict()

class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education']

page_sequence = [Instruction1]



