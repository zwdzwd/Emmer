from core import *
from canvas import EMCanvas

class EMHeat(EMCore):

    def __init__(self, data,
                 continuous = True,

                 # discrete heat map
                 level2color = None,

                 # continuous heat map
                 cmap = 'jet',
                 norm = None,
                 interpolation = 'none',
                 
                 # x tick labels
                 xticklabels = None,
                 xtickposes = None,
                 xticklabel_fontsize = 10,
                 xticklabel_side = 'bottom',
                 xticklabel_rotat = 90,
                 xticklabel_pad=0.1,
                 xticklabel_shift=0,

                 # y tick labels
                 ytickposes = None,
                 yticklabels = None,
                 yticklabel_fontsize = 10,
                 yticklabel_side = 'l',
                 yticklabel_pad=0.1,

                 # data min max
                 dmin = None,
                 dmax = None,

                 alpha = 1,
             ):

        super(EMHeat, self).__init__()
        if isinstance(data, np.ndarray):
            data = pd.DataFrame(data)
        self.data = data
        self.nr, self.nc = self.data.shape
        import inspect
        ia = inspect.getargspec(EMHeat.__init__)
        for a in ia.args[-len(ia.defaults):]:
            setattr(self, a, locals()[a])

        if continuous:
            if self.dmin is None:
                self.dmin = self.data.values.min()
            if self.dmax is None:
                self.dmax = self.data.values.max()
        
    def plot(self):

        # plot stand-alone if ax is unset
        if self.ax is None:
            canvas = EMCanvas()
            canvas.add(self, dim=(0,0,1,1))
            canvas.plot()
            return

        if self.continuous:
            self.plot_continuous()
        else:
            self.plot_discrete()

        self.plot_xticklabels()
        self.plot_yticklabels()

    def plot_continuous(self):

        self.norm = mcolors.Normalize(vmin = self.dmin, vmax = self.dmax)
        self.ax.imshow(self.data.values, aspect='auto', origin='lower',
                       cmap=self.cmap, norm=self.norm, interpolation=self.interpolation, alpha=self.alpha)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def plot_discrete(self):

        levels = sorted(list(set(self.data.values.flatten())))
        if level2color is None:
            color = wzcolors.get_distinct_colors_rgb(len(levels))
            level2color = dict(zip(levels, colors))
        else:
            colors = [level2color[level] for level in levels]

        cmap = mcolors.ListedColormap(colors)
        bounds = np.arange(0.5, len(levels)+0.5, 1.0)
        norm = mcolors.BoundaryNorm(bounds, cmap.N)
        centers = [_+0.5 for _ in bounds]
        level2center = dict(zip(levels, centers))

        dataplot = data.applymap(lambda x: level2center[x])

        self.ax.imshow(dataplot, aspect='auto', origin='lower', cmap=cmap, interpolation='none', alpha=alpha)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def plot_xticklabels(self):

        if self.xticklabels is None:
            return
        
        # modify self.xtickposes to realize sub-sampling
        if self.xtickposes is None:
            self.xtickposes = range(self.data.shape[1])
            
        if type(self.xticklabels) == bool:
            self.xticklabels = self.data.columns.format()

        for i, pos in enumerate(self.xtickposes):
            
            if self.xticklabel_side in ['bottom', 'b']:
                self.ax.text(i+self.xticklabel_shift, -self.xticklabel_pad-0.5,
                             self.xticklabels[i],
                             rotation = self.xticklabel_rotat,
                             ha ='center',
                             va ='top',
                             fontsize = self.xticklabel_fontsize)
            elif self.xticklabel_side in ['top', 't']:
                self.ax.text(i+self.xticklabel_shift, self.xtickposes[-1]+self.xticklabel_pad+2.5,
                             self.xticklabels[i],
                             rotation = self.xticklabel_rotat,
                             ha = 'center',
                             va ='bottom',
                             fontsize = self.xticklabel_fontsize)
                
    def plot_yticklabels(self):

        if self.yticklabels is None:
            return

        # modify self.ytickposes to realize sub-sampling
        
        if self.ytickposes is None:
            self.ytickposes = range(self.data.shape[0])

        if type(self.yticklabels) == bool:
            self.yticklabels = self.data.index.format()

        for i, pos in enumerate(self.ytickposes):
            if self.yticklabel_side in ['left', 'l']:
                self.ax.text(-0.5-self.yticklabel_pad, pos,
                             self.yticklabels[i],
                             ha ='right',
                             va ='center',
                             fontsize=self.yticklabel_fontsize,
                             fontname='Arial Narrow')
            elif self.yticklabel_side in ['right', 'r']:
                self.ax.text(self.data.shape[1]+self.yticklabel_pad-0.5, pos,
                             self.yticklabels[i],
                             ha ='left',
                             va ='center',
                             fontsize=self.yticklabel_fontsize,
                             fontname='Arial Narrow')
