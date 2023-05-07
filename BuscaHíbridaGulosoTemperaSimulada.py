from AlgoritmoBusca import AlgoritmoBusca
from BuscaConstrutivaGulosa import BuscaConstrutivaGulosa
from Vizinhanca import Vizinhanca
from Solucao import Solucao
from BuscaLocalTemperaSimulada import BuscaLocalTemperaSimulada

class BuscaHibridaGulosoTemperaSimulada(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima:int, tipo_resfriamento:int, alpha:float, temperatura:float):
        super().__init__("BTS"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.tipo_resfriamento = tipo_resfriamento
        self.vizinhanca = vizinhanca
        self.temperatura = temperatura
        self.alpha = alpha
    def buscar_solucao(self) -> list[Solucao]:
        algoritmo = BuscaConstrutivaGulosa(self.distancias, self.solucao_otima)
        algoritmo.tempo_limite = self.tempo_limite
        solucao_list = algoritmo.buscar_solucao()
        solucao = solucao_list[-1]
        algoritmo = BuscaLocalTemperaSimulada(self.vizinhanca, self.solucao_otima, self.tipo_resfriamento, self.alpha,self.temperatura,solucao)
        algoritmo.tempo_limite = self.tempo_limite
        solucao_list.extend(algoritmo.buscar_solucao())
        return solucao_list