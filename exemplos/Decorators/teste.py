# "Criador" de funções de potência
'''
def cria_potencia(x):
    def potencia(num):
        return x ** num
    return potencia

# Potência de 2 e 3
potencia_2 = cria_potencia(2)
potencia_3 = cria_potencia(3)

# Resultado
print(potencia_2(2))
print(potencia_3(2))

# função passada como argumento de outra função
def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()
'''

import time
# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )
    return wrapper

#função sem o decoratorr(@)
def main_sem_arroba():
    for n in range(0, 10000000):
        pass

# Decora a função com o decorator @
@calcula_duracao
def main_com_arroba():
    for n in range(0, 10000000):
        pass

# Executa a função main
func_dec = calcula_duracao(main_sem_arroba)
func_dec()

main_com_arroba()


