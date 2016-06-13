import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

class EMCore(object):

    def __init__(self):

        self.dim = None
        self.ax = None
        self.nr = 1             # number of rows
        self.nc = 1             # number of columns

