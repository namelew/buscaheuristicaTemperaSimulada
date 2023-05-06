from AlgoritmoBusca import AlgoritmoBusca
from Vizinhanca import Vizinhanca
from Solucao import Solucao
import time

class BuscaLocalTemperaSimulada(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima:int, tipo_resfriamento:int, alpha:float, temperatura:float, solucao:Solucao = None):
        super().__init__("BTS"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
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
        while time.time() < self.tempo_limite:
            self.solucao = self.vizinhanca.melhor_vizinho(self.solucao, set(), self.temperatura)
            if self.solucao.qualidade < melhor_qualidade:
                melhor_qualidade = self.solucao.qualidade
                self.solucao.tempo = time.time() - self.tempo_limite
                self.solucao.iteracao = iteracao
                solucao_list.append(self.solucao)
                if melhor_qualidade == self.solucao_otima:
                    return solucao_list
            else:
                break
            iteracao += 1
            self.temperatura = self.resfriar(self.temperatura) if self.resfriar(self.temperatura) >= 0.01 else 0
        return solucao_list