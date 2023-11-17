# Dimensión Entorno Urbano

# Documentos de referencia
# https://docs.google.com/spreadsheets/d/11sXtbYPi6ebDXrvFoHpA3qKGjS_OI4naNa0M4sXuFDY/edit#gid=1671296316
# https://kf.kobotoolbox.org/#/forms/aMbrw7VQcoKiZeRuEoJfCe/edit

# ------------------------------------------------------------
# Subcategoría: Compact neighbourhood
# Si seleccionaron Ninguno (0) el indicador vale 0
# En caso contrario, dependiendo de cuantos seleccionaron se calcula de 0 a 100, 8 opciones
# ej. "group_consented/group_urbano/urbano_1": "1 2 5 7" puntuación 50
# ej. "group_consented/group_urbano/urbano_1": "1 2 3 4 5 6 7 8" puntuación 100
# ej. "group_consented/group_urbano/urbano_1": "0" puntuación 0
# ej. "group_consented/group_urbano/urbano_1": "1 2 5 7 0" puntuación 0
def enturb_1(datos):
    respuestas = datos['group_consented/group_urbano/urbano_1'].split()
    if "0" in respuestas:
        return 0
    else:
        return len(respuestas)/8 * 100


# ------------------------------------------------------------
# Subcategoría: Well connected
# Si seleccionaron Ninguno (0) el indicador vale 0
# En caso contrario, dependiendo de cuantos seleccionaron se calcula de 0 a 100, 5 opciones
def enturb_2(datos):
    respuestas = datos['group_consented/group_urbano/urbano_2'].split()
    if "0" in respuestas:
        return 0
    else:
        return len(respuestas)/5 * 100


# ------------------------------------------------------------
# Subcategoría: Mobility patterns
# Si seleccionaron Ninguno (0) el indicador vale 0
# En caso contrario, dependiendo de cuantos seleccionaron se calcula de 0 a 100, 8 opciones
def enturb_3(datos):
    respuestas = datos['group_consented/group_urbano/urbano_3'].split()
    if "0" in respuestas:
        return 0
    else:
        return len(respuestas)/8 * 100
