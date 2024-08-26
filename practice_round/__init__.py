from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'practice_round'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1  # Only one round for practice

    # Appliance context for the practice round
    APPLIANCES_IMAGES = ['K_A.jpeg', 'K_B.jpeg']
    APPLIANCES_NAMES = ['Kompor Listrik A', 'Kompor Listrik B']
    APPLIANCES_DESCRIPTIONS = [
        'Kompor listrik seharga Rp7 juta (Bentuk A sesuai gambar) yang memiliki 90% keawetan untuk penggunaan reguler sampai dengan tahun ke-5',
        'Kompor listrik seharga Rp5 juta (Bentuk B sesuai gambar) yang memiliki 85% keawetan untuk penggunaan reguler sampai dengan tahun ke-5.'
    ]
    APPLIANCES_PRICES = [7000000, 5000000]
    APPLIANCES_RELIABILITIES = [0.90, 0.85]
    APPLIANCES_RISK_COST = 1000000  # Risk cost for appliances
    wait_seconds = 10

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    chosen_product = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelect)
    current_image_A = models.StringField()
    current_image_B = models.StringField()
    current_price_A = models.IntegerField()
    current_price_B = models.IntegerField()
    risk_simulated = models.BooleanField(initial=False)
    risk_penalty = models.FloatField(initial=0)
    income = models.FloatField()
    endowment = models.IntegerField()
    final_payoff_stored = models.FloatField()

def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        player.current_image_A = C.APPLIANCES_IMAGES[0]
        player.current_image_B = C.APPLIANCES_IMAGES[1]
        player.current_price_A = C.APPLIANCES_PRICES[0]
        player.current_price_B = C.APPLIANCES_PRICES[1]
        player.endowment = 20000000  # Set a sample endowment

class Choice(Page):
    form_model = 'player'
    form_fields = ['chosen_product']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            image_A='image_rating/{}'.format(player.current_image_A),
            image_B='image_rating/{}'.format(player.current_image_B),
            name_A=C.APPLIANCES_NAMES[0],
            name_B=C.APPLIANCES_NAMES[1],
            desc_A=C.APPLIANCES_DESCRIPTIONS[0],
            desc_B=C.APPLIANCES_DESCRIPTIONS[1],
            price_A='{:,}'.format(player.current_price_A).replace(',', '.'),
            price_B='{:,}'.format(player.current_price_B).replace(',', '.'),
            additional_info=f"Jika produk yang Anda pilih rusak/bermasalah dalam jangka waktu 5 tahun, maka Anda harus mengeluarkan biaya perbaikan sebesar Rp{C.APPLIANCES_RISK_COST:,}.",
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Determine the chosen product and simulate risk
        if player.chosen_product == 'A':
            chosen_price = player.current_price_A
            reliability = C.APPLIANCES_RELIABILITIES[0]
        else:
            chosen_price = player.current_price_B
            reliability = C.APPLIANCES_RELIABILITIES[1]

        # Simulate risk
        if random.random() > reliability:
            player.risk_simulated = True
            player.risk_penalty = C.APPLIANCES_RISK_COST
        else:
            player.risk_simulated = False
            player.risk_penalty = 0

        # Calculate income
        player.income = player.endowment - chosen_price - player.risk_penalty
        player.final_payoff_stored = player.income

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            income='{:,}'.format(round(player.income)).replace(',', '.'),
            risk_penalty='{:,}'.format(round(player.risk_penalty)).replace(',', '.'),
        )

page_sequence = [Choice, Results]
