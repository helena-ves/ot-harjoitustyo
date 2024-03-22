import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(5000)
    
    def test_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edulliset_kun_rahamaara_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisen_maara_ei_riittava_edulliseen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukkaat_kun_rahamaara_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisen_maara_ei_riittava_maukkaaseen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)   

    def test_korttiosto_syo_edullisesti_kun_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 47.60)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttiosto_syo_maukkaasti_kun_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo_euroina(), 46.00)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttiosto_jos_raha_ei_riita(self):
        kortti = Maksukortti(0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 60.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.0)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10), False)
