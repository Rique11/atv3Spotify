import os

possiveisEntradas = ['name', 'album', 'artists', 'track_number', 'disc_number', 'explicit', 'key', 'mode', 'year']

camposCabecalho = ['id','name','album','album_id','artists','artist_ids','track_number','disc_number','explicit','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature','year','release_date']

class IndicePrimario:

    def __init__(self):
        # Abrir o arquivo de dados (arquivo existente)
        self.__arquivoDados = open("tracks_features.csv", "r+", encoding="utf-8")
        
        # Arquivo de Índice Primário
        self.__arquivoIdxPrimario = None
        self.__tabelaIndices = []

        if os.path.isfile("arqIdxPrimario.txt"):
            print("Existe arquivo de índice primário")
            self.__arquivoIdxPrimario = open("arqIdxPrimario.txt", "r")
            self.__tabelaIndices = [linha.strip() for linha in self.__arquivoIdxPrimario]
            #print(self.__tabelaIndices)
            #print("TESTEEEE")
        else:
            print("Não existe arquivo de índice primário")
            self.__arquivoIdxPrimario = open("arqIdxPrimario.txt", "a+")
            RRN = 0
            for line in self.__arquivoDados.readlines():
                if line.startswith("id"):
                    continue  # Ignorar o cabeçalho
                chave = self.criaChaveCanonica(line)
                self.__tabelaIndices.append((chave, RRN))
                RRN += 1
            # Ordenar a tabela
            self.__tabelaIndices.sort(key=lambda a: a[0])

            # Escrever a tabela de índices no arquivo
            for chave, rrn in self.__tabelaIndices:
                self.__arquivoIdxPrimario.write(f"{chave} {rrn}\n")
            #Fechar arquivo
            self.__arquivoIdxPrimario.close()

            for i in range(len(self.__tabelaIndices)):
                print(self.__tabelaIndices[i])

    def criaChaveCanonica(self, registro):
        x = registro.split(',')
        chavePrimaria = x[0]
        #chavePrimaria = chavePrimaria.upper().replace(' ', '')
        return chavePrimaria

    def __del__(self):
        if self.__arquivoIdxPrimario:
            self.__arquivoIdxPrimario.close()
        if self.__arquivoDados:
            self.__arquivoDados.close()

    
    def consultaCabecalho(self):
        if self.__arquivoDados:
            self.__arquivoDados.seek(0)
            cabecalho = self.__arquivoDados.readline().strip()

            if cabecalho:
                return cabecalho
            else:
                print("Cabeçalho vazio ou não encontrado.")
                return None
        else:
            print("Arquivo de índice primário não aberto.")
            return None

    
    
    def buscaBinaria(self, chave, op):
        if op == 'I':
            tabela = self.__tabelaIndices 
        elif op == 'A': 
            tabela = self.__auxTabela
        inicio = 0
        final = len(tabela)

        #with open ("arqIdxPrimario.txt", "r") as arqIdxPrimario:
        
        while inicio < final:
            meio = (inicio + final) // 2
            linha = tabela[meio].split()
            
            
            chaveAux = linha[0]
            rnnAux = linha[1]

            if chave == chaveAux: 
                return int(rnnAux) #chave encontrada 
            elif chave < chaveAux:
                final = meio + 1
            else:
                inicio = meio - 1
                  
        return -1 #se nao achar 
    

    def criaIndiceSecundarioSimples(self, indiceSec, chave):
        print(f"{indiceSec}{chave}""aaaa")
        IDsAux = []
        RNNSec = []
        indiceSecundario = camposCabecalho.index(indiceSec)

        #print(indiceSecundario)
        with open("tracks_features.csv", "r+", encoding="utf-8") as arqDados: 
            for linha in arqDados: 
                if linha.startswith("id"):
                    continue  # Ignorar o cabeçalho
                campos = linha.strip().split(",")
                indicePrimario = campos[0].strip()

                nomeAux = campos[indiceSecundario].strip()
                if nomeAux.startswith("[") and nomeAux.endswith("]"):
                    nomeAuxFormatado = nomeAux.strip("['']")
                    
                else:
                    nomeAuxFormatado = nomeAux
                if nomeAuxFormatado == chave:
                    print(nomeAuxFormatado)
                    IDsAux.append(indicePrimario)
                else: 
                   pass
                   # print("nao presente")
            print(IDsAux)
            print("AUXBBB")
            print(IDsAux)

        #Busca Binaria Arquivo Indice Primario
        print(len(IDsAux))
        for i in IDsAux:
            print(i)
            rnn = self.buscaBinaria(i, 'I') 
            if rnn >= 0: 
                
                RNNSec.append(rnn)
            else:
                print("nao encontrado")


        #Escreve ArqIndiceSec
        with open("arqSolicitado.txt", "w", encoding="utf-8") as self.__arqSec:
            print(RNNSec)
            with open("tracks_features.csv", "r", encoding="utf-8") as self.__arqDados:
                linhas = self.__arqDados.readlines()
                for rnn in RNNSec: 
                    rnn = rnn + 1  
                    linha = linhas[rnn]
                    print(linha)
                    self.__arqSec.write(linha)




    def funcaoBase(self, indiceA, indiceB, booleano, chaveA, chaveB):
        indxSecA = camposCabecalho.index(indiceA)
        indxSecB = camposCabecalho.index(indiceB)
        print(f'{indxSecA}, {indxSecB}')
        IDsAux = []
        RNNSec = []
        with open("tracks_features.csv", "r", encoding="utf-8") as self.__arqDados:
                #funcaoSemTabelaAux
            for linha in self.__arqDados: 
                if linha.startswith("id"):
                    continue  # Ignorar o cabeçalho

                campos = linha.strip().split(",") #separa campos
                indxPrimario = campos[0].strip()  #recebe indices

                chaveAuxA = campos[indxSecA].strip()
                chaveAuxB = campos[indxSecB].strip()

                #formatacao das chaves
                if chaveAuxA.startswith("[") and chaveAuxA.endswith("]"):
                    chaveAuxAFormatado = chaveAuxA.strip("['']")
                else:
                    chaveAuxAFormatado = chaveAuxA
                        
                if chaveAuxB.startswith("[") and chaveAuxB.endswith("]"):
                    chaveAuxBFormatado = chaveAuxB.strip("['']")
                else:
                    chaveAuxBFormatado = chaveAuxB
                #fim formatacao chaves
                #print(f'{chaveAuxAFormatado}, {chaveAuxBFormatado}')

                if booleano == '&': #funcao & (and)
                    if chaveA == chaveAuxAFormatado and chaveB == chaveAuxBFormatado:
                        IDsAux.append(indxPrimario)

                elif booleano == '||':  #funcao || (or)
                    if chaveA == chaveAuxAFormatado or chaveB == chaveAuxBFormatado:
                        IDsAux.append(indxPrimario)
                    #fim da s elecao dos ID's
            print(IDsAux) 
        
        #Busca Binaria Arquivo Indice Primario
        print(len(IDsAux))
        for i in IDsAux:
            print(i)
            rnn = self.buscaBinaria(i, 'I') 
            if rnn >= 0:                
                RNNSec.append(rnn)
            else:
                print("nao encontrado")

        #Salva Tabela Auxiliar
        qtdeElemSalvos = len(IDsAux)
        for i in range(0, qtdeElemSalvos, 1): 
            linha = (f'{IDsAux[i]}, {RNNSec[i]}')
            self.__auxTabela.append(linha.strip(','))

        #return self.__auxTabela

    def funcaoDoisOuMais(self, bool, indice, chave):
        #Receber tabela auxiliar e realizar operação pedida
        indxSec = camposCabecalho.index(indice)
        print(indice)
        print(f'{indxSec}, {bool}, {chave}')
        IDsTemp = []
        RNNTemp = []
        tabelaTemp = []
        with open("tracks_features.csv", "r", encoding="utf-8") as self.__arqDados:
            for linha in self.__arqDados: 
                if linha.startswith("id"):
                    continue  # Ignorar o cabeçalho
            
                campos = linha.strip().split(",") #separa campos
                indxPrimario = campos[0].strip()  #recebe id
                chaveAux = campos[indxSec].strip() #recebe chave do indice
                #print(chaveAux)
          #formatacao das chaves
                if chaveAux.startswith("[") and chaveAux.endswith("]"):
                    chaveAuxFormatado = chaveAux.strip("['']")
                else:
                    chaveAuxFormatado = chaveAux
            #fim formatacao chaves
                if chaveAuxFormatado == chave: 
                    IDsTemp.append(indxPrimario)

           # print(IDsTemp)
            
        #Busca Binaria Arquivo Indice Primario
        print(len(IDsTemp))
        for i in IDsTemp:
           # print(i)
            rnn = self.buscaBinaria(i, 'I') 
            if rnn >= 0: 
                RNNTemp.append(rnn)
            else:
                print("nao encontrado")
                #Salva Tabela Auxiliar
        print(RNNTemp)
        qtdeElemSalvos = len(IDsTemp)
        for i in range(0, qtdeElemSalvos, 1): 
            linha = (f'{IDsTemp[i]}, {RNNTemp[i]}')
            tabelaTemp.append(linha.strip(','))
        print(len(tabelaTemp))
        # || (OU)  Adiciona na tabela o que a condicao pedir
        if bool == '||': 
            for linhaTemp in tabelaTemp: 
                for linhaAux in self.__auxTabela:
                    if linhaAux.strip() == linhaTemp.strip():
                        tabelaTemp.remove(linhaTemp)
            for linha in tabelaTemp:  
                tabelaTemp.append(linha)
            
        # &  (E)  Filtra da tabela com a proxima condicao 
        #### UNICO QUE FALTA
        elif bool == '&': 
            print("entrou no &")
            tabelaTempSet = set(tabelaTemp)
            auxTabelaSet = set(self.__auxTabela)

            linhasComuns = tabelaTempSet.intersection(auxTabelaSet)
            self.__auxTabela = list(linhasComuns)

    def criaIndiceSecBool(self, indices, bools, chaves):
        self.__auxTabela = []
        RNNSec = []
        print(f'{indices}, {bools}, {chaves}')
        totalOp = len(bools)
        print(totalOp)
        for i in range(0, len(bools), 1):
            if self.__auxTabela == []:
               self.funcaoBase(indices[i], indices[i+1], bools[i], chaves[i], chaves[i+1]) #(self, indiceA, indiceB, booleano, chaveA, chaveB, auxTable)
               print(self.__auxTabela)
            else: 
                print(f"FASE 2 {bools[i]}, {indices[i+1]}, {chaves[i+1]}")
                print(self.__auxTabela)
                self.funcaoDoisOuMais(bools[i], indices[i+1], chaves[i+1])  # 2 operadores ou mais (3 indices ou mais) (self, bool, indice, chave):
                
        

        #Escreve ArqIndiceSec
        with open("arqSolicitado.txt", "w", encoding="utf-8") as self.__arqSec:
            for linha in self.__auxTabela:
                #print(f'{auxTable[i]}, {auxTable[i+1]} LINHA')
                infoTable = linha.split(", ")
                print(infoTable)
                RNNSec.append(int(infoTable[1]))
            print(RNNSec)

            with open("tracks_features.csv", "r", encoding="utf-8") as self.__arqDados:
                linhas = self.__arqDados.readlines()
                for rnn in RNNSec: 
                    rnn = rnn + 1  
                    linha = linhas[rnn]
                    print(linha)
                    self.__arqSec.write(linha)
            print(len(camposCabecalho))
