import pyodbc
import mysql.connector as mysql
from datetime import datetime
import socket 


class SqlServer():
    def __init__(self) -> None:
        self.__connectionString = None
        self.__cursor = None
        self.__portNumber = '1433'

    #Configuração Conexão
    def setServer(self, server):
        
        self.__server = server

    def setUser(self, user):
        self.__username = user

    def setDatabase(self, database):
        self.__database = database
    
    def setPassword(self, password):
        self.__password = password

    def setCommand(self, command):
        self.__command = command 

    #Retornos conexão
    def getValidation(self):
        self.__connectionString = f'DRIVER={{SQL Server}};SERVER={self.__server},{self.__portNumber};DATABASE={self.__database};UID={self.__username};PWD={self.__password}'
        self.__conn = pyodbc.connect(self.__connectionString)
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute(self.__command)
        usuario = self.__cursor.fetchall()
        

        if usuario:
            retornoBanco = usuario[0][0]
            return retornoBanco
        else:
            return False         
        
    def stringPBS(self):
        self.__connectionString = f'DRIVER={{SQL Server}};SERVER={self.__server},{self.__portNumber};DATABASE={self.__database};UID={self.__username};PWD={self.__password}'
        self.__conexao = pyodbc.connect(self.__connectionString)
        cursor = self.__conexao.cursor()
        cursor.execute(self.__command)
        resultado = cursor.fetchall()
        
        return resultado
    
    def insertPBS(self):
        print('inicio conexão banco de dados SQL Server BD_Python')
        self.__connectionString = f'DRIVER={{SQL Server}};SERVER={self.__server},{self.__portNumber};DATABASE={self.__database};UID={self.__username};PWD={self.__password}'
        self.__conexao = pyodbc.connect(self.__connectionString)
        cursor = self.__conexao.cursor()
        cursor.execute(self.__command)
        cursor.commit()
        



class MysqlServer():

    def __init__(self) -> None:
        self.__username = None
        self.__password = None
        self.__server = None
        self.__database =None
        self.__command= None
        
        
        
    def setServer(self, server):
        self.__server = server

    def setUser(self, usuario):
        self.__username = usuario
    
    def setPassword(self, password):
        self.__password = password
    
    def setDatabase(self, database):
        self.__database = database 
    
    def setCommand(self, command):
        self.__command=command


    def stringGLPI(self):
        conexao = mysql.connect(host=f'{self.__server}', database=f'{self.__database}',user=f'{self.__username}', password=f'{self.__password}')
        cursor = conexao.cursor()
        cursor.execute(self.__command)
        retorno = cursor.fetchall()
        print(retorno)
        if retorno:
            retornoBanco = retorno[0][0]
            return retornoBanco
        else:
            return False


'''
proximas classes e funções para pegar informações da máquinas
importante na geração de logs de usuários e/ou locais de envio de comandos
Serão acrescentadas maiores funcionalidades na biblioteca
'''

class informacoesMaquinas():           
    def __init__(self):
        self.__teste = None
        self.__ip = None
    
    def getIp(self):
        '''
        tem que passar o getHostName primeiro para buscar alimentar a variável e depois executar a segunda.
        '''
        hostName = socket.gethostname()
        ip = socket.gethostbyname(hostName)
        
        return ip

    
    def getAllInfo(self):
        hostName = socket.gethostname()
        ip = socket.gethostbyname(hostName)
        data = datetime.now()
        dataForm = data.strftime("%d%m%Y")
        dic = {'ip': ip,'hostname': hostName,'date':dataForm}
        return dic

