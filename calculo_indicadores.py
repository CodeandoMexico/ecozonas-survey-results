import json
import dim_enturb
import dim_medamb
import dim_biensoc
import dim_risdes


def cargar_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def calcular_indicadores(json_data):
    print(dim_risdes.d7(json_data))


def main():
    file_path = 'data/test.json'
    json_data = cargar_json(file_path)
    print(json_data['start'])
    calcular_indicadores(json_data)


if __name__ == "__main__":
    main()
