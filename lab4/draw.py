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


def visualization(df):
    df.hist(bins=60, figsize=[30, 20])
    plt.show()


