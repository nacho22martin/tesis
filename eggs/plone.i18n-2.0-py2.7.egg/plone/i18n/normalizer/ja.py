# -*- coding: UTF-8 -*-

from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implements
from plone.i18n.normalizer.base import allowed

MAX_LENGTH = 6

TABLE = "abcdefghijklmnopqrstuvwxyz0123456789"
TABLE_LEN = len(TABLE)

def _gethashed(obj, n):
   num = hash(obj) % (TABLE_LEN ** n)
   while True:
       d, m = divmod(num, TABLE_LEN)
       num = d
       yield TABLE[m]
       if d == 0:
           return

def ja_normalize(text, max_length=MAX_LENGTH):
    """
    This function is normalize for Japanese.
    exchange from unicode string to hash and base64 string.
    """
    text = text.strip()
    if all(s in allowed for s in text):
        return text.encode('ascii')
    else:
        return "".join(_gethashed(text, max_length))
    

class Normalizer(object):
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(INormalizer, Normalizer)
      True

      >>> norm = Normalizer()
      >>> text = unicode("test page", 'utf-8')
      >>> norm.normalize(text)
      'test page'

      >>> norm = Normalizer()
      >>> text = unicode("テストページ", 'utf-8')
      >>> norm.normalize(text)
      '921bib'
    """
    implements(INormalizer)

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return ja_normalize(text)

normalizer = Normalizer()
