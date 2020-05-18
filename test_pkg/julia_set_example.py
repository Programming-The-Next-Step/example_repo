import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import colorsys

class fractal:

    im_width  = 320
    im_height = 320
    fractal   = None

    def _check_size(self):
        if self.im_width <= 0 or self.im_height <= 0:
            raise ValueError("im_width and im_height should be positive!")

    def compute(self):
        raise NotImplementedError("subclasses should overwrite the compute method!")

    def plot(self):

        if self.fractal is None:
            self.compute()

        fig, ax = plt.subplots()
        ax.imshow(self.fractal, interpolation='nearest', cmap=cm.hot)
        plt.axis('off')
        plt.show()

class julia_set(fractal):
    def __init__(self):
        # adapted from https://scipython.com/book/chapter-7-matplotlib/problems/p72/the-julia-set/
        
        self.c = complex(-0.1, 0.65)
        self.zabs_max = 10
        self.nit_max = 50
        self.xmin, self.xmax = -1.5, 1.5
        self.xwidth = self.xmax - self.xmin
        self.ymin, self.ymax = -1.5, 1.5
        self.yheight = self.ymax - self.ymin

    def compute(self):
        if self.fractal is None:
            self._check_size()
            self.fractal = np.zeros((self.im_width, self.im_height))
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
                    self.fractal[ix,iy] = self.ratio

    
class mandelbrot_set(fractal):

    def __init__(self):
        # adadpted from https://www.geeksforgeeks.org/mandelbrot-fractal-set-visualization-in-python/
        self.nit_max = 50
        
    def rgb_conv(self, i): 
        color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
        return tuple(color.astype(int)) 
  
    def mandelbrot(self, x, y): 
        c0 = complex(x, y) 
        c = 0
        for i in range(1, self.nit_max): 
            if abs(c) > 2: 
                return i / self.nit_max #self.rgb_conv(i) 
            c = c * c + c0 
        return 1#(0, 0, 0) 

    def compute(self):
        if self.fractal is None:
            self._check_size()
            self.fractal = np.zeros((self.im_width, self.im_height))
            width = self.im_width
            for x in range(self.im_width):
                for y in range(self.im_height):
                    value = self.mandelbrot((x - (0.75 * width)) / (width / 4), (y - (width / 4)) / (width / 4))
                    self.fractal[x, y] = value
        
# mb = mandelbrot_set()
# mb.plot()

# js = julia_set()
# js.plot()


# Try catch example
#try:
#    mb = mandelbrot_set()
#    mb.im_height = -1
#    mb.plot()
#except ValueError:
#    print("A value error occured")
#except:
#    print("An error occured")
#else:
#    print("No error occured")
#finally:
#    print("End.")
