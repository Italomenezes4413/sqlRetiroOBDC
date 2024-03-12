import sqlRetiroODBC as sql
from icecream import ic
# get IP of de local machine
# informacoes = sql.informacoesMaquinas()
# informacoes = informacoes.getAllInfo()

 

# # Variáveis de exemplo
# a = 5
# b = 10
# c = "Olá, mundo!"

# # Use ic() para imprimir variáveis junto com seus nomes
# ic(a, b, c)

# # Você também pode usá-lo dentro de expressões
# resultado = a + b
# ic(resultado)

# # Ou mesmo em chamadas de função
# def multiplicar(x, y):
#     return x * y

# ic(multiplicar(a, b))



teste = sql.TratamentosInternos()
retorno = teste.setIP(320)
print(retorno)