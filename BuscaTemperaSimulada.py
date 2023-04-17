from AlgoritmoBusca import AlgoritmoBusca
from Vizinhanca import Vizinhanca
from Solucao import Solucao
import time

class BuscaTemperaSimulada(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima:int, temperatura:float):
        super().__init__("BTS"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.temperatura = temperatura
    def buscar_solucao(self) -> list[Solucao]:
        pass