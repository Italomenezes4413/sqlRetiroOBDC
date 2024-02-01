import sqlRetiroODBC as sql

# get IP of de local machine
informacoes = sql.informacoesMaquinas()
informacoes = informacoes.getAllInfo()

print(informacoes['hostname'])
print(informacoes['date'])
print(informacoes['ip'])
