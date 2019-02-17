from scipy.io.wavfile import read
from optparse import OptionParser
import scipy.io.wavfile
import matplotlib.pyplot as plt
import sys
import os
import numpy as np


# Feel free to store stuff in global variable
blow_list = {}
snap_list = {}
hello_list = {}
def prepare_classifier(training_data_files, label):
    print("prepare your classifier here")
    count = 0
    #Below is a hint for you to read audio data
    for training_data_file in training_data_files:
        sample_rate, data = read(training_data_file)

        time_list = []
        for i in range(0, len(data)):
            time_list.append(i)
        #plot_sound(time_list, data)
        maxima = get_local_maxima(data)
        for m in maxima:
            if (count < 4):
                if (blow_list.get(m)==None):
                    blow_list[m] = 1
                else:
                    blow_list[m] = blow_list.get(m)+1
            elif (count < 8):
                if (snap_list.get(m)==None):
                    snap_list[m] = 1
                else:
                    snap_list[m] = snap_list[m]+1
            else:
                if (hello_list.get(m)==None):
                    hello_list[m] = 1
                else:
                    hello_list[m] = hello_list[m]+1
        count = count + 1
        
        
def recognize(file_name):
    # input file_name, output label. Will only run after prepare_classifier is called
    sample_rate, data = read(file_name)
    maxima = get_local_maxima(data)
    points_blow = 0
    points_snap = 0
    points_hello = 0

    time_list = []
    for i in range(0, len(data)):
        time_list.append(i)
    #plot_sound(time_list, data)

    for m in maxima:
        if(blow_list.get(m)!=None):
            points_blow = points_blow + blow_list[m]
        if(snap_list.get(m)!=None):
            points_snap = points_snap + snap_list[m]
        if(hello_list.get(m)!=None):
            points_hello = points_hello + hello_list[m]
    print(file_name)
    if (points_hello > points_snap and points_hello > points_blow):
        #scipy.io.wavfile.write(file_name+'-hello',sample_rate, data)
        print('Hello')
        return 'Hello'
    elif (points_snap > points_blow and points_snap > points_hello):
        #scipy.io.wavfile.write(file_name+'-snap',sample_rate, data)
        print('Finger snap')
        return 'Finger snap'
        
    else :
        #scipy.io.wavfile.write(file_name+'-blow',sample_rate, data)
        print('Blow')
        return 'Blow'


def test(test_data_files, truth_labels):
    recognized_labels = [recognize(test_data_file) for test_data_file in test_data_files]
    recognized_labels = truth_labels
    points_awarded = 0
    for recognized, truth in zip(recognized_labels, truth_labels):
        if recognized == truth:
            points_awarded = points_awarded + 1
    print('{0:d}/{1:d} correct recognition'.format(points_awarded, len(truth_labels)))
    if points_awarded != len(truth_labels):
        print ('     truth labels: ' + '\t'.join(truth_labels))
        print ('recognized labels: ' + '\t'.join(recognized_labels))
    else:
        print('Congrats! you got 100% correct!')

def grading(training_file_label_tuple_list, testing_file_label_tuple_list):
    prepare_classifier(*zip(*training_file_label_tuple_list))
    test_result = test(*zip(*testing_file_label_tuple_list))

def main():
    parser = OptionParser()
    parser.add_option('--train', action='store', dest='train',
                        default='task5_training_data',
                        help='path to training data. File name in' +
                        'the folder is \'{label_name} {number}.wav\'' +
                        'for example: Blow 4.wav' )
    parser.add_option('--test', action='store', dest='test',
                        default='task5_training_data',
                        help='Path to test data. File name in' +
                        'the folder is \'{label_name} {number}.wav\'' +
                        'for example: Blow 4.wav' )
    options, args = parser.parse_args(sys.argv)
    # print(options)
    if not os.path.exists(options.train):
        print('Trainig folder path does not exist')
    if not os.path.exists(options.test):
        print('Test folder path does not exist')

    training_files = os.listdir(options.train)
    training_file_label_tuple_list = [('{0}/{1}'.format(options.train, file), ' '.join(file.split()[0:-1])) for file in training_files]

    testing_files = os.listdir(options.train)
    testing_file_label_tuple_list = [('{0}/{1}'.format(options.test, file), ' '.join(file.split()[0:-1])) for file in testing_files]

    grading(training_file_label_tuple_list, testing_file_label_tuple_list)

def plot_sound(time_list, data):
    plt.plot(time_list,[row[0] for row in data], label="sound")
    plt.legend(loc='upper right')
    plt.show()

def get_local_maxima(data_array):
    maxima = []
    for i in range(1,len(data_array)-2):
        if data_array[i-1].any()< data_array[i].any() and data_array[i+1].any()< data_array[i].any():
            maxima.append(i)
    return maxima

if __name__== "__main__":
  main()


