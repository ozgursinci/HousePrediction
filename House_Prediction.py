import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn


file_path = "C:\\Users\\Asus\\Desktop\\House_Predict\\HousePricePrediction.xlsx"

df = pd.read_excel(file_path)

print(df.describe())