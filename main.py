import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#fig = ff.create_distplot([data],["Math Scores"],show_hist=False)
#fig.show()

mean = statistics.mean(data)
print("Mean of the population",mean)

std_dev = statistics.stdev(data)
print("Standard Deviation of population",std_dev)

##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


# Function to get the mean of 100 data sets
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
print("Mean of Sampling distribution",mean)

std_deviation = statistics.stdev(mean_list)
print("Standard deviation of Sampling distribution",std_deviation)

##first_std_deviation_start, first_std_deviation_end = mean-std_deviation,  mean+std_deviation
#second_std_deviation_start, second_std_deviation_end = (2*mean-std_deviation),  (2*mean+std_deviation)
#third_std_deviation_start, third_std_deviation_end = (3*mean-std_deviation),  (3*mean+std_deviation)

#print("std1",first_std_deviation_start, first_std_deviation_end)
#print("std2",second_std_deviation_start, second_std_deviation_end)
#print("std3",third_std_deviation_start, third_std_deviation_end)

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_data1 = statistics.mean(data)
print("Mean of data1",mean_of_data1)


df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
mean_of_data2 = statistics.mean(data)
print("Mean of data2",mean_of_data2)

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_data3 = statistics.mean(data)
print("Mean of data3",mean_of_data3)


z_score = (mean_of_data1-mean)/std_deviation
print("z_score is ",z_score)

z_score = (mean_of_data2-mean)/std_deviation
print("z_score is ",z_score)

z_score = (mean_of_data3-mean)/std_deviation
print("z_score is ",z_score)