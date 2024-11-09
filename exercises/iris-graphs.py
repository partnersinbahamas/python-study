import modules.graphsModule as irisGraph

user_menu = """Please choose from the following options:

- Enter 'c' to chart a new graph.
- Enter 'q' to quit.

Your selection: """

charting_menu = "Enter the column you'd like to chart: "

graph_propmt = """Please choose type of creating graph:

- Enter 'd' to chart a new graph.
- Enter 'm' to chart a new multi-graph.

Your selection: """

def defineGraphType():
    user_selection = input(graph_propmt)
    handle_chart(True if user_selection == 'm' else False)

def get_iris_columns(index):
    try:
        columns = []
        with open('files/iris-flowers.csv', 'r') as flowers:
            flowers_content = flowers.readlines()[1:]

            for column in flowers_content:
                list_column = column.split(',')
                columns.append(list_column[index])
            return columns
         

    except (FileExistsError, FileNotFoundError):
        print('File do not exist.')

def handle_chart(multi):
    if multi:
        name_file = input('Please select a file graph name: ')

        with open('files/iris-flowers.csv', 'r') as flowers:
            columns_length = len(flowers.readlines()[0].split(','))
            print(columns_length)

            for n in range(0, columns_length - 1):
                y = [float(el) for el in get_iris_columns(int(n))]
                x = get_iris_columns(-1)

                irisGraph.create_graph(x, y, name_file, True)
    else:
        selected_column = input(charting_menu)
        x = get_iris_columns(-1)
        y = [float(el) for el in get_iris_columns(int(selected_column))]

        name_file = input('Please select a file graph name: ')
        irisGraph.create_graph(x, y, name_file, multi)


while True:
    user_selection = input(user_menu)

    if user_selection == 'c':
        defineGraphType()
    elif user_selection == 'q':
        break
    else:
        print(f'Selection "{user_selection}" is not a valid option.')
        break
