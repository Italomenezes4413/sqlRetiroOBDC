import pyodbc
import mysql.connector as mysql

class Credentials():
    def __init__(self) -> None:
        self.__server = None
        self.__database = None
        self.__password = None
        self.__username = None
        self.__command = None
        self.__portNumber = '1433'



class ServerRetiroPbs(Credentials):
    def __init__(self) -> None:
        self.__connectionString = None
        self.__cursor = None
        self.__return = None
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
    def getUserValidation(self):
        self.__connectionString = f'DRIVER={{SQL Server}};SERVER={self.__server},{self.__portNumber};DATABASE={self.__database};UID={self.__username};PWD={self.__password}'
        self.__conn = pyodbc.connect(self.__connectionString)
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute(self.__command)
        teste = self.__cursor.fetchall()
        print(teste)

        if len(teste)>0 :
            return True
        
        else:
            return False



class serverGlpi(Credentials):

    def __init__(self) -> None:
        self.__ticket = None
        self.__groupTicket = None
        self.__solveDate = None
        self.__server = None
        
        
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
    
    
    def getTicket(self,ticket):
        self.__ticket = ticket

    def returnGLPI(self):
        conexao = mysql.connect(host=self.__server, database=self.__database, user=self.__username, password=self.__password)
        cursor = conexao.cursor()
        cursor.execute(self.__command)
        retorno = cursor.fetchall()[0][0]
        if retorno != None:
            return True
        elif retorno =='':
            return False
        else:
            return False