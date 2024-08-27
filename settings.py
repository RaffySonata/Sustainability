from os import environ

SESSION_CONFIGS = [
     dict(
         name='anp',
         app_sequence=['anp'],
         num_demo_participants=3,
     ),
    dict(
         name='image',
         app_sequence=['image_rating'],
         num_demo_participants=3,
     ),
    dict(
        name='instructions',
        app_sequence=['instructions'],
        num_demo_participants=3,
    ),
    dict(
        name='survey',
        app_sequence=['survey'],
        num_demo_participants=3,
    ),
    dict(
        name='sustainability',
        app_sequence=['instructions','practice_round','image_rating','survey'],
        num_demo_participants=3,
    ),
    dict(
        name='practice',
        app_sequence=['practice_round'],
        num_demo_participants=3,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_FIELDS = [
    'completions_by_treatment',
    'past_groups',
    'matrices',
    'wait_for_ids',
    'arrived_ids',
]

PARTICIPANT_FIELDS = [
    'app_payoffs',
    'app_row',
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'quiz_num_correct',
    'selected_round',
    'task_rounds',
    'time_pressure',
    'wait_page_arrival',
    'umr_list',
    'iw_lists',
    'sw_lists',
    'endowment_lists',
    'iw_type',
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

DEBUG=True
ADMIN_USERNAME = 'admin'
# for security, best to set admin passwordInput in an environment variable
ADMIN_PASSWORD = 'admin'
AUTH_LEVEL= environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5123142091007'
