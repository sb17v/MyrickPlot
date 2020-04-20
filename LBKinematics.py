import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt
import Curve

class LBKinematics(Curve):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    @staticmethod
    def plot(sub_con, velocity):
        rec_sub_con = np.reciprocal(sub_con)
        rec_velocity = np.reciprocal(velocity)

        slope, intercept, rvalue, pvalue, std_err = sc.linregress(rec_sub_con, rec_velocity)

        x = np.linspace(np.min(rec_sub_con - 100), np.max(rec_sub_con + 100))

        for i in x:
            y = (slope * x) + intercept

        plt.scatter(intercept, 0, color='Blue')
        
        intercept_x = ((0 - intercept)/slope)
        plt.scatter(intercept_x, 0, color='red')
        Km = (-1 / intercept_x)

        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        plt.scatter(rec_sub_con, rec_velocity)

        #Graph linear regresison
        plt.plot(x, y)

        #Titles and labels
        plt.xlabel('1/[S] ($\mu$M)')
        plt.ylabel('1/v ($\mu$M/s)')
        plt.title('Lineweaver-Burk')

        return plt

# if __name__ == '__main__':
#     LBKinematics.plot([0.0, 5.0, 7.0, 10.0, 16.0, 30.0, 50.0, 80.0, 120.0], [3.4, 13.4, 16.1, 20.6, 25.3, 32.4, 38.4, 44.3, 48.4])