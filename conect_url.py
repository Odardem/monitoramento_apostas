import requests
import json
import os
from datetime import datetime, timedelta
from secrets import *

def get_token(url_test, query_test):
    corr_hour = timedelta(hours=5)
    diretorio = os.getcwd()
    check_expiration = open(fr'{diretorio}\expiration.txt','r')
    data_atual = datetime.now()
    conversion_data_exp = check_expiration.read()
    data_expiracao_inicial = datetime.strptime(conversion_data_exp, "%Y-%m-%dT%H:%M:%SZ")
    data_expiracao = data_expiracao_inicial - corr_hour
    token_check = open(fr'{diretorio}\token.txt','r')
    token_valido = token_check.read()
    r2 = requests.post(url_test, json={'query': query_test},headers={"authorization":f"Bearer {token_valido}"})
    if data_expiracao < data_atual or token_valido == "" or r2.status_code != 200:                              # Checa conexão 
        token = requests.post(URL_TOKEN, json={'query': AUTHENTICATION})
        token_jason = json.loads(token.text)
        token = token_jason['data']['createToken']['token']
        token_txt = open(fr'{diretorio}\token.txt',"w")
        token_txt.write(token)
        token_txt.close
        expiration = token_jason['data']['createToken']['expiration']
        expiration_txt = open(fr'{diretorio}\expiration.txt',"w")
        expiration_txt.write(expiration)
        expiration_txt.close
    else:
        token = token_valido
    return token

if __name__ == '__main__':
    get_token()
