from Vizinhanca import Vizinhanca
from Solucao import Solucao
import math


class Vizinhanca2opt(Vizinhanca):
    def __init__(self, distancias: tuple):
        super().__init__("2opt", distancias, 2)

    def computar_qualidade(self, solucao: Solucao, i: int, j: int) -> int:
        qualidade = solucao.qualidade
        elemento_pre_i, elemento_i, elemento_pos_i, elemento_pre_j, elemento_j, elemento_pos_j \
            = solucao.retornar_elementos(i, j)
        # i sempre < j
        qualidade += - self.distancias[elemento_i][elemento_pre_i] - self.distancias[elemento_j][elemento_pos_j] \
            + self.distancias[elemento_i][elemento_pos_j] + self.distancias[elemento_j][elemento_pre_i]
        return qualidade

    @staticmethod
    def gerar_novo_ciclo(solucao: Solucao, i: int, j: int) -> list:
        return solucao.ciclo[:i] + list(reversed(solucao.ciclo[i:j + 1])) + solucao.ciclo[j + 1:]

    def melhor_vizinho(self, solucao: Solucao, tabu: set) -> Solucao:
        melhor_qualidade = math.inf
        imelhor = -1
        jmelhor = -1
        for i in range(self.tamanho-1):
            if solucao.ciclo[i] not in tabu:
                for j in range(i+1, self.tamanho-1):
                    if solucao.ciclo[j] not in tabu:
                        qualidade = self.computar_qualidade(solucao, i, j)
                        if qualidade < melhor_qualidade:
                            melhor_qualidade = qualidade
                            imelhor = i
                            jmelhor = j
        return Solucao(melhor_qualidade, self.gerar_novo_ciclo(solucao, imelhor, jmelhor), solucao.ciclo[imelhor], solucao.ciclo[jmelhor])

    def primeiro_vizinho_melhor(self, solucao: Solucao, tabu: set) -> Solucao:
        melhor_qualidade = solucao.qualidade
        for i in range(self.tamanho-1):
            if i not in tabu:
                for j in range(i + 1, self.tamanho-1):
                    if j not in tabu:
                        qualidade = self.computar_qualidade(solucao, i, j)
                        if qualidade < melhor_qualidade:
                            return Solucao(qualidade, self.gerar_novo_ciclo(solucao, i, j), i, j)
        return solucao
