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
        app_sequence=['instructions','image_rating','survey'],
        num_demo_participants=4,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

OTREE_AUTH_LEVEL = 'DEMO'
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'admin'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5123142091007'
