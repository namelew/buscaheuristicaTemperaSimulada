from AlgoritmoBusca import AlgoritmoBusca
from BuscaConstrutivaGulosa import BuscaConstrutivaGulosa
from Vizinhanca import Vizinhanca
from Solucao import Solucao
import time

class BuscaHibridaGulosoTemperaSimulada(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima:int, tipo_resfriamento:int, alpha:float, temperatura:float):
        super().__init__("BTS"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.temperatura = temperatura
        self.alpha = alpha
        if tipo_resfriamento == 0:
            self.resfriar = lambda x:x*self.alpha
        else:
            linear = lambda x : x if x > 0 else 0
            self.resfriar = lambda x: linear(x-self.alpha)
        guloso = BuscaConstrutivaGulosa(vizinhanca.distancias, solucao_otima)
        guloso.tempo_limite = self.tempo_limite
        self.solucao = guloso.buscar_solucao()[0]
    def buscar_solucao(self) -> list[Solucao]:
        pass