import pytest
import Examen2  # Asegúrate de importar la clase desde tu módulo

# Prueba para el método ObtieneValencia
def test_obtiene_valencia():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneValencia(12345)
    assert resultado == 3

# Prueba 2 para el método ObtieneValencia
def test_obtiene_valencia2():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneValencia(7689314233)
    assert resultado == 6

# Prueba para el método DivisibleTempo
def test_divisible_tempo():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.DivisibleTempo(10)
    assert resultado == [1, 2, 5, 10]

# Prueba 2 para el método DivisibleTempo
def test_divisible_tempo2():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.DivisibleTempo(31)
    assert resultado == [1, 31]

# Prueba para el método ObtieneMasBailable
def test_obtiene_mas_bailable():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneMasBailable([0.8, 0.9, 0.7, 0.6])
    assert resultado == 0.7

# Prueba 2 para el método ObtieneMasBailable
def test_obtiene_mas_bailable2():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneMasBailable([10, 35, 0.1, 34])
    assert resultado == 35

# Prueba para el método VerificaListaCanciones
def test_verifica_lista_canciones():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.VerificaListaCanciones([1, 2, 3])
    assert resultado

# Prueba 2 para el método VerificaListaCanciones cuando hay un elemento None
def test_verifica_lista_canciones2():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.VerificaListaCanciones([1, 2, None, 3])
    assert not resultado

# Prueba para el método Encuentra
def test_encuentra():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.Encuentra([2, 7, 1, 4, 5], 1)
    assert resultado