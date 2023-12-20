# Dimensión Riesgo Desastres

# Documentos de referencia
# https://docs.google.com/spreadsheets/d/11sXtbYPi6ebDXrvFoHpA3qKGjS_OI4naNa0M4sXuFDY/edit#gid=1671296316
# https://kf.kobotoolbox.org/#/forms/aMbrw7VQcoKiZeRuEoJfCe/edit

import utils
from statistics import mean


# ------------------------------------------------------------
# Categoría: Hazards
# Subcategoría: Environmental
# Environmental degradation or physical or chemical pollution in the air, water and soil
# ------------------------------------------------------------
def d1(datos):
    ids = ["risdes_1",  # ola de calor
           "risdes_13",  # salinizacion
           "risdes_18",  # deforestacion
           "risdes_19",  # perdida de biodiversidad
           "risdes_20"  # incendios
           ]

    valores = []
    for i in ids:
        r = datos['group_consented/group_risdes/' + i].split()
        if "1" in r:
            ra = datos['group_consented/group_risdes/' + i + "a"].split()
            if "NA" not in ra:
                valores.append(utils.normalize(int(ra[0]), 3, 1, 0, 100))

    return mean(valores)


# ------------------------------------------------------------
# Categoría: Hazards
# Subcategoría: Geological
# Originate from internal earth processes
# ------------------------------------------------------------
def d2(datos):
    ids = ["risdes_4",  # terremoto
           "risdes_5",  # desertificacion
           "risdes_6",  # deslizamientos de tierra
           "risdes_7",  # erosion
           "risdes_8",  # tsunami
           "risdes_17",  # degradacion del suelo
           ]

    valores = []
    for i in ids:
        r = datos['group_consented/group_risdes/' + i].split()
        if "1" in r:
            ra = datos['group_consented/group_risdes/' + i + "a"].split()
            if "NA" not in ra:
                valores.append(utils.normalize(int(ra[0]), 3, 1, 0, 100))

    return mean(valores)


# ------------------------------------------------------------
# Categoría: Hazards
# Subcategoría: Hydrometeorological
# Atmospheric, hydrological or oceanographic origin
# ------------------------------------------------------------
def d3(datos):
    ids = ["risdes_2",  # inundacion
           "risdes_9",  # rayo
           "risdes_12",  # tormenta
           "risdes_15",  # tormenta de polvo
           "risdes_16"]  # granizo

    valores = []
    for i in ids:
        r = datos['group_consented/group_risdes/' + i].split()
        if "1" in r:
            ra = datos['group_consented/group_risdes/' + i + "a"].split()
            if "NA" not in ra:
                valores.append(utils.normalize(int(ra[0]), 3, 1, 0, 100))

    return mean(valores)


# ------------------------------------------------------------
# Categoría: Hazards
# Subcategoría: Biological
# Organic origin or conveyed by biological vectors, including pathogenic microorganisms, toxins and bioactive substances
# ------------------------------------------------------------
def d4(datos):
    ids = ["risdes_10"]  # enfermedad o plaga

    valores = []
    for i in ids:
        r = datos['group_consented/group_risdes/' + i].split()
        if "1" in r:
            ra = datos['group_consented/group_risdes/' + i + "a"].split()
            if "NA" not in ra:
                valores.append(utils.normalize(int(ra[0]), 3, 1, 0, 100))

    return mean(valores)


# ------------------------------------------------------------
# Categoría: Hazards
# Subcategoría: Anthropogenic
# Caused by human activities
# ------------------------------------------------------------
def d5(datos):
    ids = ["risdes_11",  # sustancias o residuos peligrosos
           "risdes_14"]  # contaminacion actividades humanas

    valores = []
    for i in ids:
        r = datos['group_consented/group_risdes/' + i].split()
        if "1" in r:
            ra = datos['group_consented/group_risdes/' + i + "a"].split()
            if "NA" not in ra:
                valores.append(utils.normalize(int(ra[0]), 3, 1, 0, 100))

    return mean(valores)


# ------------------------------------------------------------
# Categoría: Impacts
# Subcategoría: Exposure, vulnerability & damage
# Adverse observed impacts and/or projected risks of climate change. These impacts can be economic and/or non-economic
# ------------------------------------------------------------
def d6(datos):
    # Hay que calcular el promedio de todos los riesgos, da igual la dimension
    valores = []
    for i in range(1, 21):
        r = datos['group_consented/group_risdes/risdes_' + str(i)].split()
        if "1" in r:
            ra = datos['group_consented/group_risdes/risdes_' + str(i) + "b"].split()
            # Average rate of infrastructures without any damage in case of disasters (100% if "No" to all, 75% if 1
            #   is selected, 50% if 2 are selected, 25% if 3 are selected, 1% if 4-5 are selected)
            if len(ra) == 0:
                valores.append(100)
            if len(ra) == 1:
                valores.append(75)
            if len(ra) == 2:
                valores.append(50)
            if len(ra) == 3:
                valores.append(25)
            if len(ra) >= 4:
                valores.append(1)

    return mean(valores)


# ------------------------------------------------------------
# Categoría: Capacity
# Subcategoría: Responsiveness and Preparedness
# Perception of hazard preparedness and elements available to reduce the impact of hazards
# ------------------------------------------------------------
def d7(datos):
    return mean([mean([d7a(datos), d7b(datos)]), d7c(datos)])


def d7a(datos):
    r = datos['group_consented/group_risdes/risdes_22'].split()
    return utils.normalize(int(r[0]), 1, 3, 0, 100)


def d7b(datos):
    r = datos['group_consented/group_risdes/risdes_23'].split()
    return utils.normalize(int(r[0]), 1, 3, 0, 100)


def d7c(datos):
    r = datos['group_consented/group_risdes/risdes_24'].split()
    return utils.normalize(len(r), 0, 9, 0, 100)
