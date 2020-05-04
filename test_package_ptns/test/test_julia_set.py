import unittest
import numpy as np

from test_package_ptns.julia_set_example import julia_set

class TestSum(unittest.TestCase):

    def test_compute(self):
        obj = julia_set()
        obj.im_width, obj.im_height = 5, 5
        obj.compute_julia_set()
        self.assertAlmostEqual(
            obj.julia.tolist(),
            np.array([[0.002, 0.002, 0.003, 0.003, 0.003],
                      [0.002, 0.003, 0.004, 0.007, 0.008],
                      [0.003, 0.005, 0.231, 0.54,  0.007],
                      [0.003, 0.007, 0.54,  0.231, 0.005],
                      [0.003, 0.008, 0.007, 0.004, 0.003]]).tolist()
        )

    def test_initialized_is_none(self):
        obj = julia_set()
        self.assertIs(obj.julia, None)


if __name__ == '__main__':
    unittest.main()
