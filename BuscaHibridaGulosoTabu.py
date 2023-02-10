from BuscaTabu import BuscaTabu
from AlgoritmoBusca import AlgoritmoBusca
from Solucao import Solucao
from Vizinhanca import Vizinhanca
from BuscaConstrutivaGulosa import BuscaConstrutivaGulosa


class BuscaHibridaGulosoTabu(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima: int, parametro_mandato):
        super().__init__("CG+BT"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.vizinhanca = vizinhanca
        self.parametro_mandato = parametro_mandato

    def buscar_solucao(self) -> list[Solucao]:
        algoritmo = BuscaConstrutivaGulosa(self.distancias, self.solucao_otima)
        algoritmo.tempo_limite = self.tempo_limite
        solucao_list = algoritmo.buscar_solucao()
        solucao = solucao_list[-1]
        algoritmo = BuscaTabu(self.vizinhanca, self.solucao_otima, self.parametro_mandato, solucao)
        algoritmo.tempo_limite = self.tempo_limite
        solucao_list.extend(algoritmo.buscar_solucao())
        return solucao_list
