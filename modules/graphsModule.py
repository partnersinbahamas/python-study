from matplotlib import pyplot

def create_graph(x, y, name, multi):
    if multi:
        pyplot.scatter(x, y, alpha=0.5)
        pyplot.savefig(f'graphs/{name}.png')
    else:
        figure = pyplot.figure()
        pyplot.scatter(x, y, alpha=0.5)
        figure.savefig(f'graphs/{name}.png')