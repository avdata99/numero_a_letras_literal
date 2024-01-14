import unittest

from numero_a_letras import numero_a_letras, numero_a_moneda


class TestNumeroALetras(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(numero_a_letras(0), 'cero')
        self.assertEqual(numero_a_letras(1), 'uno')
        self.assertEqual(numero_a_letras(2), 'dos')
        self.assertEqual(numero_a_letras(3), 'tres')
        self.assertEqual(numero_a_letras(4), 'cuatro')
        self.assertEqual(numero_a_letras(5), 'cinco')
        self.assertEqual(numero_a_letras(6), 'seis')
        self.assertEqual(numero_a_letras(7), 'siete')
        self.assertEqual(numero_a_letras(8), 'ocho')
        self.assertEqual(numero_a_letras(9), 'nueve')

    def test_decenas(self):
        self.assertEqual(numero_a_letras(10), 'diez')
        self.assertEqual(numero_a_letras(11), 'once')
        self.assertEqual(numero_a_letras(12), 'doce')
        self.assertEqual(numero_a_letras(13), 'trece')
        self.assertEqual(numero_a_letras(14), 'catorce')
        self.assertEqual(numero_a_letras(15), 'quince')
        self.assertEqual(numero_a_letras(16), 'dieciseis')
        self.assertEqual(numero_a_letras(17), 'diecisiete')
        self.assertEqual(numero_a_letras(18), 'dieciocho')
        self.assertEqual(numero_a_letras(19), 'diecinueve')
        self.assertEqual(numero_a_letras(20), 'veinte')
        self.assertEqual(numero_a_letras(21), 'veintiuno')
        self.assertEqual(numero_a_letras(22), 'veintidos')
        self.assertEqual(numero_a_letras(23), 'veintitres')
        self.assertEqual(numero_a_letras(24), 'veinticuatro')
        self.assertEqual(numero_a_letras(25), 'veinticinco')
        self.assertEqual(numero_a_letras(26), 'veintiseis')
        self.assertEqual(numero_a_letras(27), 'veintisiete')
        self.assertEqual(numero_a_letras(28), 'veintiocho')
        self.assertEqual(numero_a_letras(29), 'veintinueve')
        self.assertEqual(numero_a_letras(30), 'treinta')
        self.assertEqual(numero_a_letras(31), 'treinta y uno')

    def test_decenas_diez(self):
        self.assertEqual(numero_a_letras(40), 'cuarenta')
        self.assertEqual(numero_a_letras(50), 'cincuenta')
        self.assertEqual(numero_a_letras(60), 'sesenta')
        self.assertEqual(numero_a_letras(70), 'setenta')
        self.assertEqual(numero_a_letras(80), 'ochenta')
        self.assertEqual(numero_a_letras(90), 'noventa')
        self.assertEqual(numero_a_letras(99), 'noventa y nueve')

    def test_centenas(self):
        self.assertEqual(numero_a_letras(100), 'cien')
        self.assertEqual(numero_a_letras(101), 'ciento uno')
        self.assertEqual(numero_a_letras(102), 'ciento dos')
        self.assertEqual(numero_a_letras(103), 'ciento tres')
        self.assertEqual(numero_a_letras(104), 'ciento cuatro')
        self.assertEqual(numero_a_letras(105), 'ciento cinco')
        self.assertEqual(numero_a_letras(106), 'ciento seis')
        self.assertEqual(numero_a_letras(107), 'ciento siete')
        self.assertEqual(numero_a_letras(108), 'ciento ocho')
        self.assertEqual(numero_a_letras(109), 'ciento nueve')
        self.assertEqual(numero_a_letras(110), 'ciento diez')
        self.assertEqual(numero_a_letras(111), 'ciento once')
        self.assertEqual(numero_a_letras(112), 'ciento doce')
        self.assertEqual(numero_a_letras(113), 'ciento trece')
        self.assertEqual(numero_a_letras(114), 'ciento catorce')
        self.assertEqual(numero_a_letras(115), 'ciento quince')
        self.assertEqual(numero_a_letras(116), 'ciento dieciseis')
        self.assertEqual(numero_a_letras(117), 'ciento diecisiete')
        self.assertEqual(numero_a_letras(118), 'ciento dieciocho')
        self.assertEqual(numero_a_letras(119), 'ciento diecinueve')
        self.assertEqual(numero_a_letras(120), 'ciento veinte')
        self.assertEqual(numero_a_letras(121), 'ciento veintiuno')
        self.assertEqual(numero_a_letras(122), 'ciento veintidos')
        self.assertEqual(numero_a_letras(123), 'ciento veintitres')
        self.assertEqual(numero_a_letras(124), 'ciento veinticuatro')
        self.assertEqual(numero_a_letras(125), 'ciento veinticinco')
        self.assertEqual(numero_a_letras(126), 'ciento veintiseis')
        self.assertEqual(numero_a_letras(127), 'ciento veintisiete')
        self.assertEqual(numero_a_letras(128), 'ciento veintiocho')
        self.assertEqual(numero_a_letras(129), 'ciento veintinueve')
        self.assertEqual(numero_a_letras(829), 'ochocientos veintinueve')
        self.assertEqual(numero_a_letras(999), 'novecientos noventa y nueve')

    def test_miles(self):
        self.assertEqual(numero_a_letras(1000), 'mil')
        self.assertEqual(numero_a_letras(1001), 'mil uno')
        self.assertEqual(numero_a_letras(1002), 'mil dos')
        self.assertEqual(numero_a_letras(1003), 'mil tres')
        self.assertEqual(numero_a_letras(1004), 'mil cuatro')
        self.assertEqual(numero_a_letras(1005), 'mil cinco')
        self.assertEqual(numero_a_letras(1006), 'mil seis')
        self.assertEqual(numero_a_letras(1007), 'mil siete')
        self.assertEqual(numero_a_letras(1008), 'mil ocho')
        self.assertEqual(numero_a_letras(1009), 'mil nueve')
        self.assertEqual(numero_a_letras(1010), 'mil diez')
        self.assertEqual(numero_a_letras(1011), 'mil once')
        self.assertEqual(numero_a_letras(1012), 'mil doce')
        self.assertEqual(numero_a_letras(1013), 'mil trece')
        self.assertEqual(numero_a_letras(1014), 'mil catorce')
        self.assertEqual(numero_a_letras(1015), 'mil quince')
        self.assertEqual(numero_a_letras(1016), 'mil dieciseis')
        self.assertEqual(numero_a_letras(1017), 'mil diecisiete')
        self.assertEqual(numero_a_letras(1018), 'mil dieciocho')
        self.assertEqual(numero_a_letras(1019), 'mil diecinueve')
        self.assertEqual(numero_a_letras(1020), 'mil veinte')
        self.assertEqual(numero_a_letras(1021), 'mil veintiuno')
        self.assertEqual(numero_a_letras(1022), 'mil veintidos')
        self.assertEqual(numero_a_letras(1023), 'mil veintitres')
        self.assertEqual(numero_a_letras(1024), 'mil veinticuatro')
        self.assertEqual(numero_a_letras(1025), 'mil veinticinco')
        self.assertEqual(numero_a_letras(1026), 'mil veintiseis')
        self.assertEqual(numero_a_letras(1027), 'mil veintisiete')
        self.assertEqual(numero_a_letras(1028), 'mil veintiocho')
        self.assertEqual(numero_a_letras(5329), 'cinco mil trescientos veintinueve')
        self.assertEqual(numero_a_letras(9999), 'nueve mil novecientos noventa y nueve')

    def test_decenas_miles(self):
        self.assertEqual(numero_a_letras(10000), 'diez mil')
        self.assertEqual(numero_a_letras(10001), 'diez mil uno')
        self.assertEqual(numero_a_letras(10002), 'diez mil dos')
        self.assertEqual(numero_a_letras(10003), 'diez mil tres')
        self.assertEqual(numero_a_letras(10004), 'diez mil cuatro')
        self.assertEqual(numero_a_letras(10005), 'diez mil cinco')
        self.assertEqual(numero_a_letras(10006), 'diez mil seis')
        self.assertEqual(numero_a_letras(10007), 'diez mil siete')
        self.assertEqual(numero_a_letras(10008), 'diez mil ocho')
        self.assertEqual(numero_a_letras(10009), 'diez mil nueve')
        self.assertEqual(numero_a_letras(10010), 'diez mil diez')
        self.assertEqual(numero_a_letras(10011), 'diez mil once')
        self.assertEqual(numero_a_letras(10012), 'diez mil doce')
        self.assertEqual(numero_a_letras(10013), 'diez mil trece')
        self.assertEqual(numero_a_letras(10014), 'diez mil catorce')
        self.assertEqual(numero_a_letras(10015), 'diez mil quince')
        self.assertEqual(numero_a_letras(10016), 'diez mil dieciseis')
        self.assertEqual(numero_a_letras(10017), 'diez mil diecisiete')
        self.assertEqual(numero_a_letras(10018), 'diez mil dieciocho')
        self.assertEqual(numero_a_letras(10019), 'diez mil diecinueve')
        self.assertEqual(numero_a_letras(10020), 'diez mil veinte')
        self.assertEqual(numero_a_letras(10021), 'diez mil veintiuno')
        self.assertEqual(numero_a_letras(10022), 'diez mil veintidos')
        self.assertEqual(numero_a_letras(10023), 'diez mil veintitres')
        self.assertEqual(numero_a_letras(10024), 'diez mil veinticuatro')
        self.assertEqual(numero_a_letras(10025), 'diez mil veinticinco')
        self.assertEqual(numero_a_letras(10026), 'diez mil veintiseis')
        self.assertEqual(numero_a_letras(34526), 'treinta y cuatro mil quinientos veintiseis')
        self.assertEqual(numero_a_letras(99999), 'noventa y nueve mil novecientos noventa y nueve')

    def test_centenas_miles(self):
        self.assertEqual(numero_a_letras(100000), 'cien mil')
        self.assertEqual(numero_a_letras(100001), 'cien mil uno')
        self.assertEqual(numero_a_letras(100002), 'cien mil dos')
        self.assertEqual(numero_a_letras(100003), 'cien mil tres')
        self.assertEqual(numero_a_letras(100004), 'cien mil cuatro')
        self.assertEqual(numero_a_letras(100005), 'cien mil cinco')
        self.assertEqual(numero_a_letras(100006), 'cien mil seis')
        self.assertEqual(numero_a_letras(100007), 'cien mil siete')
        self.assertEqual(numero_a_letras(100008), 'cien mil ocho')
        self.assertEqual(numero_a_letras(100009), 'cien mil nueve')
        self.assertEqual(numero_a_letras(100010), 'cien mil diez')
        self.assertEqual(numero_a_letras(100011), 'cien mil once')
        self.assertEqual(numero_a_letras(100012), 'cien mil doce')
        self.assertEqual(numero_a_letras(100013), 'cien mil trece')
        self.assertEqual(numero_a_letras(100014), 'cien mil catorce')
        self.assertEqual(numero_a_letras(100015), 'cien mil quince')
        self.assertEqual(numero_a_letras(100016), 'cien mil dieciseis')
        self.assertEqual(numero_a_letras(100017), 'cien mil diecisiete')
        self.assertEqual(numero_a_letras(100018), 'cien mil dieciocho')
        self.assertEqual(numero_a_letras(100019), 'cien mil diecinueve')
        self.assertEqual(numero_a_letras(100020), 'cien mil veinte')
        self.assertEqual(numero_a_letras(100021), 'cien mil veintiuno')
        self.assertEqual(numero_a_letras(100022), 'cien mil veintidos')
        self.assertEqual(numero_a_letras(100023), 'cien mil veintitres')
        self.assertEqual(numero_a_letras(100024), 'cien mil veinticuatro')
        self.assertEqual(numero_a_letras(100025), 'cien mil veinticinco')
        self.assertEqual(numero_a_letras(345678), 'trescientos cuarenta y cinco mil seiscientos setenta y ocho')
        self.assertEqual(numero_a_letras(999999), 'novecientos noventa y nueve mil novecientos noventa y nueve')

    def test_millones(self):
        self.assertEqual(numero_a_letras(1000000), 'un millon')
        self.assertEqual(numero_a_letras(1000001), 'un millon uno')
        self.assertEqual(numero_a_letras(1000002), 'un millon dos')
        self.assertEqual(numero_a_letras(1000003), 'un millon tres')
        self.assertEqual(numero_a_letras(1000004), 'un millon cuatro')
        self.assertEqual(numero_a_letras(1000005), 'un millon cinco')
        self.assertEqual(numero_a_letras(1000006), 'un millon seis')
        self.assertEqual(numero_a_letras(1000007), 'un millon siete')
        self.assertEqual(numero_a_letras(1000008), 'un millon ocho')
        self.assertEqual(numero_a_letras(1000009), 'un millon nueve')
        self.assertEqual(numero_a_letras(1000010), 'un millon diez')
        self.assertEqual(numero_a_letras(1000011), 'un millon once')
        self.assertEqual(numero_a_letras(1000012), 'un millon doce')
        self.assertEqual(numero_a_letras(1000013), 'un millon trece')
        self.assertEqual(numero_a_letras(1000014), 'un millon catorce')
        self.assertEqual(numero_a_letras(1000015), 'un millon quince')
        self.assertEqual(numero_a_letras(1000016), 'un millon dieciseis')
        self.assertEqual(numero_a_letras(1000017), 'un millon diecisiete')
        self.assertEqual(numero_a_letras(1000018), 'un millon dieciocho')
        self.assertEqual(numero_a_letras(1000019), 'un millon diecinueve')
        self.assertEqual(numero_a_letras(1000020), 'un millon veinte')
        self.assertEqual(numero_a_letras(1000021), 'un millon veintiuno')
        self.assertEqual(numero_a_letras(1000022), 'un millon veintidos')
        self.assertEqual(numero_a_letras(1000023), 'un millon veintitres')
        self.assertEqual(numero_a_letras(1000024), 'un millon veinticuatro')
        self.assertEqual(numero_a_letras(1234456), 'un millon doscientos treinta y cuatro mil cuatrocientos cincuenta y seis')

    def test_raros(self):
        self.assertEqual(numero_a_letras(1345.67), 'mil trescientos cuarenta y cinco con sesenta y siete')
        self.assertEqual(numero_a_letras(0.01), 'cero con uno')
        self.assertEqual(numero_a_letras(0.02), 'cero con dos')
        self.assertEqual(numero_a_letras(303003.014042), 'trescientos tres mil tres con uno')
        self.assertEqual(numero_a_letras(303003.055042), 'trescientos tres mil tres con seis')

    def test_raros_moneda(self):
        self.assertEqual(numero_a_moneda(1345.67), 'mil trescientos cuarenta y cinco pesos con sesenta y siete centavos')
        self.assertEqual(numero_a_moneda(0.01), 'cero pesos con un centavo')
        self.assertEqual(numero_a_moneda(0.02), 'cero pesos con dos centavos')
        self.assertEqual(numero_a_moneda(303003.014042), 'trescientos tres mil tres pesos con un centavo')
        self.assertEqual(numero_a_moneda(303003.055042), 'trescientos tres mil tres pesos con seis centavos')


if __name__ == '__main__':
    unittest.main()
