import parser_data
from plot_data import plot_data
import pandas as pd
import numpy as np
def segment_climbing_walking(data):
    '''
    While collecting data on stairs there were times when you were also walking rather than climbing
    It is importing to remove the parts from the data where you were walking in between the flight of stairs
    Write your own algorithm to find segments in data which corresponds to climbing only

    This functions returns
    List of tuples (x,y,z) which corresponds to climbing only.
    i.e. remove data points from the original data which corresponds to walking
    '''

    print ('segment_climbing_walking')
    plot_data(data)

    return data


def count_steps(walk1):
    print ('count_steps')
    num_steps = 0
    denoised = walk1['BarometerSensor'].diff().values[375:1736]
    binarized = denoised < -0.008
    num_steps= np.count_nonzero(binarized)
    return num_steps


def main():
    # Get data
    file_name = "data/climb_steps_2.csv"  # Change this to your data file name
    walk1 = pd.read_csv(file_name)

    number_of_steps = count_steps(walk1)
    print ("Number of steps counted are :{0:d}".format(number_of_steps))


if __name__== "__main__":
  main()
