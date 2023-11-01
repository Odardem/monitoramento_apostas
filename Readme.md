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

# returns
[121, 8, 16, 103, 2, 0, 0, 0, 121, 0]

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)