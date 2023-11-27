import json
import dim_enturb

def cargar_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def calcular_indicadores(json_data):
    print(dim_enturb.enturb_p12(json_data))


def main():
    file_path = 'data/leon_f437caa7-0e46-47de-9a6b-cb8b42f902b9.json'
    json_data = cargar_json(file_path)
    print(json_data['start'])
    calcular_indicadores(json_data)


if __name__ == "__main__":
    main()
