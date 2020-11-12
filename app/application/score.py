import random
import pandas as pd


def evaluate_score(filename):
    ground_truth = pd.read_csv("static/gt.csv")
    user = pd.read_csv(filename)
    x = user.join(ground_truth, how="right", lsuffix="lad_code", rsuffix="lad_code")
    a = x["imd_2019lad_code"]
    rmse = ((a.iloc[:,0] - a.iloc[:,1]) ** 2).mean() ** .5
    return (1-rmse)*100
