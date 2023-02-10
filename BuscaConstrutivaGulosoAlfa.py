import math
from AlgoritmoBusca import AlgoritmoBusca
from Solucao import Solucao
import time
import random
from heapq import heappush
from heapq import heappushpop


class BuscaConstrutivaGulosoAlfa(AlgoritmoBusca):
    def __init__(self, distancias: tuple, solucao_otima: int, alfa: float):
        super().__init__("BCGα10", distancias, solucao_otima)
        self.alfa = alfa

    def buscar_solucao(self) -> list[Solucao]:
        solucao_list = []
        iteracao = 1
        melhor_qualidade = math.inf
        while time.time() < self.tempo_limite:
            elemento = random.randint(1, self.tamanho-1)
            solucao = Solucao(self.distancias[0][elemento], [elemento])  # Elemento 0 fixo no início da solução
            visitados = {elemento}
            tamanho_restante = self.tamanho-2
            while tamanho_restante > 0:
                heap_max = []
                raiz = 0
                mellhores_alfa = math.ceil(tamanho_restante * self.alfa)
                for i in range(1, self.tamanho):
                    if i not in visitados:
                        if len(heap_max) < mellhores_alfa:
                            # Multiplica por -1 para transformar heap min (padrão) em heap max
                            heappush(heap_max, (self.distancias[i][elemento]*-1, i))
                        elif raiz < self.distancias[i][elemento]*-1:
                            heappushpop(heap_max, (self.distancias[i][elemento]*-1, i))
                        raiz = (heap_max[0])[0]
                elemento_tup = heap_max[random.randint(0, mellhores_alfa-1)]
                distancia = elemento_tup[0]*-1
                elemento = elemento_tup[1]
                visitados.add(elemento)
                solucao.ciclo.append(elemento)
                solucao.qualidade += distancia
                tamanho_restante -= 1
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
