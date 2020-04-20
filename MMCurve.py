import numpy as np
from lmfit import minimize, Parameters
import matplotlib.pyplot as plt

class MMCurve(Curve):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    @staticmethod
    def residual(param, x, data):
        vmax = param['vmax'].value
        km = param['km'].value
        print(vmax)
        print(km)
        model = vmax * x / (km + x)
        return (data-model)

    @staticmethod
    def plot(sub_con, velocity):
        param = Parameters()
        param.add('vmax', value = 1., min = 0.)
        param.add('km', value = 1., min = 0.)

        out = minimize(MMCurve.residual, param, args = (sub_con, velocity))

        plt.plot(sub_con, velocity, 'bo')

        temp = np.float_(np.array(range(0,1200,12)))
        y = param['vmax'].value * temp / (param['km'].value + temp)
        plt.plot(temp, y, 'r-')
        return plt

# if __name__ == '__main__':
#     MMCurve.plot(np.float_([0.0, 5.0, 7.0, 10.0, 16.0, 30.0, 50.0, 80.0, 120.0]), np.float_([3.4, 13.4, 16.1, 20.6, 25.3, 32.4, 38.4, 44.3, 48.4]))