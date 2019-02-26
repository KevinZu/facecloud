# -*- coding: utf-8 -*-
import os


basedir = os.path.abspath(os.path.dirname(__file__))

VERSION_NAME = '0.0.1'

class Config(object):
    """
    The base configuration option. Contains the defaults.
    """

    DEBUG = False

    DEVELOPMENT = False
    STAGING = False
    PRODUCTION = False
    TESTING = False



class DevelopmentConfig(Config):
    """
    The configuration for a development environment
    """

    DEVELOPMENT = True
    DEBUG = True