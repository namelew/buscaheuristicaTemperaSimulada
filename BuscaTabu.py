from AlgoritmoBusca import AlgoritmoBusca
from Vizinhanca import Vizinhanca
import time
from Solucao import Solucao


class BuscaTabu(AlgoritmoBusca):
    def __init__(self, vizinhanca: Vizinhanca, solucao_otima, parametro_mandato, solucao: Solucao = None):
        super().__init__("BT"+vizinhanca.nome, vizinhanca.distancias, solucao_otima)
        self.parametro_mandato = parametro_mandato
        self.vizinhanca = vizinhanca
        if solucao is None:
            self.solucao = self.gerar_solucao_inicial_aleatoria()
        else:
            self.solucao = solucao

    def buscar_solucao(self) -> list[Solucao]:
        solucao_list = [self.solucao]
        iteracao = self.solucao.iteracao + 1
        melhor_qualidade = self.solucao.qualidade
        tabu = set()
        tabu_mandato = list()
        mandato = round(self.tamanho/self.parametro_mandato)
        qtd_trocas = self.vizinhanca.qtd_trocas
        while time.time() < self.tempo_limite:
            self.solucao = self.vizinhanca.melhor_vizinho(self.solucao, tabu)
            tabu.add(self.solucao.i_movimento)
            tabu_mandato.append(self.solucao.i_movimento)
            if qtd_trocas == 2:
                tabu.add(self.solucao.j_movimento)
                tabu_mandato.append(self.solucao.j_movimento)
            if self.solucao.qualidade < melhor_qualidade:
                melhor_qualidade = self.solucao.qualidade
                self.solucao.tempo = time.time() - self.tempo_limite
                self.solucao.iteracao = iteracao
                solucao_list.append(self.solucao)
                if melhor_qualidade == self.solucao_otima:
                    return solucao_list
            iteracao += 1
            if mandato == 0:
                tabu.remove(tabu_mandato.pop(0))
                if qtd_trocas == 2:
                    tabu.remove(tabu_mandato.pop(0))
            else:
                mandato -= 1
        return solucao_list
