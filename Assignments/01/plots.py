import numpy as np
import numba as nb
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import os

# setting up the plots
plt.rcParams.update({'font.size': 15})
plt.rcParams['lines.linewidth'] = 2.5
font = {'family': 'serif', 'serif': ['Palatino'], 'size': 15}
plt.rc('font', **font)
plt.rc('text', usetex=True)
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#0072BD', '#D95319', '#FAAD26', '#7E2F8E', '#77AC30', '#4DBEEE',
                                                     '#A2142F', '#000000']) 

def compare_lifecycle(model1,model2, sim, par, labels = ['Model 1','Model 2']):
    # plot behavior
    fig, ax = plt.subplots(2,2,figsize=(2/3*17.5,13*2/3), sharex=True)
    ax = ax.flatten()

    var_name = {'c': r'Average consumption ($c$)', 'a': r'Average assets ($a$)', 
                'h': r'Average hours worked ($h$)', 'n': r'Average fertility ($n$)'}

    # for i, var in enumerate(('c','a','h','n')):
    for i, (var, _) in enumerate(var_name.items()):   
        # fig, ax = plt.subplots()
        ax[i].scatter(range(par[model1].simT),np.mean(getattr(sim[model1],var),axis=0),label=labels[0])
        ax[i].scatter(range(par[model2].simT),np.mean(getattr(sim[model2],var),axis=0),label=labels[1])
        ax[i].set(xlabel='period, t',ylabel=f'Avg. {var}',xticks=range(par[model1].simT));
        ax[i].set_title(var_name[var])
        if i == 0:
            ax[i].legend(frameon=False, fontsize = 12)
    return fig