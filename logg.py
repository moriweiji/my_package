# -*- coding: utf-8 -*-

import logging
import logging.config


# log_file = 'fire.log'


def Loger(log_name, log_file):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(asctime)s -- %(name)s !!!%(levelname)s!!!: %(message)s'
            },
        },
        'filters': {
            'basic': {
                '()': SpiderFilter,
                'allow': ('mongo', 'redis', 'mysql', 'ix', 'fire', 'duomi', 'run'),
            },
            'warn': {
                '()': SpiderFilter,
                'disable': ()
            }
        },
        'handlers': {
            'file': {
                'level': 'WARN',
                'formatter': 'simple',
                'class': 'logging.FileHandler',
                'filename': log_file,
                'mode': 'a',
                'filters': ['warn']
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'database': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'simple',
                'filename': log_file,
                'mode': 'a',
                'filters': ['basic']
            }
        },
        'loggers': {
            'mongo': {
                'handlers': ['file'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'mysql': {
                # 使用database的handler
                'handlers': ['console', 'database'],
                # log 的级别为 DEBUG
                'level': 'DEBUG',
                # 是否要把log继续传递给更高级别（ancestor）的logger
                'propagate': False,
            },
            'redis': {
                'handlers': ['console', 'file', 'database'],
                'level': 'INFO',
                'filters': ['basic'],
                'propagate': False,
            },
            'run': {
                'handlers': ['console', 'file', 'database'],
                'level': 'INFO',
                'filters': ['basic'],
                'propagate': False,
            },
            'fire': {
                'handlers': ['console', 'file', 'database'],
                'level': 'INFO',
                'filters': ['basic'],
                'propagate': False,
            },
            'duomi': {
                'handlers': ['console', 'file', 'database'],
                'level': 'INFO',
                'filters': ['basic'],
                'propagate': False,
            },
            'taoma': {
                'handlers': ['console', 'file', 'database'],
                'level': 'INFO',
                'filters': ['basic'],
                'propagate': False,
            }

        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger(log_name)
    return logger


class SpiderFilter(logging.Filter):

    def __init__(self, allow=None, disable=None):
        self.allow_channels = allow
        self.disable_channels = disable

    def filter(self, record):
        if self.allow_channels is not None:
            if record.name in self.allow_channels:
                allow = True
            else:
                allow = False
        elif self.disable_channels is not None:
            if record.name in self.disable_channels:
                allow = False
            else:
                allow = True
        else:
            allow = False
        return allow


def log_output(logger, log_type, content_tuple):
    """

    :param logger: logger  class
    :param log_type: info, warn, error, debug logging 的方法
    :param content_tuple:  [('pro_name', 'duomi'),('resp', 'ok')] or str 必须以这种格式传入,输出多个需要输出的字段或者是字符串
    :return:
    """
    if isinstance(content_tuple, list) or isinstance(content_tuple, tuple):
        content_str = ' ==== '.join(["[{}]:{}".format(content[0], content[1]) for content in content_tuple])
        getattr(logger, log_type)(content_str)
    elif isinstance(content_tuple, str):
        getattr(logger, log_type)(content_tuple)
    else:
        raise TypeError('content_tuple Type error, content_tuple必须是list,tuple,str类型')


if __name__ == '__main__':
    log_file = 'duomi.log'
    logger = Loger('duomi', log_file)
    content_tuple = (('pro_name', 'duomi'), ('resp', 'ok'))
    # content_tuple = 'xxxxx'
    # content_tuple = dict(content_tuple)
    log_type = 'warn'
    log_output(logger, log_type, content_tuple)
