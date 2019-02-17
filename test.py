from plot_data import plot_data
import parser_data
import matplotlib.pyplot as plt

import parser_data
# numpy imported to check if the student has numpy
import numpy as np

data = parser_data.get_data("walking_steps_1_cleaned.csv")
data = np.array(data)
plot_data(data)
