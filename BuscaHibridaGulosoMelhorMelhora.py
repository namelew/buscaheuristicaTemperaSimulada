from BuscaLocalMelhorMelhora import BuscaLocalMelhorMelhora
from AlgoritmoBusca import AlgoritmoBusca
from Solucao import Solucao
from Vizinhanca import Vizinhanca
from BuscaConstrutivaGulosa import BuscaConstrutivaGulosa


class BuscaHibridaGulosoMelhorMelhora(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima: int):
        super().__init__("CG+MM"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.vizinhanca = vizinhanca

    def buscar_solucao(self) -> list[Solucao]:
        algoritmo = BuscaConstrutivaGulosa(self.distancias, self.solucao_otima)
        algoritmo.tempo_limite = self.tempo_limite
        solucao_list = algoritmo.buscar_solucao()
        solucao = solucao_list[-1]
        algoritmo = BuscaLocalMelhorMelhora(self.vizinhanca, self.solucao_otima, solucao)
        algoritmo.tempo_limite = self.tempo_limite
        solucao_list.extend(algoritmo.buscar_solucao())
        return solucao_list
