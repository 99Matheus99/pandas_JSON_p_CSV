import pandas as pd
from time import sleep
try:
    df = pd.read_json('dados.json')
    print('Arquivo dados.csv encontrado...')
    sleep(1)
    print(f'Processando {len(df)} registros...')
    sleep(1)
    df.to_csv('novos_dados.csv', encoding='utf-8', index=False)
    sleep(1)
    print('Arquivo novos_dados.cvs gerado com sucesso!')
except FileNotFoundError:
    print('Erro... Arquivo não encontrado!')