## FUNCIÓN PARA EL TEST DE MULTIPLICACIÓN DE PRIMOS (n=p*q)
def calcular_producto_y_longitud(primo1, primo2):
    producto = primo1 * primo2
    longitud_en_bits = producto.bit_length()
    return producto, longitud_en_bits

# Ejemplo de uso con dos números primos
primo1 = 9577908256623349494681923209724992758006514365169244811902560688250618757872939430760119960306626866868877031043402716952325183167371293000434328092998881
primo2 = 9577908256623349494681923209724992758006514365169244811902560688250618757872932285936030165430188153818988990503064992274419390609277508426598746986029589

producto, longitud_en_bits = calcular_producto_y_longitud(primo1, primo2)
print(f"Producto de los primos (n=p*q):\n{producto}\n")
print(f"Longitud en bits del producto:\n{longitud_en_bits}\n")
