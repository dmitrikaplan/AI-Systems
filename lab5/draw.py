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
