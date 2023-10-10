import pandas as pd
from time import sleep
try:
    df = pd.read_json('dados.json') # abre o arquivo
    print('Arquivo dados.csv encontrado...')
    sleep(1) # espera 1 segundo
    print(f'Processando {len(df)} registros...') 
    sleep(1)
    df.to_csv('novos_dados.csv', encoding='utf-8', index=False) # converte o arquivo e salva
    sleep(1)
    print('Arquivo novos_dados.cvs gerado com sucesso!')
except FileNotFoundError:
    print('Erro... Arquivo não encontrado!')