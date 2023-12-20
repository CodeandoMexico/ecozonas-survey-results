# Dimensión Entorno Urbano

# Documentos de referencia
# https://docs.google.com/spreadsheets/d/11sXtbYPi6ebDXrvFoHpA3qKGjS_OI4naNa0M4sXuFDY/edit#gid=1671296316
# https://kf.kobotoolbox.org/#/forms/aMbrw7VQcoKiZeRuEoJfCe/edit

import utils
from statistics import mean


# ------------------------------------------------------------
# Categoría: Urban form / Forma Urbana
# Subcategoría: Compact neighbourhood
# Density that ensure access to services, transportation options and prevent urban sprawl
# ------------------------------------------------------------
def a1(datos):

    if 'group_consented/group_urbano/urbano_21' not in datos:
        return

    respuestas = datos['group_consented/group_urbano/urbano_21'].split()
    if "1" in respuestas:  # Tamaño adecuado
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Urban form / Forma Urbana
# Subcategoría: Mixed uses
# Availability of facilities and basic servicies within a walking distance that avoid the need for long and
#   motorized trips, according to 15-minute city principles, and ensuring the fullfillment of basic needs such as food,
#   schools and medical care (pharmacyes and healthcare services), carecenters, and public spaces and green areas
# ------------------------------------------------------------
def a2(datos):

    if 'group_consented/group_urbano/urbano_1' not in datos:
        return

    respuestas = datos['group_consented/group_urbano/urbano_1'].split()

    if "0" in respuestas:  # Seleccionaron Ninguno
        return 0
    # Seleccionaron tiendas, guarderías, escuelas primaria y espacio publico
    if all(r in respuestas for r in ["1", "4", "5", "7"]):
        return 100
    if len(respuestas) >= 4:  # Seleccionaron al menos 4 opciones
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Urban form / Forma Urbana
# Subcategoría: Well connected
# Proximity to facilities, services and formal jobs at an adequate distance by PT (max 30 min)
# ------------------------------------------------------------
def a3(datos):
    if 'group_consented/group_urbano/urbano_2' not in datos:
        return

    respuestas = datos['group_consented/group_urbano/urbano_2'].split()

    if "0" in respuestas:  # Seleccionaron Ninguno
        return 0
    if len(respuestas) >= 5:  # Tienen acceso a todas las opciones, si no seleccionan todas no cuenta
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Built-up environment / Entorno construido
# Subcategoría: Building Efficiency
# Energy efficiency trend for the residential sector considering measures taken at households
# ------------------------------------------------------------
def a4(datos):
    if 'group_consented/group_urbano/urbano_22' not in datos:
        return

    respuestas = datos['group_consented/group_urbano/urbano_22'].split()

    if "0" in respuestas:  # Seleccionaron Ninguno
        return 0
    if len(respuestas) >= 1:  # Tienen acceso a al menos una opción
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Built-up environment / Entorno construido
# Subcategoría: Housing conditions
# Adequate housing considering habitability, access to services and tenancy
# ------------------------------------------------------------
def a5(datos):
    if 'group_consented/group_urbano/urbano_23' not in datos:
        return

    respuestas = datos['group_consented/group_urbano/urbano_23'].split()

    # Seleccionaron Ninguno
    if "0" in respuestas:
        return 0
    if all(r in respuestas for r in ["1", "2", "3", "4", "5", "6"]):
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Mobility/ Movilidad
# Subcategoría: Mobility patterns
# Main mode of transport used in a daily basis and complementary information about travel purposes, people
#   involved in accompanying trips, where to, formal/informal use of public transport. Modal share & Travel information
# ------------------------------------------------------------
def a6(datos):
    if 'group_consented/group_urbano/urbano_3' not in datos:
        return

    respuestas = datos['group_consented/group_urbano/urbano_3'].split()

    if "0" in respuestas:  # no realiza desplazamientos por lo cual es sostenible ???
        return 100

    contador = 0
    if "3" in respuestas:  # bicicleta
        contador += 1
    if "4" in respuestas:  # caminar
        contador += 1
    if "5" in respuestas:  # transporte publico informal
        contador += 1
    if "6" in respuestas:  # transporte publico formal
        contador += 1

    return contador / 4 * 100


# ------------------------------------------------------------
# Categoría: Public Transport / Trasnporte Público
# Subcategoría: Accessibility
# Access and availability of public transportation options, considering formal and informal services and proximity
#   to stops
# ------------------------------------------------------------
def a7(datos):
    if 'group_consented/group_urbano/urbano_7' not in datos:
        return
    respuestas = datos['group_consented/group_urbano/urbano_7'].split()
    if len(respuestas) > 0:  # Seleccionaron al menos una opción
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Public Transport / Trasnporte Público
# Subcategoría: Stops infrastructure
# Conditioning of stops infrastructure, considering all the features neccesary for a safe, comfort and inclusive waiting
#   area, that enables multimodal connections and the integratation of diverse sustainable modes of transportation
# ------------------------------------------------------------
def a8(datos):
    if 'group_consented/group_urbano/urbano_8' not in datos:
        return
    respuestas = datos['group_consented/group_urbano/urbano_8'].split()
    return int(respuestas[0]) / 3 * 100


# ------------------------------------------------------------
# Categoría: Public Transport / Trasnporte Público
# Subcategoría: Frecuency
# Frequency of public transport services by users' waiting time for a reliable service
# ------------------------------------------------------------
def a9(datos):
    respuestas = datos['group_consented/group_urbano/urbano_9'].split()
    if "1" in respuestas:  # Menos de 5 mins
        return 100
    if "2" in respuestas:  # Entre 5 y 10 mins
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Bikeability / Ciclabilidad
# Subcategoría: Bikeability
# Satisfaction with the actual conditions for cycling in the neighbourhood (bike lanes, bike parking, etc.)
# ------------------------------------------------------------
def a10(datos):
    respuestas_a = datos['group_consented/group_urbano/urbano_10_group/urbano_10a'].split()
    respuestas_b = datos['group_consented/group_urbano/urbano_10_group/urbano_10b'].split()
    respuestas_c = datos['group_consented/group_urbano/urbano_10_group/urbano_10c'].split()
    respuestas_d = datos['group_consented/group_urbano/urbano_10_group/urbano_10d'].split()

    # 0 No hay      0%
    # 1 Baja        33%
    # 2 Regular     66%
    # 3 Alta        100%

    return mean([utils.normalize(int(respuestas_a[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_b[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_c[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_d[0]), 0, 3, 0, 100)])


# ------------------------------------------------------------
# Categoría: Walkability / Caminabilidad
# Subcategoría: Walkability
# Satisfaction with the actual conditions for walking in the neighbourhood, are safe, comfortable and accessible for all
#   people, considerign both infrastructure and perception aspect
# ------------------------------------------------------------
def a11(datos):
    respuestas_a = datos['group_consented/group_urbano/urbano_11_group/urbano_11a'].split()
    respuestas_b = datos['group_consented/group_urbano/urbano_11_group/urbano_11b'].split()
    respuestas_c = datos['group_consented/group_urbano/urbano_11_group/urbano_11c'].split()

    # 0 No hay      0%
    # 1 Baja        33%
    # 2 Regular     66%
    # 3 Alta        100%

    return mean([utils.normalize(int(respuestas_a[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_b[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_c[0]), 0, 3, 0, 100)])


# ------------------------------------------------------------
# Categoría: Public spaces / Espacios públicos
# Subcategoría: Open public spaces and green areas
# Public spaces and environmental aspects that can improve health and wellbeing of the residents, considering green
#   spaces and vegetation and their distribution,  that are safe, attractive, comfortable, enjoyable, accesible, and
#   inclusive for all people from all backgrounds considering elements and opportunities to develop diverse activities
# ------------------------------------------------------------
def a12(datos):
    respuestas_a = datos['group_consented/group_urbano/urbano_12_group/urbano_12a'].split()
    respuestas_b = datos['group_consented/group_urbano/urbano_12_group/urbano_12b'].split()
    respuestas_c = datos['group_consented/group_urbano/urbano_12_group/urbano_12c'].split()
    respuestas_d = datos['group_consented/group_urbano/urbano_12_group/urbano_12d'].split()

    return mean([utils.normalize(int(respuestas_a[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_b[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_c[0]), 0, 3, 0, 100),
                 utils.normalize(int(respuestas_d[0]), 0, 3, 0, 100)])


# ------------------------------------------------------------
# Categoría: Public spaces / Espacios públicos
# Subcategoría: Space distribution
# Space allocation on streets and public spaces that allows flexibility for alternative uses and a balance on the use
#   of on-street space
# ------------------------------------------------------------
def a13(datos):
    respuestas = datos['group_consented/group_urbano/urbano_14'].split()

    if "1" in respuestas:  # Mas espacio para automoviles
        return 0
    return 100


# ------------------------------------------------------------
# Categoría: Safety and security / Seguridad
# Subcategoría: Road safety
# ------------------------------------------------------------
def a14(datos):
    respuestas = datos['group_consented/group_urbano/urbano_17'].split()

    if "0" in respuestas:  # Nadie ha estado en un siniestro
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Safety and security / Seguridad
# Subcategoría: Road safety
# ------------------------------------------------------------
def enturb_p18(datos):
    respuestas = datos['group_consented/group_urbano/urbano_18'].split()

    if "3" in respuestas:  # Peligrosa
        return 0
    return 100


# ------------------------------------------------------------
# Categoría: Safety and security / Seguridad
# Subcategoría: Security
# People's personal security in the neigborhood, considering experiences in terms of crime-behaviour rate along with
#   their unsafety perception in the public spaces, with an emphasis in differences by gender and women's perception
# ------------------------------------------------------------
def a15(datos):

    a15a = _a15a(datos)
    a15b = _a15b(datos)

    if a15a is not None:
        if a15b is not None:
            return mean([a15a, a15b])
        return a15a


def _a15a(datos):
    respuestas = datos['group_consented/group_urbano/urbano_19'].split()
    if "1" in respuestas:  # Sí ha sufrido X
        return 0
    return 100


def _a15b(datos):

    codigos = [
        'group_consented/group_urbano/urbano_20_group/urbano_20a',
        'group_consented/group_urbano/urbano_20_group/urbano_20b',
        'group_consented/group_urbano/urbano_20_group/urbano_20c',
        'group_consented/group_urbano/urbano_20_group/urbano_20d',
        'group_consented/group_urbano/urbano_20_group/urbano_20e',
        'group_consented/group_urbano/urbano_20_group/urbano_20f'
    ]
    existen = all(key in datos for key in codigos)
    if not existen:
        return None

    respuestas_a = datos['group_consented/group_urbano/urbano_20_group/urbano_20a'].split()
    respuestas_b = datos['group_consented/group_urbano/urbano_20_group/urbano_20b'].split()
    respuestas_c = datos['group_consented/group_urbano/urbano_20_group/urbano_20c'].split()
    respuestas_d = datos['group_consented/group_urbano/urbano_20_group/urbano_20d'].split()
    respuestas_e = datos['group_consented/group_urbano/urbano_20_group/urbano_20e'].split()
    respuestas_f = datos['group_consented/group_urbano/urbano_20_group/urbano_20f'].split()

    return mean([utils.normalize(int(respuestas_a[0]), 3, 1, 0, 100),
                 utils.normalize(int(respuestas_b[0]), 3, 1, 0, 100),
                 utils.normalize(int(respuestas_c[0]), 3, 1, 0, 100),
                 utils.normalize(int(respuestas_d[0]), 3, 1, 0, 100),
                 utils.normalize(int(respuestas_e[0]), 3, 1, 0, 100),
                 utils.normalize(int(respuestas_f[0]), 3, 1, 0, 100)])
