from plot_data import plot_data

import parser_data
# numpy imported to check if the student has numpy
import numpy

data = parser_data.get_data("walking_steps_2_cleaned.csv")
plot_data(data)
