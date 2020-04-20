import matplotlib.pyplot as pyplot
import scipy as sc
import numpy as np
from curve import LBKinematics, MMCurve

if __name__=='__main__':
    input_1 = np.float_([0.0, 5.0, 7.0, 10.0, 16.0, 30.0, 50.0, 80.0, 120.0])
    input_2 = np.float_([3.4, 13.4, 16.1, 20.6, 25.3, 32.4, 38.4, 44.3, 48.4])
    plot_lb = LBKinematics.plot(input_1, input_2)
    plot_mm = MMCurve.plot(input_1, input_2)

    #plot_lb.add(plot_mm)

    plot_lb.show()