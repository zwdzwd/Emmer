from dimension import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class EMCanvas:

    def __init__(self):
        self.x = {}             # plotting elements
        self.internal_index = 1

    def set_dim(self, xx, dim):
        if isinstance(dim, DimGen):
            dim.generate(self, xx)
        else:
            xx.dim = dim
    
    def add(self, xx, dim=DimUnit(), name=''):
        self.set_dim(xx, dim)
        if name == '':
            name = '.internal.%s.%d' % (type(xx).__name__, self.internal_index)
            self.internal_index += 1
        self.x[name] = xx

    def plot(self):
        fig = plt.figure()
        fig.set_tight_layout(True)
        for nm, xx in self.x.iteritems():
            xx.ax = fig.add_axes(xx.dim, frameon=False)
            xx.plot()
    
    def layout(self):

        fig = plt.figure()
        fig.set_tight_layout(True)
        for nm, xx in self.x.iteritems():
            xx.ax = fig.add_axes(xx.dim, frameon=False)
            xx.ax.set_xticks([])
            xx.ax.set_yticks([])
            xx.ax.text(0.5,0.5,nm,ha='center',va='center')
            xx.ax.add_patch(mpatches.Rectangle((0.02, 0.02), 0.96, 0.96, fill=False))
            
