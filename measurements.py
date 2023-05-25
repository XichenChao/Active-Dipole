#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 01:50:26 2023

@author: vv19005
"""
import background as bg

# the effective diffusion
def Da(v0, DR):
    return v0**2/(2*DR)

# the Peclet number
def Pe(v0, DR):
    return 2*v0/DR

# the number of clusters of all snapshots
def c_N(data, T=20000):
    N_list=[]
    for t in range(T):
        N_list.append(len(data[t])-1)
    return N_list

# the lifespan distribution of clusters for a simulation
def c_lifespan(data_ns, data, tau=15000):    
    if len(data[-1])-1>=100:
        return 0    
    c_info=bg.cluster_check(data_ns, tau, plot=False)
    return c_info[:,2]-c_info[:,1]