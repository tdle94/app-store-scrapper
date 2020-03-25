"""
App Store Scraper

A web scraper for IOS app store.
"""

___version___ = "0.0.1"

import logging

from lib.api import (
    details,
    search,
    suggest,
    collection,
    similar,
    rating,
    review,
)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
