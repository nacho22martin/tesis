import os

from Testing import ZopeTestCase
from App.Common import package_home

HAS_I18NDUDE = True
try:
    from Products.i18ntestcase import PotTestCase, PoTestCase
    from Products.i18ntestcase.I18NTestCase import getPoFiles, getPotFiles, getProductFromPath
    from i18ndude import catalog
except ImportError:
    HAS_I18NDUDE = False

tests=[]
if HAS_I18NDUDE:
    GLOBALS = globals()
    PACKAGE_HOME = os.path.normpath(os.path.join(package_home(GLOBALS), '..', '..'))

    head, tail = os.path.split(PACKAGE_HOME)
    if tail == 'tests':
        PACKAGE_HOME = os.path.join(PACKAGE_HOME, '..')

    i18ndir = os.path.normpath(PACKAGE_HOME)

    products=[]
    pots={}
    pot_catalogs={}
    pot_lens={}

    for potFile in getPotFiles(path=i18ndir):
        product = getProductFromPath(potFile)
        if product not in products:
            products.append(product)
        if product not in pot_catalogs:
            cat = catalog.MessageCatalog(filename=potFile)
            cat_len = len(cat)
            pots.update({product: potFile})
            pot_catalogs.update({product: cat})
            pot_lens.update({product: cat_len})

    for product in products:
        class TestOnePOT(PotTestCase.PotTestCase):
            product = product
            pot = pots[product]
        tests.append(TestOnePOT)

        for poFile in getPoFiles(path=i18ndir, product=product):
            class TestOnePoFile(PoTestCase.PoTestCase):
                po = poFile
                product = product
                pot_cat = pot_catalogs[product]
                pot_len = pot_lens[product]
            tests.append(TestOnePoFile)

import unittest
def test_suite():
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTest(unittest.makeSuite(test))
    return suite
