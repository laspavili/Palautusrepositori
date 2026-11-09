import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsServices(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_search_nimi_loytyy(self):
        pelaaja = self.stats.search("Semenko")
        self.assertIsNotNone(pelaaja)
        self.assertEqual(pelaaja.name,"Semenko")

    def test_search_nimi_ei_loydy(self):
            pelaaja = self.stats.search("Litmanen")
            self.assertIsNone(pelaaja)

    def test_team_joukkue_oikea_maara_pelaajia(self):
            pelaajat = self.stats.team("PIT")
            self.assertEqual(len(pelaajat), 1 )

            for pelaaja in pelaajat:
                self.assertEqual(pelaaja.team, "PIT")

    def test_team_joukkue_oikea_maara_pelaajia(self):
                pelaajat = self.stats.team("PIT")
                self.assertEqual(len(pelaajat), 1 )
                self.assertEqual(pelaajat[0].name, "Lemieux")

    def test_team_vaara_joukkue_maara_pelaajia(self):
                    pelaajat = self.stats.team("SUOMI")
                    self.assertEqual(len(pelaajat), 0 )

    def test_top_pelaajat_oikeassa_järjestyksessä(self):
           parhaat = self.stats.top(5)

           self.assertEqual(len(parhaat), 5)
           self.assertEqual(parhaat[0].name, "Gretzky")
           self.assertEqual(parhaat[1].name, "Lemieux")
           self.assertEqual(parhaat[2].name, "Yzerman")
           self.assertEqual(parhaat[3].name, "Kurri")
           self.assertEqual(parhaat[4].name, "Semenko")

    

    
    

    