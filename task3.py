from plot_data import plot_data
import parser_data
import matplotlib.pyplot as plt

from util import *
def get_local_maxima(data_array):
    maxima = []
    for i in range(1,len(data_array)-2):
        if data_array[i-1]< data_array[i] and data_array[i+1]< data_array[i]:
            maxima.append(i)
    return maxima

def count_steps(data):
    print("Accelerometer data graph")
    plot_data(data)
    data = np.array(data)
    datapoints =  (data[:,1:])
    magnitudes = vector_magnitude(datapoints)
    plt.plot(magnitudes)
    filtered = moving_average(magnitudes,10)
    plt.show()

    plt.plot(filtered)
    plt.show()
    num_steps = 0
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''
    return int( len(get_local_maxima(filtered))/2)


def main():
    # Get data
    file_name = "walking_steps_2_cleaned.csv"  # Change to your file name
    data = parser_data.get_data(file_name)


    number_of_steps = count_steps(data)
    print ("Number of steps counted are :{0:d}".format(number_of_steps))

if __name__== "__main__":
  main()
