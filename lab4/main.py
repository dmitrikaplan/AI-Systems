import pandas as pd

from draw import visualization
from lib import preprocessing, statistic, train_test_split
from LinearRegression import linearRegression


def main():
    df = pd.read_csv('Student_Performance.csv')

    # statistic(df)
    preprocessing(df)
    visualization(df)

    x_train, y_train, x_test, y_test = train_test_split(df, random_state=42)

    regressions = [(
        'Регрессия по всем колонкам', linearRegression(x_train, y_train, x_train.columns)
    ), (
        'Регрессия по Extracurricular Activities,Sleep Hours',
        linearRegression(x_train, y_train, ['Extracurricular Activities', 'Sleep Hours'])
    ),
        (
            'Регрессия по Hours Studied, Sample Question Papers Practiced',
            linearRegression(x_train, y_train, ['Hours Studied', 'Sample Question Papers Practiced'])
        )
    ]

    regressions.sort(key=lambda x: x[1][2])
    best_regression = regressions[0]
    name = best_regression[0]
    time, predict_y, sumOfSquares = best_regression[1]
    print('Имя лучшей регрессии: ', name)
    print('Сумма квадратов отклонений лучшей регрессии: ', sumOfSquares)
    print('Время лучшей регрессия: ', time, 'секунд')

    # print(df.describe(include='all'))  ## показывает информацию о каждом поле датасета
    # print(df.info())  # вывод информацию о количестве non-null значений


if __name__ == '__main__':
    main()
