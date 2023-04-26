from AlgoritmoBusca import AlgoritmoBusca
from BuscaConstrutivaGulosa import BuscaConstrutivaGulosa
from Vizinhanca import Vizinhanca
from Solucao import Solucao
import time

class BuscaTemperaSimulada(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima:int, alpha:float, temperatura:float):
        super().__init__("BTS"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.temperatura = temperatura
        self.alpha = alpha
        self.solucao = ((BuscaConstrutivaGulosa(vizinhanca.distancias, solucao_otima)).buscar_solucao())[0]
    def buscar_solucao(self) -> list[Solucao]:
        pass