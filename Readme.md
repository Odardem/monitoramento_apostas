# Monitoramento de Apostas

Script utilizado para consumir api graphql e retornar numeros de apostas. O mesmo é executado no zabbix para monitoramento minuto a minuto de apostas

## Instalação

É gerado um executavel atraves do PyInstaller, que será utilizado pelo zabbix.
colocar o arquivo na pasta

```bash

```

## Uso

```bash


./monitoramento todos True
# returns "todos"
#[quantidade_bets, quantidade_free_bets, quantidade_vivo, quantidade_prematch, 
# quantidade_mixed, status_cancelado,status_cashed_out, status_lost, status_open, status_paid]
[121, 8, 16, 103, 2, 0, 0, 0, 121, 0]

.\monitoramento.py bets True
# returns 'bets':
# quantidade_bets
121

.\monitoramento.py free True
# returns 'free':
# quantidade_free_bets
8

.\monitoramento.py vivo True
# returns 'vivo':
# quantidade_vivo
16

.\monitoramento.py prematch True
# returns 'prematch':
# quantidade_prematch
103

.\monitoramento.py mixed True 
# returns 'mixed':
# quantidade_mixed
2

```

## License

[MIT](https://choosealicense.com/licenses/mit/)