# Monitoramento de Apostas

Script utilizado para consumir api graphql e retornar numeros de apostas. O mesmo é executado no zabbix para monitoramento minuto a minuto de apostas

## Instalação

É gerado um executavel atraves do PyInstaller, que será utilizado pelo zabbix.
colocar o arquivo na pasta

```bash

```

## Uso

Podem ser passados até 2 parametros, o primeiro referente ao retorno de informações e o segundo referente ao horario:

```bash


./monitoramento todos True
# returns list
#[quantidade_bets, quantidade_free_bets, quantidade_vivo, quantidade_prematch, 
# quantidade_mixed, status_cancelado,status_cashed_out, status_lost, status_open, status_paid]
[121, 8, 16, 103, 2, 0, 0, 0, 121, 0]

.\monitoramento.py bets True
# returns 'bets':
# int
121

.\monitoramento.py free True
# returns 'free':
# int
8

.\monitoramento.py vivo True
# returns 'vivo':
# int
16

.\monitoramento.py prematch True
# returns 'prematch':
# int
103

.\monitoramento.py mixed True 
# returns 'mixed':
# int
2

```

## License

[MIT](https://choosealicense.com/licenses/mit/)