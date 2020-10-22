import json

import pandas as pd
import plotly.express as px
import requests as r

from environment_variables import MULLER_MAP_BACKEND

def get_chart_data():
    try:
        df_exists, df = get_data_from_backend()
        if not df_exists:
            df = get_data_from_last_backup()
        return df
    except:
        raise


def get_data_from_backend():
    try:
        request = r.get(f'{MULLER_MAP_BACKEND}/coordenadas')
        if request.status_code == 200:
            lista_coordenadas = request.json()
            dump_lista=json.dumps(lista_coordenadas)
            df_coordenadas = pd.read_json(dump_lista)
            df_coordenadas['nome_usuario'] = df_coordenadas['id_usuario'].apply(lambda x: x.get('usuario'))
            df_coordenadas.rename(
                columns={'indice_radiacao': 'Radiation Level (mR/h)', 'nm_local': 'Local', 'nome_usuario': 'User'},
                inplace=True)
            df_coordenadas['lat'] = df_coordenadas['lat'].astype(dtype='float64')
            df_coordenadas['lon'] = df_coordenadas['lon'].astype(dtype='float64')
            return True, df_coordenadas
        else:
            return False, None

    except:
        raise


def get_data_from_last_backup():
    data = pd.read_excel('data/botucatu_radiation_latlong.xlsx')
    df = pd.DataFrame(data)

    df[['lat', 'lon']] = df['lat-long'].str.split(',', expand=True)

    df['lat'] = df['lat'].astype(dtype='float64')
    df['lon'] = df['lon'].astype(dtype='float64')

    return df
