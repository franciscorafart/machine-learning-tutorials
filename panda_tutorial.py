import pandas as pd

city_name = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([84738,81298,284783])

#Creating a table/DataFrame with different columns
cities_table = pd.DataFrame({'city_names': city_name, 'Population': population})

california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=',')
print(california_housing_dataframe.describe())



