from unittest import TestCase
from src.guru import Guru

class TestGuru(TestCase):

    def test_ask(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on
        self.assertEqual('68', guru.ask('how old is Tony Blair'))
        self.assertEqual('75', guru.ask('how old is trump'))
        self.assertEqual('8908081', guru.ask('what is the population of London'))
        self.assertEqual('2175601', guru.ask('what is the population of Paris'))
        