#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:06:38 2021

@author: michela Quadrini
"""
import math
import pandas as pd
import numpy as np
from sklearn.metrics import *

from sklearn.cluster import *
from sklearn import metrics

import argparse

args = argparse.ArgumentParser()
args.add_argument('--domain', default='Archaea', choices=["Archaea", "Bacteria", "Eukaryota"])
args.add_argument('--method', default='Aspralign',  choices=["Aspralign", "Psmalign", "Genus"])
args = args.parse_args()

domain = args.domain
method = args.method


data = pd.read_csv(f'./Data/{domain}16S-{method}.txt', sep=",", header=None)
data.columns = ["molecule1", "molecule2", "distance value"]
i=0

num_lines = len(data.axes[0])
m = int((-1 + math.sqrt(1+8*num_lines))/2)
s= (m+1,m+1)
distance_matrix= np.zeros(s)

el_app = " "

i=0
row=0
col =0
while (i<num_lines):
    if (el_app == " "): 
        col = col+1
        distance_matrix[row][col] = distance_matrix[col][row] = int(data["distance value"][i])
        el_app = data["molecule1"][i]
        
    elif (el_app == data["molecule1"][i]):
        col = col+1
        distance_matrix[row][col] = distance_matrix[col][row] = data["distance value"][i]
    else:
        
        row=row +1
        col= row +1
        distance_matrix[row][col] = distance_matrix[col][row] = data["distance value"][i]
        el_app = data["molecule1"][i]
    i=i+1




n_clusters_Archaea16S = 3
n_clusters_Bacteria16S = 17
n_clusters_Eukaryota16S= 11

labels_true_Archaea16S= [ 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

labels_true_Bacteria16S = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 22, 22, 11, 11, 15, 15, 0, 18, 18,
18, 18, 18, 18, 18, 18, 14, 8, 6, 6, 6, 6, 6, 6, 6, 10, 10, 10, 10, 10, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
7, 7, 7, 7, 7, 7, 7, 7, 7, 24, 24, 24, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,  20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 16, 16, 16, 19, 
19, 19, 19, 19, 19, 19, 19, 19, 21, 21, 21, 21, 21, 21, 21, 21, 21, 12, 12, 12] 

labels_true_Eukaryota16S = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26,
27, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28,
28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28,
28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31,
31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31,
31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34,
34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34,
34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35,
35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35,
35, 35, 35, 35, 35]

if(domain=="Archaea"): 
    n_clusters = n_clusters_Archaea16S  
    labels_true = labels_true_Archaea16S
elif(domain=="Bacteria"):
    n_clusters = n_clusters_Bacteria16S
    labels_true = labels_true_Bacteria16S
elif(domain=="Eukaryota"):
    n_clusters = n_clusters_Eukaryota16S
    labels_true = labels_true_Eukaryota16S


print("Domain:", domain)
print("Method:", method)
model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage ='complete').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)

print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))
