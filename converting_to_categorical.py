"""converting to categorical.ipynb
"""

import numpy as np
import pandas as pd

data = pd.read_csv("/content/DATA FOR ANOVA - Sheet1.csv")
clean_data = data.dropna()

column_list = clean_data['WD'].tolist()

categorical_variable = []

for value in column_list:
    if value < 11.25 or value >= 348.75:
        categorical_value = "N"
    elif value < 33.75:
        categorical_value = "NNE"
    elif value < 56.25:
        categorical_value = "NE"
    elif value < 78.75:
        categorical_value = "ENE"
    elif value < 101.25:
        categorical_value = "E"
    elif value < 123.75:
        categorical_value = "ESE"
    elif value < 146.25:
        categorical_value = "SE"
    elif value < 168.75:
        categorical_value = "SSE"
    elif value < 191.25:
        categorical_value = "S"
    elif value < 213.75:
        categorical_value = "SSW"
    elif value < 236.25:
        categorical_value = "SW"
    elif value < 258.75:
        categorical_value = "WSW"
    elif value < 281.25:
        categorical_value = "W"
    elif value < 303.75:
        categorical_value = "WNW"
    elif value < 326.25:
        categorical_value = "NW"
    else:
        categorical_value = "NNW"

    categorical_variable.append(categorical_value)

clean_data["Direction"] = categorical_variable

df = pd.DataFrame({"PM 2.5": clean_data["PM 2.5"]})

clean_data["PM 2.5"] = normalized_data

clean_data.to_csv('output.csv', index=False)
