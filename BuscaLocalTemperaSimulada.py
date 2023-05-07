from AlgoritmoBusca import AlgoritmoBusca
from Vizinhanca import Vizinhanca
from Solucao import Solucao
from random import random,seed
from math import e,inf
from time import time

class BuscaLocalTemperaSimulada(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima:int, tipo_resfriamento:int, alpha:float, temperatura:float, solucao:Solucao = None):
        super().__init__("BTS"+("RG" if tipo_resfriamento == 0 else "RL")+ vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.vizinhanca = vizinhanca
        self.temperatura = temperatura
        self.alpha = alpha

        if tipo_resfriamento == 0:
            self.resfriar = lambda x:x*self.alpha
        else:
            linear = lambda x : x if x > 0 else 0
            self.resfriar = lambda x: linear(x-self.alpha)

        if solucao is None:
            self.solucao = self.gerar_solucao_inicial_aleatoria()
        else:
            self.solucao = solucao

    def buscar_solucao(self) -> list[Solucao]:
        solucao_list = [self.solucao]
        iteracao = self.solucao.iteracao + 1
        melhor_qualidade = self.solucao.qualidade
        timeout = False
        seed(time())
        while time() < self.tempo_limite:
            pivo = self.solucao
            changePivo = True
            melhor_local = pivo
            while changePivo and time() < self.tempo_limite:
                changePivo = False
                for i in range(self.vizinhanca.tamanho - 1):
                    for j in range(i,self.vizinhanca.tamanho - 2):
                        vizinho = self.vizinhanca.proximo_vizinho(pivo, i, j + 1)
                        if time() >= self.tempo_limite:
                            timeout = True
                            break
                        if vizinho.qualidade < pivo.qualidade:
                            if vizinho.qualidade < melhor_local.qualidade:
                                melhor_local = vizinho
                            changePivo = True
                            pivo = vizinho
                            break
                        elif self.temperatura > 0:
                            deltaC = lambda x:(x/pivo.qualidade)-1
                            calculaAceite = lambda x:e ** ((-1 * deltaC(x))/self.temperatura)
                            if random() <= calculaAceite(vizinho.qualidade):
                                pivo = vizinho
                    if timeout or changePivo:
                        break
            if melhor_local.qualidade < melhor_qualidade:
                self.solucao = melhor_local
                melhor_qualidade = self.solucao.qualidade
                self.solucao.tempo = time() - self.tempo_limite
                self.solucao.iteracao = iteracao
                solucao_list.append(self.solucao)
                if melhor_qualidade == self.solucao_otima:
                    return solucao_list
            else:
                break
            iteracao += 1
            self.temperatura = self.resfriar(self.temperatura) if self.resfriar(self.temperatura) >= 0.01 else 0
        return solucao_list