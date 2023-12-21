import random
from datetime import datetime
from testeClimate import *
from lista import *
from jogos import *
from multiprocessing.pool import ThreadPool

inicio = datetime.now()
jogos = []
toplist1 = list(toplist)
listaTodosJogos1 = list(listaTodosJogos)

def aposta(tamJogos):

    numbers = []
    cidades = ['Berlin', 'Tokyo', 'Nairobi', 'Rio de Janeiro', 'Denver', 'Moscou', 'Helsinki', 'Lisboa', 'Palermo']
    cidade = ''
    seed = ''
    
    while(len(numbers) < tamJogos):
        cidade = cidades[random.randint(0, len(cidades)-1)]
        seed = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f%f%f%f%f '))+str(cidade)+' '+str(paraCidade(cidade))
        random.seed(seed)
        number = random.choice(toplist)
        if number not in numbers:
            numbers.append(number)
        if len(numbers) == tamJogos:
            numbers.sort()
            if tuple(numbers) not in listaTodosJogos1:
                jogos.append((numbers))
                listaTodosJogos1.append(tuple(numbers))
                #print(listaTodosJogos1)
            else:
                number = []

def loop(qntNumeros, qntJogos):
    for i in range(0, qntJogos):
        aposta(qntNumeros)
    return True

tamJogos = [(6,10), (6,10), (6,10), (6,10), (6,13),(7,1),(8,2),(11,1)]

pool = ThreadPool(processes=4)
threads = []       
for games in tamJogos:
    async_result = pool.apply_async(loop, games)
    threads.append(async_result)
letters_list = []
for result in threads:
    try:
        letters_list.append(result.get(timeout=90))
    except Exception as e:
        print(e)         

with open('sorteados.txt', 'w') as file:
    for jogo in jogos:
        #print(jogo)
        file.write(str(jogo))
        file.write('\n')

fim = datetime.now()

print(fim - inicio)

