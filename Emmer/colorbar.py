from core import *
from heatmap import EMHeat
# # title
# label = None,
# labelside = 'r',
# labelspacing = 0.001,
# labelfontsize = 8,
# labelfontweight = 'light',

# # legend
# legend_title = None,
# legend_title_fontsize = 8,
# legend_label_fontsize = 8,


class EMCbar(EMHeat):

    def __init__(self, data,
                 orientation = 'h',
                 continuous = False,

                 # title
                 title = None,
                 title_side = 'l',
                 title_spacing = 0.001,
                 title_fontsize = 8,
                 title_fontweight = 'light',

                 # slanted annotation
                 lineanno = None,
                 annhei = None,
                 annlft = None,
                 annlen = 0.03,
                 anntan = 1,
                 
                 **kwargs
             ):

        if isinstance(data, pd.Series):
            _data = pd.DataFrame(data)
        else:
            _data = pd.DataFrame(pd.Series(data))
            
        if orientation in ['h','horizontal']:
            _data = _data.T

        EMHeat.__init__(self, _data, **kwargs)

    def plot(self):

        EMHeat.plot(self)

    # def plot_title

        # left, bottom, width, height = dim
        # top = bottom + height

        # if self.continuous:
        #     self.ax, self.norm, self.colormap = continuous_array_colorshow(self.data, dim, fig,
        #         orientation=orientation, cmap=self.cmap, dmin=self.dmin, dmax=self.dmax)
        # else:
        #     self.ax, self.label2color = discrete_colorshow(
        #         self.data, dim, fig, orientation=orientation, colors=self.colors, level2color=self.label2color)

        # if self.lineanno == 'topleft' and self.title is not None:
        #     if self.annhei is None and self.annlft is None:
        #         self.annlft = left - 0.05
        #         self.annhei = top + 0.05
        #     elif self.annhei is None:
        #         self.annhei = top + (left + width / 2. - self.annlft) * self.anntan
        #     elif self.annlft is None:
        #         self.annlft = left + width / 2. - (self.annhei - top)

        #     anno_lw = 0.5
        #     # slant line
        #     fig_add_line(fig, [self.annlft, left+width/2.], [self.annhei, top], linewidth=anno_lw)
        #     # horizontal line
        #     fig_add_line(fig, [self.annlft-self.annlen, self.annlft],
        #                  [self.annhei, self.annhei], linewidth=anno_lw)
        #     fig.text(self.annlft, self.annhei, self.title,
        #              fontsize = self.title_fontsize, fontweight = self.title_fontweight,
        #              horizontalalignment='right', verticalalignment='bottom')

        # elif self.title is not None:
        #     if orientation in ['vertical', 'v']:
        #         fig.text(left+width/2., top+topanno_pad, self.title, fontsize = self.title_fontsize, fontweight = self.title_fontweight,
        #                  horizontalalignment='center', verticalalignment='bottom', rotation=90)

        #     elif self.title_side == 'right' or self.title_side == 'r':
        #         fig.text(left + width + self.title_spacing,
        #                  bottom + height / 2., self.title,
        #                  fontsize = self.title_fontsize, fontweight = self.title_fontweight,
        #                  horizontalalignment = 'left', verticalalignment = 'center')
        #     elif self.title_side == 'left' or self.title_side == 'l':
        #         fig.text(left - self.title_spacing, bottom + height / 2., self.title,
        #                  fontsize = self.title_fontsize, fontweight = self.title_fontweight,
        #                  horizontalalignment = 'right', verticalalignment = 'center')
        #     else:
        #         raise Exception('Unacceptable title side %s' % self.title_side)

        # if self.pticklabels is not None:

        #     pl_inds = [_[0] for _ in self.pticklabels]
        #     pl_plots = text_reconcile(pl_inds, 10)
        #     ax = fig.add_axes([left-self.pticklabel_pad, bottom, self.pticklabel_pad, height], frameon=False)
        #     for _real, _plot in zip(pl_inds, pl_plots):
        #         ax.plot([1.0,0.6,0.4,0.], [_real, _real, _plot, _plot], color='k', lw=0.5)
        #     ax.set_ylim(0, len(self.data))
        #     ax.set_xlim(0,1)
        #     ax.set_yticks(pl_plots)
        #     ax.xaxis.set_tick_params(direction='in',width=0)
        #     ax.yaxis.set_tick_params(direction='in',width=0, pad=0)
        #     ax.set_yticklabels([_[1] for _ in self.pticklabels], fontsize=self.pticklabel_fontsize)
        #     ax.set_xticks([])

        # return

    # def plot_legend(self, dim=[0.1,0.1,0.03,0.4], fig=None, unitheight=0.015):

    #     """ plot legend of the color bar """

    #     if fig is None:
    #         fig = plt.figure()

    #     if isinstance(fig, tuple):
    #         fig = plt.figure(figsize=fig)

    #     kwargs = {}
    #     if self.legend_title is not None:
    #         kwargs['title'] = self.legend_title
    #     if self.legend_title_fontsize is not None:
    #         kwargs['title_fontsize'] = self.legend_title_fontsize
    #     if self.legend_label_fontsize is not None:
    #         kwargs['label_fontsize'] = self.legend_label_fontsize

    #     if self.continuous:
    #         continuous_colorshow_legend(self.norm, self.colormap, dim, fig,
    #                                     title = self.legend_title,
    #                                     title_fontsize = self.legend_title_fontsize)
    #     else:
    #         dim[-1] = unitheight*len(self.label2color)
    #         colorshow_legend(self.label2color, dim, fig, **kwargs)

    #     return
