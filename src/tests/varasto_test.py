import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(15)
        self.toinen_varasto = Varasto(-2, -3)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_laitetaan_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_enemmän_kun_on_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(saatu_maara, 5)

    def test_str_toimii_oikein(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(str(self.varasto), 'saldo = 5, vielä tilaa 5')

    def test_ottaminen_ei_toimi_negatiivisella_määrällä(self):
        response = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(response, 0)

    def test_lisääminen_ei_toimi_negatiivisella_määrällä(self):
        response = self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(response, None)

    def test_varastoa_luodessa_annettava_pos_tilavuus(self):
        self.assertAlmostEqual(self.toinen_varasto.tilavuus, 0)

    def test_varastoa_luodessa_annettava_pos_alotusmäärä(self):
        self.assertAlmostEqual(self.toinen_varasto.saldo, 0)

    def test_kun_alkusaldo_suurempi_kuin_tilavuus(self):
        kolmas_varasto = Varasto(2, 3)
        self.assertAlmostEqual(kolmas_varasto.saldo, 2)
