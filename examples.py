import sqlRetiroODBC as sql
from icecream import ic
# get IP of de local machine
# informacoes = sql.informacoesMaquinas()
# informacoes = informacoes.getAllInfo()


sqlServer = sql.SqlServer()
sqlServer.setUser('USER')
sqlServer.setPassword('PASSWORD')
sqlServer.setDatabase('MY_DATABASE')
sqlServer.setServer('192.168.10.15')

command = """select top 1 from orders"""

sqlServer.setCommand(command)
returnDataBase = sqlServer.stringPBS()

print(returnDataBase) # query result