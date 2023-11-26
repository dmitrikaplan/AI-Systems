import random

import matplotlib
import numpy as np
from matplotlib import pyplot as plt, colors

from draw import draw_confusion_matrix, draw_3d
from lib import train_test_split, confusion_matrix, knn


def fixed_set_of_features(df):
    train_x, y_train, x_test, y_test = train_test_split(df)
    n = len(np.unique(df['Wine']))

    for i, k in enumerate([3, 5, 10], 1):
        y_predict = knn(train_x, y_train, x_test, train_x.columns, k)
        cm = confusion_matrix(y_predict, y_test, n)

        ax = plt.subplot()
        ax.set_title('K = %d' % k)

        draw_confusion_matrix(ax, cm)


def random_set_of_features(df):
    train_x, y_train, x_test, y_test = train_test_split(df)
    n = len(np.unique(df['Wine']))

    columns = np.random.choice(train_x.columns, 3, replace=False)
    print('Случайно выбранные колонки: ', '\n'.join(columns))

    for i, k in enumerate([3, 5, 10], 1):
        y_predict = knn(train_x, y_train, x_test, columns, k)
        cm = confusion_matrix(y_predict, y_test, n)

        ax = plt.subplot()
        ax.set_title('K = %d' % k)

        draw_confusion_matrix(ax, cm)
        draw_3d(x_test, y_predict, columns)

