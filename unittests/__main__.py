from unittest import TestCase
from src import create_logger, Somni_Log
from ..src.constants import Loglevel, NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
from src.level_filter import LevelFilter


class Test_Loglevel(TestCase):
    def test_loglevel(self):
        self.assertEqual(None, NOTSET.INT)
        self.assertEqual(None, NOTSET.STRING)

    def test_notset(self):
        self.assertEqual(0, NOTSET.INT)
        self.assertEqual('NOTSET', NOTSET.STRING)

    def test_debug(self):
        self.assertEqual(10, DEBUG.INT)
        self.assertEqual('DEBUG', NOTSET.STRING)

    def test_info(self):
        self.assertEqual(20, INFO.INT)
        self.assertEqual('INFO', NOTSET.STRING)

    def test_warning(self):
        self.assertEqual(30, WARNING.INT)
        self.assertEqual('WARNING', NOTSET.STRING)

    def test_error(self):
        self.assertEqual(40, ERROR.INT)
        self.assertEqual('ERROR', NOTSET.STRING)

    def test_critical(self):
        self.assertEqual(50, CRITICAL.INT)
        self.assertEqual('CRITICAL', NOTSET.STRING)
