import csv
import pandas as pd
import statistics
import plotly.express as px
import random


df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
data_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("data mean : ", data_mean)
print("data standard deviation : ", std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)    

def show_fig(mean_list):
    df = mean_list
    fig = px.create_distplot([df], ["reading_time"], show_hist = False)

    fig.show()

