import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldo_ei_muut_jos_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(1000)
        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_metodi_palauttaa_oikean_arvon_rahaa_nostettaessa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

    def test__str__(self):
        self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 10.00 euroa")