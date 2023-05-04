from Vizinhanca import Vizinhanca
from Solucao import Solucao
import math


class VizinhancaShift(Vizinhanca):
    def __init__(self, distancias: tuple):
        super().__init__("sh", distancias, 1)

    def computar_qualidade(self, solucao: Solucao, i: int, j: int) -> int:
        qualidade = solucao.qualidade
        elemento_pre_i, elemento_i, elemento_pos_i, elemento_pre_j, elemento_j, elemento_pos_j \
            = solucao.retornar_elementos(i, j)
        # Elemento i é posicionado na posição de j, i sempre != de j
        if i < j:  # Deslocamento para a esquerda (elemento i movimenta-se para a direita na solução)
            qualidade += - self.distancias[elemento_i][elemento_pre_i] - self.distancias[elemento_j][elemento_pos_j] \
                         + self.distancias[elemento_i][elemento_pos_j]
            if j - i == 1:
                qualidade += self.distancias[elemento_j][elemento_pre_i]
            else:
                qualidade += - self.distancias[elemento_i][elemento_pos_i] \
                             + self.distancias[elemento_pre_i][elemento_pos_i] + self.distancias[elemento_j][elemento_i]
        else:  # Deslocamento para a direita (elemento i movimenta-se para a esquerda na solução)
            qualidade += - self.distancias[elemento_i][elemento_pos_i] - self.distancias[elemento_j][elemento_pre_j] \
                         + self.distancias[elemento_i][elemento_pre_j]
            if i - j == 1:
                qualidade += self.distancias[elemento_j][elemento_pos_i]
            else:
                qualidade += - self.distancias[elemento_i][elemento_pre_i] \
                             + self.distancias[elemento_pre_i][elemento_pos_i] + self.distancias[elemento_j][elemento_i]
        return qualidade

    @staticmethod
    def gerar_novo_ciclo(solucao: Solucao, i: int, j: int) -> list:
        if i < j:
            ciclo = solucao.ciclo[:i] + solucao.ciclo[i + 1:j + 1] + [solucao.ciclo[i]] + solucao.ciclo[j + 1:]
        else:
            ciclo = solucao.ciclo[:j] + [solucao.ciclo[i]] + solucao.ciclo[j:i] + solucao.ciclo[i + 1:]
        return ciclo

    def melhor_vizinho(self, solucao: Solucao, tabu: set, temperatura:float) -> Solucao:
        melhor_qualidade = math.inf
        imelhor = -1
        jmelhor = -1
        for i in range(self.tamanho-1):
            if solucao.ciclo[i] not in tabu:
                for j in range(self.tamanho-1):
                    if j < i and i - j == 1:  # evitar testar swap duas vezes
                        continue
                    if j != i and solucao.ciclo[j] not in tabu:
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
                for j in range(self.tamanho-1):
                    if j < i and i - j == 1:  # evita teste swap i,j vizinhos duas vezes
                        continue
                    if j != i and j not in tabu:
                        qualidade = self.computar_qualidade(solucao, i, j)
                        if qualidade < melhor_qualidade:
                            return Solucao(qualidade, self.gerar_novo_ciclo(solucao, i, j), i, j)
        return solucao
