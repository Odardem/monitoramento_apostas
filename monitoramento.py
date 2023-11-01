import requests
import json
import conect_url
from datetime import datetime,date,timedelta
import sys
from collections import Counter
from options import *



def bets_att(data,query,url,token,tempo, datainformada):
    query_teste = query.replace("xxxx-xx-xx", data)
    r2 = requests.post(url, json={'query': query_teste},headers={"authorization":f"Bearer {token}"})
    if r2.status_code != 200:
        token = conect_url.get_token(url,query_teste)
        r2 = requests.post(url, json={'query': query_teste},headers={"authorization":f"Bearer {token}"})
    json_data2 = json.loads(r2.text)
    bets_banco = json_data2['data']['bets']
    lista_id_hora=[(a['product'],a['isFreeBet'],a['state']) for a in bets_banco
                    if a['createdAt'][11:16] == tempo and a['createdAt'][:10] == datainformada]
    return lista_id_hora

def type_bets(lista:list):
    status_bets = Counter(bet_state[2] for bet_state in lista)
    numero_freebet = Counter(freebet[1] for freebet in lista)
    produto_mixed = Counter(len(mixed[0]) for mixed in lista if len(mixed[0]) > 1)
    tipo_produto = Counter(type_product[0][0] for type_product in lista if len(type_product[0]) == 1)
    retorno = status_bets + numero_freebet + tipo_produto + produto_mixed

    return retorno
    
def numero_bets(bets:str,verao:bool=False):
    horario_viena = timedelta(hours=5)
    if verao:
            horario_viena = timedelta(hours=3)
    minuto = 1
    ultimo_minuto = timedelta(minutes=minuto)
    data_hora_atual = datetime.now()
    hora_atual = data_hora_atual.time()
    ultimo_datetime_viena = data_hora_atual + horario_viena - ultimo_minuto
    ultimo_minuto_viena = datetime.strftime(ultimo_datetime_viena, '%H:%M')
    data_atual = str(date.today())
    limite_dia_brasil_viena = datetime.strptime('19:00','%H:%M')
    if hora_atual > limite_dia_brasil_viena.time():
        data_atual = str(date.today() + timedelta(days=1))
    bets_hoje = bets_att(data_atual, QUERY_BETS, URL_BETS, token_bet, ultimo_minuto_viena,data_atual)
    type_of_bets = type_bets(bets_hoje)
    quantidade_bets = len(bets_hoje)
    quantidade_free_bets = type_of_bets[True]
    quantidade_vivo =  type_of_bets['LIVE']
    quantidade_prematch =  type_of_bets['PRE_MATCH']
    quantidade_mixed =  type_of_bets[2]
    status_cancelado =  type_of_bets['CANCELLED']
    status_cashed_out =  type_of_bets['CASHED_OUT']
    status_lost =  type_of_bets['LOST']
    status_open =  type_of_bets['OPEN']
    status_paid =  type_of_bets['PAID']
    
    if bets == 'todos':
        todos_resultados = [quantidade_bets, quantidade_free_bets, quantidade_vivo, 
                            quantidade_prematch, quantidade_mixed, status_cancelado, 
                            status_cashed_out, status_lost, status_open, status_paid]
        return todos_resultados
    elif bets == 'bets':
        return quantidade_bets
    elif bets == 'free':
        return quantidade_free_bets
    elif bets == 'vivo':
        return quantidade_vivo
    elif bets == 'prematch':
        return quantidade_prematch
    elif bets == 'mixed':
        return quantidade_mixed
    
    
if __name__ == '__main__':

    token_bet = conect_url.get_token(URL_BETS,QUERY_BETS)
    token_transactions = conect_url.get_token(URL_TRANSACTIONS,QUERY_TRANSACTIONS)
    #print(sys.argv[1],type(sys.argv[2]))
    print(numero_bets(sys.argv[1],bool(sys.argv[2])))