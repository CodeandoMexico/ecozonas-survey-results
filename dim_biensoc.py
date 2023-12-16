# Dimensión Bienestar Social

# Documentos de referencia
# https://docs.google.com/spreadsheets/d/11sXtbYPi6ebDXrvFoHpA3qKGjS_OI4naNa0M4sXuFDY/edit#gid=1671296316
# https://kf.kobotoolbox.org/#/forms/aMbrw7VQcoKiZeRuEoJfCe/edit

import utils


# ------------------------------------------------------------
# Categoría: Economic conditions & opportunities
# Subcategoría: Employment & Entrepeneurship
# Employment levels and quality (e.g.: formal vs informal), as well as income levels, together with locally owned
#   businesses in the area
# ------------------------------------------------------------
def c1(datos):
    return c1a(datos)


def c1a(datos):
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

    return (
            utils.normalize(int(respuestas_a[0]), 1, 3, 0, 100) +
            utils.normalize(int(respuestas_b[0]), 1, 3, 0, 100) +
            utils.normalize(int(respuestas_c[0]), 1, 3, 0, 100) +
            utils.normalize(int(respuestas_d[0]), 1, 3, 0, 100) +
            utils.normalize(int(respuestas_e[0]), 1, 3, 0, 100) +
            utils.normalize(int(respuestas_f[0]), 1, 3, 0, 100) +
            utils.normalize(int(respuestas_g[0]), 1, 3, 0, 100) +
            utils.normalize(int(respuestas_h[0]), 1, 3, 0, 100)
    ) / 8
