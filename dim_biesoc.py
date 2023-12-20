# Dimensión Bienestar Social

# Documentos de referencia
# https://docs.google.com/spreadsheets/d/11sXtbYPi6ebDXrvFoHpA3qKGjS_OI4naNa0M4sXuFDY/edit#gid=1671296316
# https://kf.kobotoolbox.org/#/forms/aMbrw7VQcoKiZeRuEoJfCe/edit

import utils
from statistics import mean


# ------------------------------------------------------------
# Categoría: Economic conditions & opportunities
# Subcategoría: Employment & Entrepeneurship
# Employment levels and quality (e.g.: formal vs informal), as well as income levels, together with locally owned
#   businesses in the area
# ------------------------------------------------------------
def c1(datos):
    return _c1a(datos)


def _c1a(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_5'].split()
    if "1" in respuestas:  # Sector formal
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Economic conditions & opportunities
# Subcategoría: Affordability
# People´s capacity to afford basic services according to their wages
# ------------------------------------------------------------
def c2(datos):
    respuestas_a = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13a'].split()
    respuestas_b = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13b'].split()
    respuestas_c = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13c'].split()
    respuestas_d = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13d'].split()
    respuestas_e = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13e'].split()
    respuestas_f = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13f'].split()
    respuestas_g = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13g'].split()
    respuestas_h = datos['group_consented/group_biesoc/biesoc_13_group/biesoc_13h'].split()

    return mean([utils.normalize(int(respuestas_a[0]), 1, 3, 0, 100),
                 utils.normalize(int(respuestas_b[0]), 1, 3, 0, 100),
                 utils.normalize(int(respuestas_c[0]), 1, 3, 0, 100),
                 utils.normalize(int(respuestas_d[0]), 1, 3, 0, 100),
                 utils.normalize(int(respuestas_e[0]), 1, 3, 0, 100),
                 utils.normalize(int(respuestas_f[0]), 1, 3, 0, 100),
                 utils.normalize(int(respuestas_g[0]), 1, 3, 0, 100),
                 utils.normalize(int(respuestas_h[0]), 1, 3, 0, 100)])


# ------------------------------------------------------------
# Categoría: Education
# Subcategoría: Education
# Adults and children pursued / are pursuing a level of education that allows them to have better opportunities
# ------------------------------------------------------------
def c3(datos):
    respuestas_a = datos['group_consented/group_biesoc/biesoc_17'].split()  # edad
    respuestas_b = datos['group_consented/group_biesoc/biesoc_18'].split()  # estudios

    if int(respuestas_a[0]) >= 2 and int(respuestas_b[0]) >= 4:  # Mayores de 18 que erminaron bachillerato o más
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Education
# Subcategoría: Digitalización
# Access to internet and IT devices (smartphones, computers, etc)
# ------------------------------------------------------------
def c4(datos):
    return mean([_c4a(datos), _c4b(datos)])


def _c4a(datos):
    respuestas_a = datos['group_consented/group_biesoc/biesoc_4_group/biesoc_4a'].split()
    respuestas_b = datos['group_consented/group_biesoc/biesoc_4_group/biesoc_4b'].split()
    respuestas_c = datos['group_consented/group_biesoc/biesoc_4_group/biesoc_4c'].split()
    respuestas_d = datos['group_consented/group_biesoc/biesoc_4_group/biesoc_4d'].split()
    respuestas_e = datos['group_consented/group_biesoc/biesoc_4_group/biesoc_4e'].split()

    existe_f = 'group_consented/group_biesoc/biesoc_4_group/biesoc_4f' in datos
    respuestas_f = (
        datos['group_consented/group_biesoc/biesoc_4_group/biesoc_4f'].split() if existe_f else
        None
    )

    if existe_f:
        return mean([utils.normalize(int(respuestas_a[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_b[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_c[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_d[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_e[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_f[0]), 0, 3, 0, 100)])
    else:
        return mean([utils.normalize(int(respuestas_a[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_b[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_c[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_d[0]), 0, 3, 0, 100),
                     utils.normalize(int(respuestas_e[0]), 0, 3, 0, 100),])


def _c4b(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_3'].split()
    if "1" in respuestas:  # tiene celular
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Human Development and Inclusion
# Subcategoría: Social assistance and care system
# Vulnerable groups that benefit from social assistance programs (e.g.: pension, subsidies for single mothers, public
#   nurseries, etc.)
# ------------------------------------------------------------
def c5(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_10'].split()
    if "1" in respuestas:  # es beneficiario
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Human Development and Inclusion
# Subcategoría: Poverty
# ------------------------------------------------------------
def c6(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_12'].split()
    if "APENAS_CUBRE" in respuestas or "CUBRE" in respuestas or "CUBRE_HOLGADAMENTE" in respuestas:
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Health & Wellbeing
# Subcategoría: Health
# Health status according to the suffering of diseases and the access to quality essential health-care services
# ------------------------------------------------------------
def c7(datos):
    return mean([_c7a(datos), _c7b(datos)])


def _c7a(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_8'].split()
    return utils.normalize(int(respuestas[0]), 0, 4, 0, 100)


def _c7b(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_7'].split()
    if "1" in respuestas or "2" in respuestas:
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Health & Wellbeing
# Subcategoría: Food systems
# Food security that ensures access a healthy access to food, both in quantity and quality
# ------------------------------------------------------------
def c8(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_14'].split()
    return utils.normalize(int(respuestas[0]), 1, 5, 0, 100)


# ------------------------------------------------------------
# Categoría: Community engagement & participation
# Subcategoría: Culture and identity
# Availability of accesible social and cultural activities  in the neighbourhood
# ------------------------------------------------------------
def c9(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_1'].split()
    if "2" in respuestas or "3" in respuestas or "4" in respuestas:
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Community engagement & participation
# Subcategoría: Community engagement
# Community engagement level and inclusive participation processes for decision making processes in the neighbourhood
# ------------------------------------------------------------
def c10(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_2'].split()
    if (len(respuestas) >= 1) and ("0" not in respuestas):
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Gender Equity
# Subcategoría: Care distribution
# Time use in care responsibilities in mobility and private sphere
# ------------------------------------------------------------
def c11(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_15_group/biesoc_15a'].split()
    if len(respuestas) == 1 and "3" in respuestas:
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Gender Equity
# Subcategoría: Socio economic conditions
# Differences in multiple dimensions that ensure economic autonomy
# ------------------------------------------------------------
def c12(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_15_group/biesoc_15b'].split()
    if len(respuestas) == 1 and "3" in respuestas:
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Gender Equity
# Subcategoría: Safety and security aspects
# Ensurance of physical autonomy in terms of safety and security
# ------------------------------------------------------------
def c13(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_15_group/biesoc_15c'].split()
    if len(respuestas) == 1 and "3" in respuestas:
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Gender Equity
# Subcategoría: Participation
# Ensurance of decision-making autonomy
# ------------------------------------------------------------
def c14(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_15_group/biesoc_15d'].split()
    if len(respuestas) == 1 and "3" in respuestas:
        return 100
    return 0


# ------------------------------------------------------------
# Categoría: Gender Equity
# Subcategoría: Climate change impacts
# Decrease women vulnerability to the effects of climate change
# ------------------------------------------------------------
def c15(datos):
    respuestas = datos['group_consented/group_biesoc/biesoc_15_group/biesoc_15e'].split()
    if len(respuestas) == 1 and "3" in respuestas:
        return 100
    return 0
