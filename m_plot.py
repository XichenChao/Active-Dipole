#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 18:05:28 2023

@author: vv19005
"""

import matplotlib.pyplot as plt
#import numpy as np
import pickle
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--measurement', help='the measurement we want to plot')
parser.add_argument('--TT', help='translational diffusion')
parser.add_argument('--P', help='dipole strength')
parser.add_argument('--v0', help='self-propulsion speed')

parser.add_argument('--c_N_plot', help='boolean')
parser.add_argument('--c_lifespan_plot', help='boolean')

args = parser.parse_args()

measurement = args.measurement
P = float(args.P)
v0 = float(args.v0)
TT = args.TT

c_N_plot=args.c_N_plot
c_lifespan_plot=args.c_lifespan_plot

if c_N_plot:
    
    filename = f'P={P}v0={v0}phi=0.05T_R=5e-02T_T={TT}_{measurement}'
    filepath = f'/Users/vv19005/Desktop/Xichen_supervision/2023.05.18/measurements/{measurement}/{filename}'
    
    with open(filepath, 'rb') as file:
        m = pickle.load(file)
    
    plt.figure(dpi=150)
    plt.plot(range(len(m)), m)
    plt.xlabel('snapshots')
    plt.ylabel(r'$N$')
    plt.title('time evolution of number of clusters')
    plt.show()

if c_lifespan_plot:
    
    filename = f'P={P}v0={v0}phi=0.05T_R=5e-02T_T={TT}_{measurement}'
    filepath = f'/Users/vv19005/Desktop/Xichen_supervision/2023.05.18/measurements/{measurement}/{filename}'
    
    with open(filepath, 'rb') as file:
        m = pickle.load(file)    

    # Plot a histogram
    plt.hist(m, bins=300, density=True, alpha=1, label='Histogram')
    
    plt.xlabel('lifespan of clusters')
    plt.ylabel('Density')
    plt.title('Distribution of lifespan of clusters')
    plt.show()

    
    
    
    
    
    