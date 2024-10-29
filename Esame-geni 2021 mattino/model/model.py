import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._nodi = []
        self._archi = []
        self._idMap = {}


    def build_graph(self):
        self._nodi = DAO.get_all_chromosomes()
        self._grafo.add_nodes_from(self._nodi)

        self._archi = DAO.get_all_edges()

        for e in self._archi:
            cr1 = e[0]
            cr2 = e[1]
            gene1 = e[2]
            gene2 = e[3]
            peso = e[4]
            if cr1 in self._nodi and cr2 in self._nodi and cr1 != cr2:
                if self._grafo.has_edge(cr1, cr2):
                    self._grafo[cr1][cr2]['weight'] += peso
                else:
                    self._grafo.add_edge(cr1, cr2, weight=peso)

    def get_min_weight(self):
        return min([x[2]['weight'] for x in self.get_edges()])

    def get_max_weight(self):
        return max([x[2]['weight'] for x in self.get_edges()])

    def contaValoriSoglia(self, soglia):
        numMaggiori = 0
        numMinori = 0
        for a in self.get_edges():
            if a[2]['weight'] > soglia:
                numMaggiori += 1
            elif a[2]['weight'] < soglia:
                numMinori += 1
        return numMaggiori, numMinori

    def getEdgeWeight(self, v1, v2):
        return self._grafo[v1][v2]["weight"]

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def get_edges(self):
        return list(self._grafo.edges(data=True))
