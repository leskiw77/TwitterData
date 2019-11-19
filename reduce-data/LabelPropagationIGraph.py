import csv
import statistics

from igraph import *


def create_network():
    g = Graph()

    vertexes = set()
    edges = []

    with open('data_reduced.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:

            vertexes.add(row[0])

            followers = row[2].split(',')
            for f in followers:
                vertexes.add(f)
                edges.append((row[0], f))
                # g.add_vertex(f)
                # g.add_edge(row[0], f)

    print("add vertices {}".format(len(vertexes)))
    for x in vertexes:
        g.add_vertex(x)
    print("add edges")

    g.add_edges(edges)
    return g


print("Creating graph")
G = create_network()

print("Edges number: {}".format(len(G.get_edgelist())))

communities = G.community_label_propagation()

for c in communities:
    print(c)
# print("Async LPA")
#
# yield_frequency = 10
#
# for i, communities in enumerate(asyn_lpa_communities(G, max_iter=30000, yield_frequency=yield_frequency)):
#     # ccc = [com for com in communities]
#     result = [r for r in communities if len(r) > 100]
#     lengths = [len(fs) for fs in result]
#
#     # print(result)
#     print(len(G), sum(len(c) for c in result))
#     # print(set(G) == set.union(*result))
#     #
#     # q1 = coverage(G, communities)
#     # q2 = performance(G, communities)
#
#     print((i + 1) * yield_frequency, len(result), min(lengths), statistics.median(lengths), sum(lengths) / len(lengths),
#           max(lengths))
