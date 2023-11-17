# Dimensión Entorno Urbano

# Documentos de referencia
# https://docs.google.com/spreadsheets/d/11sXtbYPi6ebDXrvFoHpA3qKGjS_OI4naNa0M4sXuFDY/edit#gid=1671296316
# https://kf.kobotoolbox.org/#/forms/aMbrw7VQcoKiZeRuEoJfCe/edit

# ------------------------------------------------------------
# Categoría: Urban form / Forma Urbana
# Subcategoría: Mixed uses
# Col. E: Availability of facilities and basic servicies within a walking distance that avoid the need for long and
#   motorized trips, according to 15-minute city principles, and ensuring the fullfillment of basic needs such as food,
#   schools and medical care (pharmacyes and healthcare services), carecenters, and public spaces and green areas
# ------------------------------------------------------------
def enturb_1(datos):
    respuestas = datos['group_consented/group_urbano/urbano_1'].split()
    if "0" in respuestas:
        return 0

    if all(r in respuestas for r in ["1", "4", "5", "7"]): # Tiendas, guarderías, escuelas primaria y espacio publico
        return 100
    if len(respuestas(4)): # Al menos seleccionaron 4
        return 100


# ------------------------------------------------------------
# Subcategoría: Well connected
# ------------------------------------------------------------
def enturb_2(datos):
    respuestas = datos['group_consented/group_urbano/urbano_2'].split()
    if "0" in respuestas:
        return 0
    else:
        return len(respuestas)/5 * 100


# ------------------------------------------------------------
# Col. C: Mobility/ Movilidad
# Col. D: Subcategoría: Mobility patterns
# Col. E: Main mode of transport used in a daily basis and complementary information about travel purposes, people
#   involved in accompanying trips, where to, formal/informal use of public transport. Modal share & Travel information
# En este caso se quiere saber si caminan, usan bicicleta o transporte publico formal o informal
def enturb_3(datos):
    respuestas = datos['group_consented/group_urbano/urbano_3'].split()

    if "0" in respuestas: # no realiza desplazamientos por lo cual es sostenible ???
        return 100

    contador = 0
    if "3" in respuestas: # bicicleta
        contador += 1
    if "4" in respuestas: # caminar
        contador += 1
    if "5" in respuestas: # transporte publico informal
        contador += 1
    if "6" in respuestas: # transporte publico formal
        contador += 1

    return contador/4 * 100


# ------------------------------------------------------------
# Subcategoría: Accessibility
# Access and availability of public transportation options, considering formal and informal services and proximity
#   to stops
# Columna O: Proportion of people that have access to any public transport service
# En este caso se quiere saber si al menos tienen un transporte público a menos de 10 mins, 0 no tienen, 100 si tienen
def enturb_7(datos):
    respuestas = datos['group_consented/group_urbano/urbano_7'].split()
    if len(respuestas) > 0: # Seleccionaron al menos una opción
        return 100
    return 0 # No seleccionaron ninguna opción
