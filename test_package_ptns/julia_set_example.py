# adapted from https://scipython.com/book/chapter-7-matplotlib/problems/p72/the-julia-set/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class julia_set:
    def __init__(self):
        self.im_width, self.im_height = 300, 300
        self.c = complex(-0.1, 0.65)
        self.zabs_max = 10
        self.nit_max = 1000
        self.xmin, self.xmax = -1.5, 1.5
        self.xwidth = self.xmax - self.xmin
        self.ymin, self.ymax = -1.5, 1.5
        self.yheight = self.ymax - self.ymin
        self.julia = None
    
    def compute_julia_set(self):
        if self.julia is None:
            self.julia = np.zeros((self.im_width, self.im_height))
            for ix in range(self.im_width):
                for iy in range(self.im_height):
                    nit = 0
                    # Map pixel position to a point in the complex plane
                    z = complex(ix / self.im_width  * self.xwidth  + self.xmin,
                                iy / self.im_height * self.yheight + self.ymin)
                    # Do the iterations
                    while abs(z) <= self.zabs_max and nit < self.nit_max:
                        z = z**2 + self.c
                        nit += 1
                    self.shade = 1-np.sqrt(nit / self.nit_max)
                    self.ratio = nit / self.nit_max
                    self.julia[ix,iy] = self.ratio


    def plot(self):

        if self.julia is None:
            self.compute_julia_set()

        fig, ax = plt.subplots()
        ax.imshow(self.julia, interpolation='nearest', cmap=cm.hot)
        # Set the tick labels to the coordinates of z0 in the complex plane
        xtick_labels = np.linspace(self.xmin, self.xmax, int(self.xwidth / 0.5))
        ax.set_xticks([(x-self.xmin) / self.xwidth * self.im_width for x in xtick_labels])
        ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
        ytick_labels = np.linspace(self.ymin, self.ymax, int(self.yheight / 0.5))
        ax.set_yticks([(y-self.ymin) / self.yheight * self.im_height for y in ytick_labels])
        ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])
        plt.show()
