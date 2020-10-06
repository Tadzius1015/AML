import pandas as pd


def read_data(file):
    return pd.read_csv(file)


def show_columns_info(dataframe):
    print("--------------------------------------------")
    print("Columns info:")
    print(dataframe.info())  # Shows columns info(name, each column records count, column type)


def show_unique_categories(dataframe):
    print("--------------------------------------------")
    print("Unique categories:")
    print(dataframe.Category.unique())


def show_unique_categories_values_count(dataframe):
    print("--------------------------------------------")
    print("Unique categories values count:")
    print(dataframe.Category.value_counts())


def filter_and_show_info_selected_category(dataframe, selected_category):
    filtered_data = dataframe[dataframe.Category == selected_category]
    print("--------------------------------------------")
    print("Unique categories values count:")
    print(filtered_data[['Title', 'Address', 'Price', 'Category']])


path = 'data.csv'
filter_category = 'NATURE'
data_array = read_data(path)
show_columns_info(data_array)
show_unique_categories(data_array)
show_unique_categories_values_count(data_array)
filter_and_show_info_selected_category(data_array, filter_category)
