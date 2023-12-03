from tabelaIndicePrimario import IndicePrimario
import sys



possiveisEntradas = {'name', 'album', 'artists', 'track_number', 'disc_number', 'explicit', 'key', 'mode', 'year'}


def recebeEntradaSimples(linhas):
    
   # linhas = arqEntrada.readlines() 
    for i in range(0, len(linhas), 2):
        indice = linhas[i].strip()
        nome = linhas[i+1].strip()
    print(f"{indice}, {nome}")
    if indice not in possiveisEntradas: 
        return -1, nome
    return indice, nome

def recebeEntradaBool(linhas):
        bools = []
        indices = []
        nomes = []
        
        #linhas = arqEntrada.readlines()
        dadosCabecalho = linhas[0].split(' ')
        dadosEspecificos = linhas[1].split(', ')
        for i in dadosCabecalho: 
            if i == '&' or i == '||':
                bools.append(i)
            else:
                indices.append(i)
        for i in dadosEspecificos:
            nomes.append(i)

        print(f'{bools}, {indices}, {nomes}')

        for i in indices: 
            if i not in possiveisEntradas:
                return bools, -1, nomes

        return bools, indices, nomes

                    
#inicio main 
if __name__ == "__main__":

#construtor 
    indice = IndicePrimario()
    with open('query9.txt', 'r') as arq:
        cabecalho = arq.readlines()
        cabecalho[0] = cabecalho[0].strip()
        print(cabecalho[0])
        #Caso com booleano
        if '&' in cabecalho[0] or '||' in cabecalho[0]:     
            print('caso (BOOL)')
            boolsPedidos, indicesPedidos, chavesPedidas = recebeEntradaBool(cabecalho)
            indice.criaIndiceSecBool(indicesPedidos, boolsPedidos, chavesPedidas)
            if indicesPedidos == -1:
                print(f'ERRO: Entrada errada ({indicesPedidos})')
                sys.exit()
        #Caso Simples
        else:                                            
            print('caso (SIMPLES)')
            indicePedido, nomePedido = recebeEntradaSimples(cabecalho)
            indice.criaIndiceSecundarioSimples(indicePedido, nomePedido)
            if indicePedido == -1: 
                print(f'ERRO: Entrada errada ({indicePedido})')
                sys.exit()


