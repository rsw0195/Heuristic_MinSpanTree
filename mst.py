# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:44:26 2018

@author: Rebecca
"""

def mst_algo(locs,dist):
    name_or_team = "rswood"
    mst = []
    edges = 0
    loops = 0
    parents = {}
    for i in locs:
        parents[i[0]] = i[0]
    
    loc_pair = [[k, dist[k]] for k in dist.keys()]
    loc_pair.sort(key = lambda x:(x[1]), reverse = False)
    
    def par(parent, node):
        if parent[node] == node:
            return node
        return par(parent, parent[node])
        
    while edges < (len(locs) - 1):
        node1 = loc_pair[loops][0][0]
        node2 = loc_pair[loops][0][1]
        parent1 = par(parents, node1)
        parent2 = par(parents, node2)
        loops += 1
        if parent1 != parent2:
            edges += 1
            mst.append((node1, node2))
            parents[parent2] = parent1
            
    return name_or_team, mst