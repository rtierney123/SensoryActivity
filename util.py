from scipy.signal import butter, lfilter
import numpy as np

def vector_magnitude(data):
    """ function to calculate the magnitude of a vector

    Calculate the magnitude of the vector superposition of data (for
    example, acceleration) on x, y, and z axis

    Arguments:
        data: array of (x, y, z) tuples for a vector

    Returns:
        arra of the magnitude of a vector

    """
    magnitude_data = []
    for vector in data:
        magnitude = 0.0
        for dim in vector:
            magnitude += dim**2
        magnitude_data.append(magnitude**0.5)
    return np.array(magnitude_data)


def moving_average(data, window_size):
    """ moving average filter

    Implement a simple moving average filter to use as a low pass
    filter

    Arguments:
        data: data be filtered
        window_size: window_size chosen for the data

    Returns:
        The filtered data.

    TODO:
        Finish this function. Think about how you want to handle
        the size difference between your input array and output array.
        You can write it yourself or consider using numpy.convole for
        it:
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html

    """

    return np.convolve(data, np.ones((window_size,))/window_size, mode='same')
