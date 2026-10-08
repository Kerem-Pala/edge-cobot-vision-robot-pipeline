import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from src.transform import transormRedCoordinates

class TestTransform(unittest.TestCase):
    def test_sol_ust_kose(self):
        # Kameradaki sol üst köşe piksellerini (100, 50) veriyoruz
        # Gerçek dünyada bunun A4 kağıdının (0, 0) noktası olması lazım
        x_mm, y_mm = transormRedCoordinates(224, 204)
        
        # Sonuçların 0'a çok yakın (hata payı içinde) olduğunu test et
        self.assertAlmostEqual(x_mm, 0.0, places=1)
        self.assertAlmostEqual(y_mm, 0.0, places=1)

    def test_sag_alt_kose(self):
        # Kameradaki sağ alt köşe piksellerini (400, 300) veriyoruz
        # Gerçek dünyada bunun (210, 297) olması lazım
        x_mm, y_mm = transormRedCoordinates(1209, 469)
        
        self.assertAlmostEqual(x_mm, 210.0, places=1)
        self.assertAlmostEqual(y_mm, 297.0, places=1)

if __name__ == '__main__':
    unittest.main()
