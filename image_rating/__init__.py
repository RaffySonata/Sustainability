from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'image_rating'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 16  # Four cycles of four rounds each

    # Car images for round 1
    CAR_IMAGES = ['M_A.jpeg', 'M_B.jpeg', 'M_C1.jpeg', 'M_C2.jpeg']
    CAR_NAMES = ['Cherry Omoda E5 (A)', 'Wuling Bingo (B)', 'Toyota Corolla Altis V AT (C1)', 'Toyota Yaris (C2)']
    CAR_DESCRIPTIONS = [
        'Ini adalah mobil Listrik Chery Omoda E5 dengan spesifikasi baterai LFP (Lithium Ferrophospate) berkapasitas 61 kWh, daya tempuh 430 km, bertenaga 201 HP, memiliki torsi 340 Nm, dan top speed 172 km/jam yang memiliki daya tahan 90% untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Ini adalah mobil Listrik Wuling Binguo EV Premium Range dengan spesifikasi baterai LFP (Lithium Ferrophospate) berkapasitas 37,9 kWh, daya tempuh 410 km, bertenaga 67 HP, memiliki torsi 150 Nm, dan top speed 120 km/jam yang memiliki daya tahan 85% untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Ini adalah mobil Toyota Corolla Altis V AT berbahan bakar bensin dengan spesifikasi mesin 1798 cc, bertenaga 138 HP, memiliki torsi 172 Nm, dan top speed 200 km/jam yang memiliki daya tahan 95% untuk penggunaan reguler sampai dengan tahun ke-5',
        'Ini adalah mobil Toyota Yaris mesin 1496 cc, tenaga 106 HP, torsi 140 Nm, bensin, top speed 200 km/jam yang memiliki daya tahan 80% untuk penggunaan reguler sampai dengan tahun ke-5'
    ]
    CAR_PRICES = [500000000, 400000000, 600000000, 350000000]
    CAR_RELIABILITIES = [0.90, 0.85, 0.95, 0.80]
    CAR_RISK_COST = 50000000

    # Appliances images for round 2
    APPLIANCES_IMAGES = ['K_A.jpeg', 'K_B.jpeg', 'K_C1.jpeg', 'K_C2.jpeg']
    APPLIANCES_NAMES = ['Kompor Listrik (A)', 'Kompor Listrik (B)', 'Kompor Gas (C1)', 'Kompor Gas (C2)']
    APPLIANCES_DESCRIPTIONS = [
        'Kompor listrik seharga Rp7 juta yang memiliki 90% keawetan untuk penggunaan reguler sampai dengan tahun ke-5',
        'Kompor listrik seharga Rp5 juta yang memiliki 85% keawetan untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Kompor gas seharga Rp8 juta yang memiliki 95% keawetan untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Kompor gas seharga Rp4 juta yang memiliki 80% keawetan untuk penggunaan reguler sampai dengan tahun ke-5.'
    ]
    APPLIANCES_PRICES = [7000000, 5000000, 8000000, 4000000]
    APPLIANCES_RELIABILITIES = [0.90, 0.85, 0.95, 0.80]
    APPLIANCES_RISK_COST = 1000000

    # Electricity images for round 3
    ELECTRICITY_IMAGES = ['L_A.jpeg', 'L_B.jpeg', 'L_C1.jpeg', 'L_C2.jpeg']
    ELECTRICITY_NAMES = ['Panel Surya (A)', 'Panel Surya (B)', 'PLN (C1)', 'PLN (C2)']
    ELECTRICITY_DESCRIPTIONS = [
        'Listrik rumah kombinasi dari panel surya (PLTS Rumahan) yang mampu menghasilkan daya maksimum +/-500 Watt plus Listrik PLN 900 Watt dengan biaya total Rp12 juta yang memiliki 90% keandalan untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Listrik rumah kombinasi dari panel surya (PLTS Rumahan) yang mampu menghasilkan daya maksimum +/-300 Watt plus Listrik PLN 900 Watt dengan biaya total Rp10 juta yang memiliki 85% keandalan untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Listrik rumah dari jaringan PLN (berasal dari PLTU berbahan baku batu bara) untuk daya maksimum 2200 Watt dengan biaya (instalasi dan tagihan) Rp15 juta yang memiliki keandalan 95% untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Listrik rumah dari jaringan PLN (berasal dari PLTU berbahan baku batu bara) untuk daya maksimum 1300 Watt dengan biaya Rp8 juta yang memiliki keandalan 80% untuk penggunaan reguler sampai dengan tahun ke-5.'
    ]
    ELECTRICITY_PRICES = [12000000, 10000000, 15000000, 8000000]
    ELECTRICITY_RELIABILITIES = [0.90, 0.85, 0.95, 0.80]
    ELECTRICITY_RISK_COST = 2000000

    # Fuel images for round 4
    FUEL_IMAGES = ['BBM_A.jpeg', 'BBM_B.jpeg', 'BBM_C1.jpeg', 'BBM_C2.jpeg']
    FUEL_NAMES = ['Pertamax Green (A)', 'Pertamax (B)', 'Pertamax Turbo (C1)', 'Pertalite (C2)']
    FUEL_DESCRIPTIONS = [
        'Kebutuhan full tank BBM mobil Anda sebanyak 50 liter dengan biaya Rp700 ribu (Pertamax Green RON 95) yang membuat mobil Anda memiliki 90% keawetan mesin untuk penggunaan reguler sampai dengan tahun ke-5',
        'Kebutuhan full tank BBM mobil Anda sebanyak 50 liter dengan biaya Rp650 ribu (Pertamax RON 92) yang membuat mobil Anda memiliki 85% keawetan mesin untuk penggunaan reguler sampai dengan tahun ke-5',
        'Kebutuhan full tank BBM mobil Anda sebanyak 50 liter dengan biaya Rp725 ribu (Pertamax Turbo RON 98) yang membuat mobil Anda memiliki 95% keawetan mesin untuk penggunaan reguler sampai dengan tahun ke-5.',
        'Kebutuhan full tank BBM mobil Anda sebanyak 50 liter dengan biaya Rp500 ribu (Pertalite RON 90) yang membuat mobil Anda memiliki 80% keawetan mesin untuk penggunaan reguler sampai dengan tahun ke-5.'
    ]
    FUEL_PRICES = [700000, 650000, 725000, 500000]
    FUEL_RELIABILITIES = [0.90, 0.85, 0.95, 0.80]
    FUEL_RISK_COST = 500000

    ENDOWMENT = [700000000, 10000000, 20000000, 1500000]  # Example endowment values
    CAR_CONTEXTS = [
        "Anda tinggal di tempat yang belum ada SPKLU (Stasiun Pengisian Kendaraan Listrik Umum), tetapi sudah ada SPBU bensin yang mencukupi kebutuhan masyarakat setempat. Anda harus menyediakan charger mobil listrik secara mandiri di rumah Anda.",
        "Anda tinggal di tempat dimana belum ada dealer yang menjual dan melayani servis mobil Listrik. Hanya ada dealer dan servis untuk mobil berbahan bakar minyak. Jika terjadi masalah pada mobil listrik Anda, maka Anda harus pergi ke kota lain sejauh 100 km untuk servis.",
        "Hanya ada segelintir orang yang membeli mobil listrik dan susah menemui mobil listrik berlalu-lalang di wilayah Anda tinggal. Kebanyakan memiliki mobil berbahan bakar minyak.",
        "Produksi mobil listrik dan spare part-nya secara umum dilakukan oleh negara lain dengan Tingkat Komponen Dalam Negeri (TKDN) hanya mencapai maksimum 25%. Di sisi lain, TKDN mobil konvensional sudah mencapai minimal 50% yang mencakup perakitan mobil dan produksi spare-part."
    ]
    APPLIANCES_CONTEXTS = [
        "Anda tinggal di tempat yang sering terjadi pemadaman listrik. Hal ini bisa menjadi penyebab kerusakan perangkat rumah tangga yang menggunakan listrik. Di sisi lain, terdapat tiga agen gas di tempat Anda tinggal.",
        "Hanya ada satu toko yang menjual kompor listrik di radius 20 km dari tempat Anda tinggal. Anda harus memesan kompor listrik secara online maupun dari penyedia yang berada jauh (>20 km) di luar tempat Anda tinggal.",
        "Hanya ada segelintir rumah tangga yang menggunakan kompor listrik di daerah Anda tinggal. Kebanyakan memakai kompor gas konvensional.",
        "Kompor listrik yang tersedia di pasaran umumnya diproduksi oleh negara lain (China, Jepang, Korea Selatan, Jerman, dan Amerika). Produsen Indonesia hanya mampu memproduksi dan menjual kompor gas."
    ]
    ELECTRICITY_CONTEXTS = [
        "Hanya ada satu teknisi lokal untuk panel surya di daerah tempat Anda tinggal. Anda harus mengantri sekitar seminggu untuk servis panel surya jika mengalami kerusakan. Di sisi lain, jaringan PLN sudah cukup mumpuni di daerah tempat Anda tinggal.",
        "Hanya ada satu toko yang menjual panel surya di radius 20 km dari tempat Anda tinggal. Anda harus memesan secara online atau mengundang tenaga profesional ke rumah jika Anda ingin memasang panel surya. Di sisi lain, jaringan PLN sudah tersambung sejak lama di tempat Anda tinggal.",
        "Hanya ada segelintir rumah tangga yang menggunakan panel surya untuk memenuhi kebutuhan listrik rumah. Kebanyakan menggunakan listrik dari jaringan PLN secara konvensional.",
        "Komponen dan perakitan panel surya hanya dilakukan oleh negara lain (China, Jepang, Korea Selatan, Jerman, dan Amerika). Tidak ada produsen Indonesia yang mampu memproduksi panel surya."
    ]
    FUEL_CONTEXTS = [
        "Anda tinggal di tempat yang memiliki 4 SPBU yang terjangkau di sekitar Anda. Namun hanya 1 SPBU yang menyediakan Pertamax Green RON 95. Jenis BBM lain tersedia di keempat SPBU tersebut.",
        "SPBU di kabupaten tempat Anda tinggal tidak memiliki banyak stok untuk Pertamax Green RON 95 dan seringkali kosong. Namun tidak dengan jenis BBM lain (Pertalite RON 90, Pertamax RON 92, maupun Pertamax Turbo RON 98) yang selalu memiliki stok cukup setiap harinya.",
        "Hanya ada segelintir orang yang membeli Pertamax Green RON 95. Kebanyakan menggunakan BBM konvensional (Pertalite, Pertamax, Pertamax Turbo, Biosolar, Dexlite, dan Pertadex) untuk kendaraan bermotornya.",
        "Bahan utama untuk campuran di Pertamax Green RON 95 berasal dari kelapa sawit yang banyak ditanam di Pulau Kalimantan, Sumatera, dan Sulawesi. "
    ]
    wait_seconds = 10

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    session = subsession.session
    session.params = {}
    for p in subsession.get_players():
        # initialize an empty dict to store how much they made in each app
        p.participant.app_payoffs = {}
    for p in subsession.get_players():
        p.participant.app_row = {}
    for p in subsession.get_players():
        p.participant.selected_round = {}
    for p in subsession.get_players():
        if 'selected_round' not in p.participant.vars:
            p.participant.vars['selected_round'] = {}
    cycle = (subsession.round_number - 1) // 4
    round_in_cycle = (subsession.round_number - 1) % 4

    for player in subsession.get_players():
        if round_in_cycle == 0:
            player.current_image_A = C.CAR_IMAGES[0]
            player.current_image_B = C.CAR_IMAGES[1]
            player.current_price_A = C.CAR_PRICES[0]
            player.current_price_B = C.CAR_PRICES[1]
            player.endowment = C.ENDOWMENT[0]
        elif round_in_cycle == 1:
            player.current_image_A = C.APPLIANCES_IMAGES[0]
            player.current_image_B = C.APPLIANCES_IMAGES[1]
            player.current_price_A = C.APPLIANCES_PRICES[0]
            player.current_price_B = C.APPLIANCES_PRICES[1]
            player.endowment = C.ENDOWMENT[1]
        elif round_in_cycle == 2:
            player.current_image_A = C.ELECTRICITY_IMAGES[0]
            player.current_image_B = C.ELECTRICITY_IMAGES[1]
            player.current_price_A = C.ELECTRICITY_PRICES[0]
            player.current_price_B = C.ELECTRICITY_PRICES[1]
            player.endowment = C.ENDOWMENT[2]
        elif round_in_cycle == 3:
            player.current_image_A = C.FUEL_IMAGES[0]
            player.current_image_B = C.FUEL_IMAGES[1]
            player.current_price_A = C.FUEL_PRICES[0]
            player.current_price_B = C.FUEL_PRICES[1]
            player.endowment = C.ENDOWMENT[3]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    chosen_product = models.StringField(choices=['A', 'B'], widget=widgets.RadioSelect)
    current_image_A = models.StringField()
    current_image_B = models.StringField()
    winner_image_choice1 = models.StringField()
    winner_image_choice2 = models.StringField()
    winner_price_choice1 = models.CurrencyField()
    winner_price_choice2 = models.CurrencyField()
    endowment = models.IntegerField()
    endowment_s = models.StringField()
    income = models.FloatField()
    potential_payoff  = models.FloatField()
    winner_choice = models.IntegerField()  # 0 if A won, 1 if B won
    current_price_A = models.IntegerField()
    current_price_B = models.IntegerField()
    risk_simulated = models.BooleanField(initial=False)
    risk_penalty = models.FloatField(initial=0)
    choice_round = models.IntegerField()
    choice1_winner = models.StringField()
    choice2_winner = models.StringField()
    choice3_winner = models.StringField()
    choice1_price = models.FloatField()
    choice2_price = models.FloatField()
    choice3_price = models.FloatField()
    random_round = models.IntegerField()
    context = models.IntegerField()
    app_payoff = models.FloatField()
    final_payoff = models.FloatField()

def get_current_context(player):
    round_in_cycle = (player.round_number - 1) % 4
    if round_in_cycle == 0:
        return C.CAR_IMAGES, C.CAR_NAMES, C.CAR_DESCRIPTIONS, C.CAR_PRICES, C.CAR_RELIABILITIES, C.CAR_RISK_COST, C.CAR_CONTEXTS
    elif round_in_cycle == 1:
        return C.APPLIANCES_IMAGES, C.APPLIANCES_NAMES, C.APPLIANCES_DESCRIPTIONS, C.APPLIANCES_PRICES, C.APPLIANCES_RELIABILITIES, C.APPLIANCES_RISK_COST, C.APPLIANCES_CONTEXTS
    elif round_in_cycle == 2:
        return C.ELECTRICITY_IMAGES, C.ELECTRICITY_NAMES, C.ELECTRICITY_DESCRIPTIONS, C.ELECTRICITY_PRICES, C.ELECTRICITY_RELIABILITIES, C.ELECTRICITY_RISK_COST, C.ELECTRICITY_CONTEXTS
    elif round_in_cycle == 3:
        return C.FUEL_IMAGES, C.FUEL_NAMES, C.FUEL_DESCRIPTIONS, C.FUEL_PRICES, C.FUEL_RELIABILITIES, C.FUEL_RISK_COST, C.FUEL_CONTEXTS


class Choice1(Page):
    form_model = 'player'
    form_fields = ['chosen_product']

    @staticmethod
    def vars_for_template(player: Player):
        cycle = (player.round_number - 1) // 4
        images, names, descriptions, prices, reliabilities, risk_cost, contexts = get_current_context(player)
        context = contexts[cycle]
        player.context = cycle + 1
        additional_info = additional_info = f"Jika produk yang Anda pilih rusak/bermasalah dalam jangka waktu 5 tahun, maka Anda harus mengeluarkan biaya perbaikan sebesar Rp{risk_cost:,}."


        endowment = player.endowment / 1000000
        player.endowment_s = '{:,}'.format(round(endowment)).replace(',', '.')

        return dict(
            context=context,
            additional_info=additional_info,
            image_A='image_rating/{}'.format(player.current_image_A),
            image_B='image_rating/{}'.format(player.current_image_B),
            name_A=names[images.index(player.current_image_A)],
            name_B=names[images.index(player.current_image_B)],
            desc_A=descriptions[images.index(player.current_image_A)],
            desc_B=descriptions[images.index(player.current_image_B)],
            price_A='{:,}'.format(round(player.current_price_A)).replace(',', '.'),
            price_B='{:,}'.format(round(player.current_price_B)).replace(',', '.'),
            reliability_A=reliabilities[images.index(player.current_image_A)] * 100,
            reliability_B=reliabilities[images.index(player.current_image_B)] * 100,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        images, names, descriptions, prices, reliabilities, risk_cost, contexts = get_current_context(player)

        if player.chosen_product == 'A':
            player.winner_image_choice1 = player.current_image_A
            player.winner_price_choice1 = player.current_price_A
            player.winner_choice = 0
            chosen_name = names[images.index(player.current_image_A)]
            chosen_price = player.current_price_A
            reliability = reliabilities[images.index(player.current_image_A)]
        else:
            player.winner_image_choice1 = player.current_image_B
            player.winner_price_choice1 = player.current_price_B
            player.winner_choice = 1
            chosen_name = names[images.index(player.current_image_B)]
            chosen_price = player.current_price_B
            reliability = reliabilities[images.index(player.current_image_B)]

        # Store choices for result recap
        player.participant.vars['choice1_name'] = chosen_name
        player.participant.vars['choice1_price'] = chosen_price
        player.choice1_winner = chosen_name

        # Simulate risk
        if random.random() > reliability:
            player.risk_simulated = True
            player.risk_penalty = risk_cost
        else:
            player.risk_simulated = False
            player.risk_penalty = 0

        player.current_image_A = player.winner_image_choice1
        round_in_cycle = (player.round_number - 1) % 4

        if round_in_cycle == 0:
            player.current_image_B = C.CAR_IMAGES[2]
            player.current_price_B = C.CAR_PRICES[2]
        elif round_in_cycle == 1:
            player.current_image_B = C.APPLIANCES_IMAGES[2]
            player.current_price_B = C.APPLIANCES_PRICES[2]
        elif round_in_cycle == 2:
            player.current_image_B = C.ELECTRICITY_IMAGES[2]
            player.current_price_B = C.ELECTRICITY_PRICES[2]
        elif round_in_cycle == 3:
            player.current_image_B = C.FUEL_IMAGES[2]
            player.current_price_B = C.FUEL_PRICES[2]

class Choice2(Page):
    form_model = 'player'
    form_fields = ['chosen_product']

    @staticmethod
    def vars_for_template(player: Player):
        cycle = (player.round_number - 1) // 4
        images, names, descriptions, prices, reliabilities, risk_cost, contexts = get_current_context(player)
        context = contexts[cycle]
        additional_info = f"Jika produk yang Anda pilih rusak/bermasalah dalam jangka waktu 5 tahun, maka Anda harus mengeluarkan biaya perbaikan sebesar Rp{risk_cost:,}."

        return dict(
            context=context,
            additional_info=additional_info,
            image_A='image_rating/{}'.format(player.current_image_A),
            image_B='image_rating/{}'.format(player.current_image_B),
            name_A=names[images.index(player.current_image_A)],
            name_B=names[2],
            desc_A=descriptions[images.index(player.current_image_A)],
            desc_B=descriptions[2],
            price_A='{:,}'.format(round(player.current_price_A)).replace(',', '.'),
            price_B='{:,}'.format(round(player.current_price_B)).replace(',', '.'),
            reliability_A=reliabilities[images.index(player.current_image_A)] * 100,
            reliability_B=reliabilities[2] * 100,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        images, names, descriptions, prices, reliabilities, risk_cost, contexts = get_current_context(player)

        if player.chosen_product == 'A':
            player.winner_image_choice2 = player.current_image_A
            player.winner_price_choice2 = player.current_price_A
            player.winner_choice = 0
            chosen_name = names[images.index(player.current_image_A)]
            chosen_price = player.current_price_A
            reliability = reliabilities[images.index(player.current_image_A)]
        else:
            player.winner_image_choice2 = player.current_image_B
            player.winner_price_choice2 = player.current_price_B
            player.winner_choice = 1
            chosen_name = names[images.index(player.current_image_B)]
            chosen_price = player.current_price_B
            reliability = reliabilities[images.index(player.current_image_B)]

        # Store choices for result recap
        player.participant.vars['choice2_name'] = chosen_name
        player.participant.vars['choice2_price'] = chosen_price
        player.choice2_winner = chosen_name

        # Simulate risk
        if random.random() > reliability:
            player.risk_simulated = True
            player.risk_penalty = risk_cost
        else:
            player.risk_simulated = False
            player.risk_penalty = 0

        player.current_image_A = player.winner_image_choice1
        round_in_cycle = (player.round_number - 1) % 4

        if round_in_cycle == 0:
            player.current_image_B = C.CAR_IMAGES[3]
            player.current_price_B = C.CAR_PRICES[3]
        elif round_in_cycle == 1:
            player.current_image_B = C.APPLIANCES_IMAGES[3]
            player.current_price_B = C.APPLIANCES_PRICES[3]
        elif round_in_cycle == 2:
            player.current_image_B = C.ELECTRICITY_IMAGES[3]
            player.current_price_B = C.ELECTRICITY_PRICES[3]
        elif round_in_cycle == 3:
            player.current_image_B = C.FUEL_IMAGES[3]
            player.current_price_B = C.FUEL_PRICES[3]

class Choice3(Page):
    form_model = 'player'
    form_fields = ['chosen_product']

    @staticmethod
    def vars_for_template(player: Player):
        cycle = (player.round_number - 1) // 4
        images, names, descriptions, prices, reliabilities, risk_cost, contexts = get_current_context(player)
        context = contexts[cycle]
        additional_info = f"Jika produk yang Anda pilih rusak/bermasalah dalam jangka waktu 5 tahun, maka Anda harus mengeluarkan biaya perbaikan sebesar Rp{risk_cost:,}."

        return dict(
            context=context,
            additional_info=additional_info,
            image_A='image_rating/{}'.format(player.current_image_A),
            image_B='image_rating/{}'.format(player.current_image_B),
            name_A=names[images.index(player.current_image_A)],
            name_B=names[3],
            desc_A=descriptions[images.index(player.current_image_A)],
            desc_B=descriptions[3],
            price_A='{:,}'.format(round(player.current_price_A)).replace(',', '.'),
            price_B='{:,}'.format(round(player.current_price_B)).replace(',', '.'),
            reliability_A=reliabilities[images.index(player.current_image_A)] * 100,
            reliability_B=reliabilities[3] * 100,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        images, names, descriptions, prices, reliabilities, risk_cost, contexts = get_current_context(player)

        if player.chosen_product == 'A':
            player.winner_image_choice1 = player.current_image_A
            player.winner_price_choice1 = player.current_price_A
            player.winner_choice = 0
            chosen_name = names[images.index(player.current_image_A)]
            chosen_price = player.current_price_A
            reliability = reliabilities[images.index(player.current_image_A)]
        else:
            player.winner_image_choice1 = player.current_image_B
            player.winner_price_choice1 = player.current_price_B
            player.winner_choice = 1
            chosen_name = names[images.index(player.current_image_B)]
            chosen_price = player.current_price_B
            reliability = reliabilities[images.index(player.current_image_B)]

        # Store choices for result recap
        player.participant.vars['choice3_name'] = chosen_name
        player.participant.vars['choice3_price'] = chosen_price
        player.choice3_winner = chosen_name

        # Simulate risk
        if random.random() > reliability:
            player.risk_simulated = True
            player.risk_penalty = risk_cost
        else:
            player.risk_simulated = False
            player.risk_penalty = 0

        # Final pay calculation
        player.income = player.endowment - player.winner_price_choice1 - player.risk_penalty


class Result(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # Determine the final choice based on the specified scenario
        choice1_winner = player.choice1_winner
        choice2_winner = player.choice2_winner
        choice3_winner = player.choice3_winner

        # Initialize final choice and background
        final_choice = None
        background = ""

        if choice1_winner == choice2_winner and choice1_winner != choice3_winner:
            # A won Choice1 and Choice2 but lost Choice3
            final_choice = random.choice([choice1_winner, choice3_winner])
            background = f"Pada halaman pertama dan kedua {choice1_winner} dipilih, tapi pada halaman ketiga {choice3_winner} dipilih. Maka, 50:50 antara {choice1_winner} dan {choice3_winner}."
        elif choice1_winner == choice3_winner and choice1_winner != choice2_winner:
            # A won Choice1 and Choice3 but lost Choice2 to C1
            final_choice = random.choice([choice1_winner, choice2_winner])
            background = f"Pada halaman pertama dan ketiga {choice1_winner} dipilih, tapi pada halaman kedua {choice2_winner} dipilih. Maka, 50:50 antara {choice1_winner} dan {choice2_winner}."
        elif choice1_winner != choice2_winner and choice2_winner == choice3_winner:
            # A only won Choice1 but lost Choice2 and Choice3
            final_choice = random.choice([choice2_winner, choice3_winner])
            background = f"Pada halaman kedua dan ketiga {choice2_winner} dan {choice3_winner} dipilih, tapi pada halaman pertama {choice1_winner} dipilih. Maka, 50:50 antara {choice2_winner} dan {choice3_winner}."
        elif choice1_winner == choice2_winner and choice2_winner == choice3_winner:
            # If all choices are the same
            final_choice = choice1_winner
            background = "Produk dipilih secara konsisten di semua halaman."
        elif choice1_winner != choice2_winner and choice1_winner != choice3_winner:
            # Scenario where A only won in Choice 1, and lost in both Choice 2 and Choice 3
            final_choice = random.choice([choice2_winner, choice3_winner])
            background = f"Pada halaman pertama {choice1_winner} dipilih, tapi pada halaman kedua {choice2_winner} dan halaman ketiga {choice3_winner} dipilih. Maka, 50:50 antara {choice2_winner} dan {choice3_winner}."

        # Fallback logic in case none of the above conditions were met
        if final_choice is None:
            final_choice = choice1_winner
            background = "Produk dipilih secara default ke pemenang halaman pertama."

        # Get the price of the final choice
        choice_price_map = {
            player.choice1_winner: player.participant.vars.get('choice1_price'),
            player.choice2_winner: player.participant.vars.get('choice2_price'),
            player.choice3_winner: player.participant.vars.get('choice3_price')
        }
        chosen_price = choice_price_map.get(final_choice, 0)

        # Calculate payoff
        endowment = player.endowment
        risk_penalty = player.risk_penalty if player.risk_penalty is not None else 0
        payoff = (endowment - chosen_price) + chosen_price - risk_penalty
        player.income = payoff
        player.choice1_price = player.participant.vars.get('choice1_price')
        player.choice2_price = player.participant.vars.get('choice2_price')
        player.choice3_price = player.participant.vars.get('choice3_price')

        return dict(
            choice1_name=player.participant.vars.get('choice1_name'),
            choice1_price='{:,}'.format(round(player.participant.vars.get('choice1_price'))).replace(',', '.'),
            choice2_name=player.participant.vars.get('choice2_name'),
            choice2_price='{:,}'.format(round(player.participant.vars.get('choice2_price'))).replace(',', '.'),
            choice3_name=player.participant.vars.get('choice3_name'),
            choice3_price='{:,}'.format(round(player.participant.vars.get('choice3_price'))).replace(',', '.'),
            final_choice=final_choice,
            chosen_price='{:,}'.format(round(chosen_price)).replace(',', '.'),
            payoff='{:,}'.format(round(payoff)).replace(',', '.'),
            risk_simulated=player.risk_simulated,
            risk_penalty='{:,}'.format(round(risk_penalty)).replace(',', '.'),
            background=background,
            endowment='{:,}'.format(round(endowment)).replace(',', '.')
        )


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random
        import numpy as np
        participant = player.participant

        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            player.random_round = random_round
            participant.vars['selected_round'][__name__] = random_round
            player_in_selected_round = player.in_round(random_round)
            player.potential_payoff = player_in_selected_round.income
            potential_payoff = player.potential_payoff

class FinalPayoff(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        selected_round = player.random_round
        player_in_selected_round = player.in_round(selected_round)
        final_payoff = player_in_selected_round.income

        # Determine the type of goods based on the selected round
        round_index = (selected_round - 1) % 4
        if round_index == 0:
            goods_type = "Mobil"
            adjusted_payoff = final_payoff / 10000
        elif round_index == 1:
            goods_type = "Kompor Listrik"
            adjusted_payoff = final_payoff / 500
        elif round_index == 2:
            goods_type = "Listrik Rumah"
            adjusted_payoff = final_payoff / 500
        elif round_index == 3:
            goods_type = "BBM"
            adjusted_payoff = final_payoff / 10

        # Store the final payoff in the player's field
        player.app_payoff = adjusted_payoff
        player.final_payoff = player.app_payoff + 10000

        return dict(
            selected_round=selected_round,
            app_payoff='{:,}'.format(round(player.app_payoff)).replace(',', '.'),
            final_payoff='{:,}'.format(round(player.final_payoff)).replace(',', '.'),
            goods_type=goods_type,
        )

page_sequence = [Choice1, Choice2, Choice3, Result, FinalPayoff]
