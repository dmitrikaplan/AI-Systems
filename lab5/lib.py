import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.utils import shuffle

from draw import draw_table


def preprocessing(df):
    processing_missing_values(df)
    normalize(df)


# обработка отсутвующих значений
def processing_missing_values(df):
    # обработка отсутвующих значений
    for column in df.columns:
        df[column].fillna(df[column].mean(), inplace=True)


def visualization(df):
    df.hist(bins=120, figsize=(30, 20))
    plt.show()


def normalize(df):
    for column in df.columns:
        max = df[column].max()
        min = df[column].min()

        normalized_list = []

        for x in df[column]:
            normalized_list.append(float(x - min) / (max - min))

        df[column] = normalized_list


def train_test_split(x, random_state=42, test_size=0.3):
    x_columns = x.columns
    x = x.to_numpy(copy=True)
    idxes = np.array(range(len(x)))

    test_size = round(test_size * len(x))

    np.random.shuffle(idxes)

    train_idx = idxes[test_size:len(x)]
    test_idx = idxes[:test_size]

    train = pd.DataFrame(x[train_idx, :], columns=x_columns)
    test = pd.DataFrame(x[test_idx, :], columns=x_columns)

    return (train.drop('Wine', axis=1), train['Wine'],
            test.drop('Wine', axis=1), test['Wine'])


def knn(x_train, y_train, x_test, columns, k):
    x_train = np.array(x_train[columns])
    y_train = np.array(y_train)
    x_test = np.array(x_test[columns])

    result = []

    for elem in x_test:
        norma = np.linalg.norm(x_train - elem,
                               axis=1)  # находит нормы эйлера (расстояние от тестовой точки до всех тренировочных)
        k_indexes = norma.argsort()[:k]  # получаем индексы k ближайших
        k_classes = y_train[k_indexes]
        unique_classes, counts = np.unique(k_classes,
                                           return_counts=True)  # получаем уникальные расстояния и их количество
        index_of_most_common = counts.argsort()[-1]  # индекс наиболее встречающегося
        result.append(unique_classes[index_of_most_common])

    return np.array(result)


def confusion_matrix(y_predict, y_train, n):
    matrix = np.zeros((n, n))

    for predict, train in zip(y_predict, y_train):
        matrix[int(predict * 2), int(train * 2)] += 1

    return matrix


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
    median = round(column_values.median(), 4)
    std = round(np.std(column_values), 4)
    min = round(column_values.min(), 4)
    max = round(column_values.max(), 4)
    (q25, q50, q75) = column_values.quantile([0.25, 0.5, 0.75])
    q25 = round(q25, 4)
    q50 = round(q50, 4)
    q75 = round(q75, 4)

    return [column_name, count, mean, std, median, min, max, q25, q50, q75]


def get_object(column_values, column_name):
    count = column_values.count()
    return [column_name, count, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']
