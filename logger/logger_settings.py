import structlog


LOGGING = {
    'version':1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters':{
        'large':{
            'format':'%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  %(lineno)d  %(message)s  '
        },
        'tiny':{
            'format':'%(asctime)s  %(message)s  '
        }
    },
    'handlers':{
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'large'
        },
        'logfile':{
            'level':'INFO',
               'class':'logging.handlers.TimedRotatingFileHandler',
            'when':'midnight',
            'interval':1,
            'backupCount': 10,
            'filename': os.path.join(MAIN_DIR, 'logs/commservice.log'),
            'formatter':'large',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers':{
        'django': {
            'handlers': ['console', 'mail_admins'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'custom_logger':{
            'handlers':['logfile'],
            'level':'DEBUG',
            'propagate':False,
        },
    },
}