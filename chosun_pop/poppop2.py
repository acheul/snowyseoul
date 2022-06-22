import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random

# init: 2022-06-22 #
# For the distributed data observers #
# Display identical personnels nested in two households with paird colors. #

def style_here(s, index_here, props=''):
    return np.where(s.index==index_here, props, '')

def display_iden_hhs(df, i, j):
    '''
    * df should be the distributed data set.
    * i and j stands for an index of each personnel (index here is not pid(personal id). Just a sequantial normal index.)
    '''
    d1, d2 = df[df['hid']==df['hid'].iloc[i]], df[df['hid']==df['hid'].iloc[j]]
    pid2idx = {}
    for d in [d1,d2]:
        for idx,pid in zip(d.index, d['pid']):
            if pid not in pid2idx:
                pid2idx[pid] = [idx]
            else:
                pid2idx[pid].append(idx)
    pids = [pid for pid,idx in pid2idx.items() if len(idx)>1]
    bg_rgbas = [e/len(pids) for e in range(len(pids))]
    bg_rgbas = [plt.cm.get_cmap('tab20b')(e) for e in bg_rgbas]
    bg_rgbas = [tuple(e*256 for e in bg_rgba[:-1])+(1.0,) for bg_rgba in bg_rgbas]
    random.shuffle(bg_rgbas)

    d1 = d1.fillna('').style
    d2 = d2.fillna('').style
    for (pid, bg_rgba) in zip(pids, bg_rgbas):
        idx_s = pid2idx.get(pid)
        if len(idx_s)>1:
            for idx in idx_s:
                d1 = d1.apply(style_here, index_here=idx, props=f"color:white;background-color:rgba{bg_rgba}", axis=0)
                d2 = d2.apply(style_here, index_here=idx, props=f"color:white;background-color:rgba{bg_rgba}", axis=0)
    display(d1)
    display(d2)