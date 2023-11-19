import time

import numpy as np


def determinationCoeff(y, predict_y):
    mean_y = np.mean(y)
    rss = np.sum(np.square(y - predict_y))
    tss = np.sum(np.square(y - mean_y))

    return 1 - rss / tss


def sumOfSquares(y, predict_y):
    return np.sum(np.square(y - predict_y))


def concat(x):
    return np.concatenate((np.ones((len(x), 1)), x), axis=1)


def train(x, y, columns):
    x = concat(np.array(x[columns]))
    y = np.array(y)
    return np.linalg.inv((x.T @ x)) @ x.T @ y  # определяет какие значения влияют на результат


def predict(x, beta, columns):
    return np.array(concat(x[columns])) @ beta.T


def linearRegression(x, y, columns):
    start_time = time.time()
    beta = train(x, y, columns)
    predict_y = predict(x, beta, columns)
    sum = sumOfSquares(y, predict_y)
   # print("Коэффициент детерминации: ", determinationCoeff(y, predict_y))
    #print("Сумма квадратов: ", sum)
    return time.time() - start_time, predict_y, sum
