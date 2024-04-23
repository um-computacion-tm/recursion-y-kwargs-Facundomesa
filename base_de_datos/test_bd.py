import unittest

from bd import ver_datos

class test_db(unittest.TestCase):
    database = {
            '1':{
                "nombre1":"Pedro",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            '2':{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            '3':{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            },
            '4':{
                "nombre":"Fabricio",
                "apellido":"Romano"
            },
            '5':{
                "nombre":"Fabricio",
                "apellido":"Alonso"
            }
                }
    
    def test(self):
        resultado = ver_datos("Pedro", "Diego","Ruiz","Picasso", **self.database)
        self.assertEqual(resultado, '2')

    def test(self):
        resultado = ver_datos("Marcos", "Marcelo","Luciano","Elias","Gonzalez",**self.database)
        self.assertEqual(resultado, '1')

    def test(self):
        resultado = ver_datos("Marquitos", **self.database)
        self.assertEqual(resultado, 'no hay')

    def test_nombre(self):
        resultado = ver_datos("Fabricio", **self.database)
        self.assertEqual(resultado, 'Hay 2 ID con el mismo nombre')

    def test_duplicado(self):
        resultado = ver_datos("Fabricio", "Romano", **self.database)
        self.assertEqual(resultado, '4')

    def test_trampa(self):
        resultado = ver_datos("Fabricio", "Romano", "Alonso", **self.database)
        self.assertEqual(resultado, 'no hay')


if __name__ == '__main__':
    unittest.main()