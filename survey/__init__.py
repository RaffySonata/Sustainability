from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Define form fields based on the questions
    q1 = models.StringField(
        label="Saya yakin saya akan selalu membeli BBM Pertamax Green 95 demi lingkungan dan pembangunan yang berkelanjutan meski SPBU yang menjualnya cukup jauh (3 km) dari tempat saya tinggal.",
        choices=['Di bawah 3km', '3km-5km','Di atas 5km'],
        widget=widgets.RadioSelect
    )
    q2 = models.StringField(
        label="Saya yakin bahwa pemerintah akan segera membangun infrastruktur yang baik untuk mendukung lingkungan dan pembangunan yang berkelanjutan (misal: memperluas pembangunan pembangkit listrik tenaga surya).",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q3 = models.StringField(
        label="Saya yakin bahwa pihak swasta (investor) akan segera ikut dalam pembangunan infrastruktur yang tepat dan baik untuk mendukung lingkungan yang berkelanjutan (misal: terkait penyediaan stasiun pengisian kendaraan listrik umum/SPKLU).",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q4 = models.StringField(
        label="Saya yakin bahwa saya akan tetap membeli mobil listrik (jika memiliki uang cukup) meski saya tinggal di daerah pedesaan yang jauh dari dealer mobil tersebut demi mendukung lingkungan dan pembangunan yang berkelanjutan.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q5 = models.StringField(
        label="Saya yakin dalam waktu dekat akan banyak produsen panel surya rumahan, termasuk di sekitar daerah saya tinggal, dan saya akan membelinya jika memiliki uang yang cukup untuk mendukung pembangunan yang berkelanjutan.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q6 = models.StringField(
        label="Saya yakin pemerintah akan segera merealisasikan jaringan gas rumah tangga di sekitar saya tinggal dan saya (rumah saya) akan berlangganan jaringan gas tersebut untuk mendukung pembangunan yang berkelanjutan.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q7 = models.StringField(
        label="Saya yakin untuk tetap menggunakan kompor listrik di rumah saya (jika memiliki uang cukup) demi mendukung lingkungan dan pembangunan berkelanjutan meskipun tidak banyak tetangga sekitar dan orang yang saya kenal menggunakan kompor listrik tersebut.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q8 = models.StringField(
        label="Saya yakin dalam waktu dekat akan banyak yang sadar dan menggunakan BBM Pertamax Green 95 demi lingkungan dan pembangunan berkelanjutan di Indonesia yang berkelanjutan.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q9 = models.StringField(
        label="Saya yakin bahwa keluarga, kolega, dan teman saya akan ikut menggunakan BBM Pertamax Green 95 demi lingkungan dan pembangunan berkelanjutan meskipun mereka setelahnya tidak tahu apa manfaatnya.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q10 = models.StringField(
        label="Saya yakin akan tetap membeli mobil listrik (jika memiliki uang cukup) meskipun saya tahu bahwa mobil listrik tersebut diproduksi perusahaan asing.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q11 = models.StringField(
        label="Saya yakin untuk tetap mendukung program kompor listrik dari pemerintah meskipun saya tahu jika listrik di Indonesia kebanyakan masih dihasilkan dari Batubara.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    q12 = models.StringField(
        label="Saya yakin untuk tetap mendukung dan menggunakan BBM Pertamax Green 95 meskipun saya tahu bahwa bahan utama campuran BBM Pertamax Green 95 berasal dari kelapa sawit yang banyak ditanam di Pulau Kalimantan, Sumatera, dan Sulawesi.",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )

    # Demographic questions
    usia = models.IntegerField(
        label="Usia Anda (dalam tahun):"
    )
    jenis_kelamin = models.StringField(
        label="Jenis kelamin Anda:",
        choices=['Laki-laki', 'Perempuan'],
        widget=widgets.RadioSelect
    )
    pendidikan = models.StringField(
        label="Tingkat pendidikan yang sedang atau telah Anda tempuh:",
        choices=['Sarjana (S1/D4)', 'Magister (S2)', 'Doktoral (S3)'],
        widget=widgets.RadioSelect
    )
    aktivitas = models.StringField(
        label="Aktivitas utama Anda saat ini:",
        choices=['Kuliah', 'Lulus belum bekerja', 'Bekerja'],
        widget=widgets.RadioSelect
    )
    tahu_program = models.StringField(
        label="Apakah Anda merasa cukup mengetahui program transisi energi dan pembangunan berkelanjutan yang sedang direncanakan dan dijalankan di Indonesia:",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    ikuti_isu = models.StringField(
        label="Apakah Anda merasa cukup mengikuti perkembangan isu transisi energi dan Pembangunan berkelanjutan di tingkat global:",
        choices=['Ya', 'Tidak'],
        widget=widgets.RadioSelect
    )
    bidang_studi = models.StringField(
        label="Cakupan bidang studi yang sedang atau telah Anda tempuh:",
        choices=['Sosio humaniora', 'Sains dan Teknologi Rekayasa', 'Agro, Hayati, dan Veteriner', 'Medis'],
        widget=widgets.RadioSelect
    )
    metode_pembayaran = models.StringField(
        label="Metode pembayaran online yang Anda gunakan:",
        choices=['OVO', 'GoPay', 'Shopee Pay', 'Bank BNI', 'Bank Mandiri'],
        widget=widgets.RadioSelect
    )
    no_hp_rekening = models.StringField(
        label="No. HP untuk online payment/No. Rekening:"
    )
    menariknya_eksperimen = models.StringField(
        label="Seberapa menariknya eksperimen ini bagi Anda:",
        choices=['Tidak menarik', 'Cukup menarik', 'Menarik', 'Sangat menarik'],
        widget=widgets.RadioSelect
    )

class Survey(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']

class Demographic(Page):
    form_model = 'player'
    form_fields = [
        'usia', 'jenis_kelamin', 'pendidikan', 'aktivitas',
        'tahu_program', 'ikuti_isu', 'bidang_studi',
        'metode_pembayaran', 'no_hp_rekening', 'menariknya_eksperimen'
    ]

page_sequence = [Survey, Demographic]
