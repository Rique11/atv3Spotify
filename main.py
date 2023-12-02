from tabelaIndicePrimario import IndicePrimario
import sys



possiveisEntradas = {'name', 'album', 'artists', 'track_number', 'disc_number', 'explicit', 'key', 'mode', 'year'}


def recebeEntrada():
    with open("query7.txt","r") as arqEntrada:
        linhas = arqEntrada.readlines() 
        for i in range(0, len(linhas), 2):
            indice = linhas[i].strip()
            nome = linhas[i+1].strip()
        print(f"{indice}, {nome}")
    if indice not in possiveisEntradas: 
        return -1, nome
    return indice, nome

#inicio main 
if __name__ == "__main__":

#construtor 
    indice = IndicePrimario()

    indicePedido, nomePedido = recebeEntrada()

    if indicePedido == -1: 
        print(f'ERRO: Entrada errada ({indicePedido})')
        sys.exit()
    
    indice.criaIndiceSecundario(indicePedido, nomePedido)

