import os

possiveisEntradas = ['name', 'album', 'artists', 'track_number', 'disc_number', 'explicit', 'key', 'mode', 'year']

camposCabecalho = ['id','name','album','album_id','artists','artist_ids','track_number','disc_number','explicit','danceability','energy,key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature','year','release_date']

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
            print(self.__tabelaIndices)
            print("TESTEEEE")
#            for linha in self.__tabelaIndices:
#                dados = linha.split()
#                print(dados)
            # TODO: Carregar tabela com base no arquivo de índice
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

    
    
    def buscaBinaria(self, chave):
        inicio = 0
        final = len(self.__tabelaIndices)

        #with open ("arqIdxPrimario.txt", "r") as arqIdxPrimario:
        
        while inicio < final:
            meio = (inicio + final) // 2
            linha = self.__tabelaIndices[meio].split()
            
            
            chaveAux = linha[0]
            rnnAux = linha[1]

            if chave == chaveAux: 
                return int(rnnAux) #chave encontrada 
            elif chave < chaveAux:
                final = meio + 1
            else:
                inicio = meio - 1
                  
        return -1 #se nao achar 
    

    def criaIndiceSecundario(self, indiceSec, chave):
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
        for i in IDsAux:
            print(i)
            rnn = self.buscaBinaria(i) 
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



