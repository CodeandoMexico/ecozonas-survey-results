import json
import os
import csv
import pandas as pd

import dim_enturb
import dim_medamb
import dim_biesoc
import dim_risdes


def cargar_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def calcular_indicadores(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    calculos = []

    for file in files:
        json_data = cargar_json(path + "/" + file)

        if json_data['introduccion/consentimiento'] == '0':  # No dio consentimiento, no se procesa
            continue

        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a1', 'puntuacion': dim_enturb.a1(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a2', 'puntuacion': dim_enturb.a2(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a3', 'puntuacion': dim_enturb.a3(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a4', 'puntuacion': dim_enturb.a4(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a5', 'puntuacion': dim_enturb.a5(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a6', 'puntuacion': dim_enturb.a6(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a7', 'puntuacion': dim_enturb.a7(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a8', 'puntuacion': dim_enturb.a8(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a9', 'puntuacion': dim_enturb.a9(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a10', 'puntuacion': dim_enturb.a10(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a11', 'puntuacion': dim_enturb.a11(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a12', 'puntuacion': dim_enturb.a12(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a13', 'puntuacion': dim_enturb.a13(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a14', 'puntuacion': dim_enturb.a14(json_data)})
        calculos.append({'dimension': 'Entorno urbano', 'indicador': 'a15', 'puntuacion': dim_enturb.a15(json_data)})

        calculos.append({'dimension': 'Medio ambiente', 'indicador': 'b1', 'puntuacion': dim_medamb.b1(json_data)})
        calculos.append({'dimension': 'Medio ambiente', 'indicador': 'b2', 'puntuacion': dim_medamb.b2(json_data)})
        calculos.append({'dimension': 'Medio ambiente', 'indicador': 'b3', 'puntuacion': dim_medamb.b3(json_data)})
        calculos.append({'dimension': 'Medio ambiente', 'indicador': 'b4', 'puntuacion': dim_medamb.b4(json_data)})
        calculos.append({'dimension': 'Medio ambiente', 'indicador': 'b5', 'puntuacion': dim_medamb.b5(json_data)})
        calculos.append({'dimension': 'Medio ambiente', 'indicador': 'b6', 'puntuacion': dim_medamb.b6(json_data)})
        calculos.append({'dimension': 'Medio ambiente', 'indicador': 'b7', 'puntuacion': dim_medamb.b7(json_data)})
        # Bienestar social
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c1', 'puntuacion': dim_biesoc.c1(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c2', 'puntuacion': dim_biesoc.c2(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c3', 'puntuacion': dim_biesoc.c3(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c4', 'puntuacion': dim_biesoc.c4(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c5', 'puntuacion': dim_biesoc.c5(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c6', 'puntuacion': dim_biesoc.c6(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c7', 'puntuacion': dim_biesoc.c7(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c8', 'puntuacion': dim_biesoc.c8(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c9', 'puntuacion': dim_biesoc.c9(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c10', 'puntuacion': dim_biesoc.c10(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c11', 'puntuacion': dim_biesoc.c11(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c12', 'puntuacion': dim_biesoc.c12(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c13', 'puntuacion': dim_biesoc.c13(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c14', 'puntuacion': dim_biesoc.c14(json_data)})
        calculos.append({'dimension': 'Bienestar social', 'indicador': 'c15', 'puntuacion': dim_biesoc.c15(json_data)})
        # Riesgo desastres
        for riesgo in dim_risdes.d0(json_data):
            print(riesgo)
            calculos.append({
                'dimension': 'Riesgo desastres',
                'indicador': 'd0',
                'riesgo': riesgo['nombre_riesgo'],
                'puntuacion': riesgo['puntuacion']
            })
        calculos.append({'dimension': 'Riesgo desastres', 'indicador': 'd1', 'puntuacion': dim_risdes.d1(json_data)})
        calculos.append({'dimension': 'Riesgo desastres', 'indicador': 'd2', 'puntuacion': dim_risdes.d2(json_data)})
        calculos.append({'dimension': 'Riesgo desastres', 'indicador': 'd3', 'puntuacion': dim_risdes.d3(json_data)})
        calculos.append({'dimension': 'Riesgo desastres', 'indicador': 'd4', 'puntuacion': dim_risdes.d4(json_data)})
        calculos.append({'dimension': 'Riesgo desastres', 'indicador': 'd5', 'puntuacion': dim_risdes.d5(json_data)})
        calculos.append({'dimension': 'Riesgo desastres', 'indicador': 'd6', 'puntuacion': dim_risdes.d6(json_data)})
        calculos.append({'dimension': 'Riesgo desastres', 'indicador': 'd7', 'puntuacion': dim_risdes.d7(json_data)})

    return calculos


def guardar_csvs(encuesta, calculos):
    csv_file_path = 'data/export/calculos_' + encuesta + '.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        nombre_columnas = ['dimension', 'indicador', 'riesgo', 'puntuacion']
        print(nombre_columnas)
        csv_writer = csv.DictWriter(csv_file, fieldnames=nombre_columnas)
        csv_writer.writeheader()
        csv_writer.writerows(calculos)


def calcular_resultados(encuesta):
    csv_file_path = 'data/export/calculos_' + encuesta + '.csv'
    df = pd.read_csv(csv_file_path)
    df = df.dropna(subset=['puntuacion'])
    resultados = df.groupby(['dimension', 'indicador',])['puntuacion'].mean().reset_index()
    resultados = resultados.sort_values(by=['dimension', 'puntuacion'])
    resultados['puntuacion'] = resultados['puntuacion'].astype(int)
    resultados_file_path = 'data/export/resultados_' + encuesta + '.csv'
    resultados.to_csv(resultados_file_path, index=False)

    resultados_riesgos = df.groupby(['dimension', 'indicador', 'riesgo'])['puntuacion'].mean().reset_index()
    resultados_riesgos = resultados_riesgos.sort_values(by=['dimension', 'puntuacion'])
    resultados_riesgos['puntuacion'] = resultados_riesgos['puntuacion'].astype(int)
    resultados_riesgos_file_path = 'data/export/resultados_riesgos_' + encuesta + '.csv'
    resultados_riesgos.to_csv(resultados_riesgos_file_path, index=False)


def main():
    encuestas = [
        'leon',
        'hermosillo'
    ]
    for encuesta in encuestas:
        calculos = calcular_indicadores('data/' + encuesta)
        guardar_csvs(encuesta, calculos)
        calcular_resultados(encuesta)


if __name__ == "__main__":
    main()
