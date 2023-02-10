import math
from AlgoritmoBusca import AlgoritmoBusca
from Solucao import Solucao
import time


class BuscaConstrutivaGulosa(AlgoritmoBusca):
    def __init__(self, distancias: tuple, solucao_otima: int):
        super().__init__("BCG", distancias, solucao_otima)

    def buscar_solucao(self) -> list[Solucao]:
        melhor_qualidade = math.inf
        iteracao = 1
        solucao_list = []
        while time.time() < self.tempo_limite and iteracao < self.tamanho:
            solucao = Solucao(self.distancias[0][iteracao], [iteracao], 0, 0)  # Elemento 0 fixo no início da solução
            visitados = {iteracao}
            elemento = iteracao
            melhor = math.inf
            melhor_elemento = 0
            while len(visitados)+1 < self.tamanho:
                for i in range(1, self.tamanho):
                    if i not in visitados:
                        if self.distancias[i][elemento] < melhor:
                            melhor = self.distancias[i][elemento]
                            melhor_elemento = i
                visitados.add(melhor_elemento)
                solucao.ciclo.append(melhor_elemento)
                solucao.qualidade += melhor
                elemento = melhor_elemento
                melhor = math.inf
            solucao.qualidade += self.distancias[0][elemento]
            if solucao.qualidade < melhor_qualidade:
                melhor_qualidade = solucao.qualidade
                solucao.tempo = time.time() - self.tempo_limite
                solucao.iteracao = iteracao
                solucao_list.append(solucao)
                if melhor_qualidade == self.solucao_otima:
                    return solucao_list
            iteracao += 1
        return solucao_list
