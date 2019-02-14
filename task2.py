import parser_data
from plot_data import plot_data
from constants import data_folder
import csv


def clean_data(data,start_index,end_index,clean_file_name):

    print ("Write code to remove garbage data")


    print ("Create new file without garbage data and save it in data folder")
    with open(data_folder+clean_file_name, 'w+') as outfile:
        for row in data[start_index:end_index]:
            outfile.write(','.join((map(str, row))))
            outfile.write("\n")





def main():
    # Get data
    file_name = "walking_steps_1.csv"  # Change to your file name
    data = parser_data.get_data(file_name) #data -- time,X,Y,Z
    clean_data(data,350,1113,'walking_steps_1_cleaned.csv')
    data = parser_data.get_data("walking_steps_1_cleaned.csv")
    plot_data(data)
    file_name = "walking_steps_2.csv"  # Change to your file name
    data = parser_data.get_data(file_name) #data -- time,X,Y,Z
    clean_data(data,200,1099,'walking_steps_2_cleaned.csv')
    data = parser_data.get_data("walking_steps_2_cleaned.csv")
    plot_data(data)


if __name__== "__main__":
  main()
