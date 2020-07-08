# -*- coding: utf-8 -*-

"""Top-level package"""

# =============================================================================
# Basic
# =============================================================================
import os

__author__ = """Dominique Makowski"""
__email__ = 'dom.makowski@gmail.com'
__version__ = '0.0.2'
__modulepath__ = os.path.split(__file__)[0]




# =============================================================================
# Imports
# =============================================================================
from .pypi_downloads import *
from .github_stars import *
from .github_contributors import *