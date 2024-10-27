
# Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.

def csvFileToDictFormat(path):
  try:
    with open(path) as flowers:

        irises = []
        file_content = flowers.readlines()

        headers = file_content[0].split(',')

        for row in file_content:
            zipped = zip(headers, row.strip().split(','))

            irises.append(zipped)
        return irises
  except FileNotFoundError:
    print('File not found.')


def zipToCsvFileFormat(zipped):
    try:
        with open('files/zip-csv.csv', 'w') as file:
            for z in zipped:
                line = []
                for _, value in z:
                    line.append(value)
                file.write(str(','.join(line) + '\n'))
    except FileNotFoundError:
        print('File not found.')

zipToCsvFileFormat(csvFileToDictFormat('files/iris-flowers.csv'))

