import logging

logging.basicConfig(level=logging.CRITICAL)  # Somente na saida de erro padrao (stderr)


#logging.basicConfig(filename='program.log', filemode='a', level=logging.DEBUG)  # Criando um arquivo de LOG




logging.debug('Info de depuracao para devs')

logging.info('Informativo, nada grave.')

logging.warning('Avisos aos usuarios sobre entradas, parametros, etc.')

logging.error('Relata um erro causado por algo que o usuario ou no sistema.')

logging.critical('Deu merda feia....')

print("This is the program output") #Saida padrão(stdout)
