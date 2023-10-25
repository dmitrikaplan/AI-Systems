import pandas as pd

from lib import preprocessing, statistic, train_test_split


def main():
    df = pd.read_csv('Student_Performance.csv')
    # print(df.info())
    # statistic(df)
    preprocessing(df)

    x_train, x_test = train_test_split(df, random_state=42)

    print(x_train, x_test)

    # print(df.describe(include='all'))  ## показывает информацию о каждом поле датасета
    # print(df.info())  # вывод информацию о количестве non-null значений


if __name__ == '__main__':
    main()
