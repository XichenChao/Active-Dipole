#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:57:06 2023

@author: vv19005
"""

#import numpy as np
import background as bg
import pickle
#import string_shifting as ss
import measurements as ms
import argparse

### parameters

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--P', help='dipole strength')
parser.add_argument('--v0', help='self-propulsion speed')
parser.add_argument('--TT', help='translational diffuison')

parser.add_argument('--Da_pickle', help='boolean')
parser.add_argument('--Pe_pickle', help='boolean')
parser.add_argument('--c_N_pickle', help='boolean')
parser.add_argument('--c_lifespan_pickle', help='boolean')

# Parse the command-line arguments
args = parser.parse_args()

# Access the argument value
P = float(args.P)
v0 = float(args.v0)
TT = args.TT

Da_pickle = args.Da_pickle
Pe_pickle = args.Pe_pickle
c_N_pickle = args.c_N_pickle
c_lifespan_pickle = args.c_lifespan_pickle

TR='5e-02' # rotational temperature
DR=3*float(TR) # rotational diffusion

path='/Users/vv19005/Desktop/Xichen_supervision/2022.09.01/data_ns/scan1'
path_pickle='/Users/vv19005/Desktop/Xichen_supervision/2023.05.18/measurements'

### pick the data
file = open('{path}/P={P}v0={v0}phi=0.05T_R={TR}T_T={T_T}'.format(T_T=TT, TR=TR, path=path, P=P, v0=v0) ,'rb')
data_ns=pickle.load(file)
data=bg.cluster_split(data_ns)
file.close()

### dump measurements specified
if Da_pickle:
    file = open('{path_pickle}/Da/P={P}v0={v0}phi=0.05T_R={TR}T_T={T_T}_Da'.format(T_T=TT, TR=TR, path_pickle=path_pickle, P=P, v0=v0) ,'wb')
    pickle.dump(ms.Da(v0, DR),file)
    file.close()  

if Pe_pickle:
    file = open('{path_pickle}/Pe/P={P}v0={v0}phi=0.05T_R={TR}T_T={T_T}_Pe'.format(T_T=TT, TR=TR, path_pickle=path_pickle, P=P, v0=v0) ,'wb')
    pickle.dump(ms.Pe(v0, DR),file)
    file.close()  

if c_N_pickle:
    file = open('{path_pickle}/c_N/P={P}v0={v0}phi=0.05T_R={TR}T_T={T_T}_c_N'.format(T_T=TT, TR=TR, path_pickle=path_pickle, P=P, v0=v0) ,'wb')
    pickle.dump(ms.c_N(data),file)
    file.close()  

if c_lifespan_pickle:
    file = open('{path_pickle}/c_lifespan/P={P}v0={v0}phi=0.05T_R={TR}T_T={T_T}_c_lifespan'.format(T_T=TT, TR=TR, path_pickle=path_pickle, P=P, v0=v0) ,'wb')
    pickle.dump(ms.c_lifespan(data_ns, data),file)
    file.close()  












