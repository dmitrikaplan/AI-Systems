import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def draw_table(l):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.axis('tight')

    columns = ['Название', 'Кол-во', 'Ср. знач',
               'Cт. откл.', 'Медиана', 'Мин.',
               'Макc.', '25%', '50%', '75%']

    table = ax.table(cellText=l, colLabels=columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    fig.tight_layout()
    plt.show()


def draw_confusion_matrix(ax, matrix):
    ax.matshow(matrix)
    ax.set_xlabel('True class')
    ax.set_ylabel('Predicted class')

    for (i, j), z in np.ndenumerate(matrix):
        ax.text(j, i, str(int(z)), ha='center', va='center')

    plt.show()


def draw_3d(x_test, y_predict, columns):
    coord = x_test[columns].values.tolist()
    coord = list(zip(*coord[::-1]))

    x = coord[0]
    y = coord[1]
    z = coord[2]

    colors = y_predict

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter(x, y, z, c=colors)
    matplotlib.pyplot.show()
