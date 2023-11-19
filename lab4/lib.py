import pandas as pd
import numpy as np
from sklearn.utils import shuffle

from draw import draw_table, visualization


# предобратока данных
def preprocessing(df):
    # кодирование категориальных признаков
    df['Extracurricular Activities'] = np.where(df['Extracurricular Activities'] == 'Yes', 1, 0)

    processing_missing_values(df)
    normalize(df)


# обработка отсутвующих значений
def processing_missing_values(df):
    # обработка отсутвующих значений
    for column in df.columns:
        df[column].fillna(df[column].mean(), inplace=True)


# нормировка значений по столбцу
def normalize(df):
    for column in df.columns:
        max = df[column].max()
        min = df[column].min()

        normalized_list = []

        for x in df[column]:
            normalized_list.append(float(x - min) / (max - min))

        df[column] = normalized_list


def statistic(df):
    l = []
    for i in df.columns:
        if df[i].dtype == 'int64' or df[i].dtype == 'float64':
            data = get_number(df[i], i)
            l.append(data)
        else:
            data = get_object(df[i], i)
            l.append(data)

    draw_table(l)


def get_number(column_values, column_name):
    count = column_values.count()
    mean = round(column_values.mean(), 4)
    median = column_values.median()
    std = round(np.std(column_values), 4)
    min = column_values.min()
    max = column_values.max()
    (q25, q50, q75) = column_values.quantile([0.25, 0.5, 0.75])

    return [column_name, count, mean, std, median, min, max, q25, q50, q75]


def get_object(column_values, column_name):
    count = column_values.count()
    return [column_name, count, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']


def train_test_split(x, test_size=0.3, random_state=42):
    x_columns = x.columns
    x = x.to_numpy()
    idxes = np.array(range(len(x)))

    test_size = round(test_size * len(x))

    shuffle(idxes, random_state=random_state)

    train_idx = idxes[test_size:len(x)]
    test_idx = idxes[:test_size]

    train = pd.DataFrame(x[train_idx, :], columns=x_columns)
    test = pd.DataFrame(x[test_idx, :], columns=x_columns)

    return (train.drop('Performance Index', axis=1), train['Performance Index'],
            test.drop('Performance Index', axis=1), test['Performance Index'])

