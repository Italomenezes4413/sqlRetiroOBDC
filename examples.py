import sqlRetiroODBC as sql
from icecream import ic
# get IP of the local machine
# info = sql.informacoesMaquinas()
# info = informacoes.getAllInfo()

db = sql.SqlServer('192.168.0.1','PBS_RETIRO_DADOS','SA_PRECO','R3T1R0@2020')

query = """ select nome from usuarios where usuario = 1120"""
db.setCommand(query)

resulta = db.stringPBS()

print(resulta)