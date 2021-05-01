import logging

# Criando um nome que sera chamado em qualquer lugar do programa
logger = logging.getLogger("My Logger")
#Setando um nivel de registro GLOBAL.
logger.setLevel(logging.DEBUG)

#Criando o manipulador para as msgs em tela
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL) # Niveis diferente de Registro

#Criando o manipulador para as msgs em arquivo
file_handler = logging.FileHandler('file.log', mode='a')
file_handler.setLevel(logging.DEBUG) # Niveis diferente de Registro

#Configurando o Formato dos LOGS
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# adicionando os manipuladores de registro no logger GLOBAL
logger.addHandler(console_handler)
logger.addHandler(file_handler)



#Logs criados para testar os niveis de log
logger.debug('Info de depuracao para devs')

logger.info('Info, nada grave.')

logger.warning('Avisos aos usuarios sobre entradas, parametros, etc.')

logger.error('Relata um erro causado por algo que o usuario ou no sistema.')

logger.critical('Deu merda feia....')

print("This is the program output") #Saida padrão(stdout)
