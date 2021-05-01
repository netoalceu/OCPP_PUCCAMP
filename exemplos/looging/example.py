import logging

import output as output

logger = logging.getLogger('Program Name-Version')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

consoleHeader = logging.StreamHandler()
consoleHeader.setFormatter(formatter)
consoleHeader.setLevel(logging.INFO)

fileHandler = logging.FileHandler(f"{output}/metabcc-lr.log")
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(consoleHeader)


#Logs criados para testar os niveis de log
logger.debug('Info de depuracao para devs')

logger.info('Info, nada grave.')

logger.warning('Avisos aos usuarios sobre entradas, parametros, etc.')

logger.error('Relata um erro causado por algo que o usuario ou no sistema.')

logger.critical('Deu merda feia....')

print("This is the program output") #Saida padrão(stdout)
