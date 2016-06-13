class DimGen(object):

    def __init__(self):

        self.dim = (0.,0.,1.,1.)

class DimUnit(DimGen):

    def __init__(self):

        super(DimUnit, self).__init__()

    def generate(self, canvas, yy):

        yy.dim = (0.,0.,1.,1.)

""" Edge anchors """

class RightOf(DimGen):

    def __init__(self, nm, pad=0.05):

        super(RightOf, self).__init__()
        self.nm = nm
        self.pad = pad

    def generate(self, canvas, yy):

        xx = canvas.x[self.nm]
        width = float(xx.dim[2]) / float(xx.nc) * float(yy.nc)
        height = xx.dim[3]
        
        width = max(width, 0.05)
        height = max(height, 0.05)
        
        left = xx.dim[0]+xx.dim[2]+self.pad
        bottom = xx.dim[1]
        yy.dim = (left, bottom, width, height)

class LeftOf(DimGen):

    def __init__(self, nm, pad=0.05):

        super(LeftOf, self).__init__()
        self.nm = nm
        self.pad = pad

    def generate(self, canvas, yy):

        xx = canvas.x[self.nm]
        width = float(xx.dim[2]) / float(xx.nc) * float(yy.nc)
        height = xx.dim[3]
        
        width = max(width, 0.05)
        height = max(height, 0.05)
        
        left = xx.dim[0]-self.pad-width
        bottom = xx.dim[1]
        yy.dim = (left, bottom, width, height)

class TopOf(DimGen):

    def __init__(self, nm, pad=0.05):

        super(TopOf, self).__init__()
        self.nm = nm
        self.pad = pad

    def generate(self, canvas, yy):

        xx = canvas.x[self.nm]
        width = xx.dim[2]
        height = float(xx.dim[3]) / float(xx.nr) * float(yy.nr)

        width = max(width, 0.05)
        height = max(height, 0.05)

        bottom = xx.dim[1]+xx.dim[3]+self.pad
        left = xx.dim[0]
        yy.dim = (left, bottom, width, height)

class Beneath(DimGen):

    def __init__(self, nm, pad=0.05):

        super(Beneath, self).__init__()
        self.nm = nm
        self.pad = pad

    def generate(self, canvas, yy):

        xx = canvas.x[self.nm]
        width = xx.dim[2]
        height = float(xx.dim[3]) / float(xx.nr) * float(yy.nr)

        width = max(width, 0.05)
        height = max(height, 0.05)

        bottom = xx.dim[1]+xx.dim[3]+self.pad
        left = xx.dim[0]
        yy.dim = (left, bottom, width, height)


