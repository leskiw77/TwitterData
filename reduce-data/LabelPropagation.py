import csv
import statistics

import networkx as nx
from networkx.algorithms.community import asyn_lpa_communities, greedy_modularity_communities, coverage, performance
from networkx.algorithms import is_bipartite

def create_network():
    G = nx.Graph()

    with open('data_reduced.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            followers = row[2].split(',')
            edges = [(row[0], f) for f in followers]
            G.add_edges_from(edges)
    return G


print("Creating graph")
G = create_network()

print("Edges number: {}".format(len(G.edges)))

is_bipartite(G)
print("Async LPA")

yield_frequency = 10

for i, communities in enumerate(asyn_lpa_communities(G, max_iter=30000, yield_frequency=yield_frequency)):
    # ccc = [com for com in communities]
    result = [r for r in communities if len(r) > 100]
    lengths = [len(fs) for fs in result]

    # print(result)
    print(len(G), sum(len(c) for c in result))
    # print(set(G) == set.union(*result))
    #
    # q1 = coverage(G, communities)
    # q2 = performance(G, communities)

    print((i + 1) * yield_frequency, len(result), min(lengths), statistics.median(lengths), sum(lengths) / len(lengths),
          max(lengths))
