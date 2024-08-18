from otree.api import *


doc = """
Radio buttons in various layouts, looping over anp choices
"""


class C(BaseConstants):
    NAME_IN_URL = 'anp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    page_pass_time = models.FloatField()
    #Skala likert
    inf_avb = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5,4,3,2,1,-2,-3,-4,-5],
    )
    inf_nmb = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    inf_prc = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    avb_nmb = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    avb_prc = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    nmb_prc = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    Halal_lbl_logo = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    Halal_lbl_clhll = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    Halal_lbl_hlloff = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    Halal_logo_clhll = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    Halal_logo_hlloff = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    Halal_clhll_hlloff = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],
    )
    ##Sub-kriteria Harga
    Harga_A1_A2 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],)
    Harga_A1_A3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],)
    Harga_A2_A3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5],)

    #Sub-kriteria HalalProcess
    HalalProses_B1_B2 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B1_B3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B1_B4 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B1_B5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B2_B3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B2_B4 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B2_B5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B3_B4 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )
    HalalProses_B3_B5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1,-2, -3, -4, -5], )
    HalalProses_B4_B5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[5, 4, 3, 2, 1, -2, -3, -4, -5], )

class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_pass_time = time.time() + 15

# PAGES
class kriteria(Page):
    form_model = 'player'
    form_fields = ['inf_avb','inf_nmb','inf_prc','avb_nmb','avb_prc','nmb_prc']

    @staticmethod
    def error_message(player: Player, values):
        import time

        if time.time() < player.page_pass_time:
            return "Tunggu hingga lima belas detik."

class sub_kriteria1(Page):
    form_model = 'player'
    form_fields = ['Halal_lbl_logo','Halal_lbl_clhll','Halal_lbl_hlloff',
                   'Halal_logo_clhll','Halal_logo_hlloff','Halal_clhll_hlloff']

    @staticmethod
    def error_message(player: Player, values):
        import time

        if time.time() < player.page_pass_time:
            return "Tunggu hingga lima belas detik."

class sub_kriteria2(Page):
    form_model = 'player'
    form_fields = ['Harga_A1_A2','Harga_A1_A3','Harga_A2_A3']

    @staticmethod
    def error_message(player: Player, values):
        import time

        if time.time() < player.page_pass_time:
            return "Tunggu hingga lima belas detik."

class sub_kriteria3(Page):
    form_model = 'player'
    form_fields = ['HalalProses_B1_B2','HalalProses_B1_B3','HalalProses_B1_B4',
                   'HalalProses_B1_B5','HalalProses_B2_B3','HalalProses_B2_B4',
                   'HalalProses_B2_B5','HalalProses_B3_B4','HalalProses_B3_B5',
                   'HalalProses_B4_B5']

    @staticmethod
    def error_message(player: Player, values):
        import time

        if time.time() < player.page_pass_time:
            return "Tunggu hingga lima belas detik."

page_sequence = [MyPage,kriteria,sub_kriteria1,sub_kriteria2,sub_kriteria3]
