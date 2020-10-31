# Name: Josie Omel
# Date: 10/26/2020
# Description: A class named SatData that reads a JSOn file and writes that data to a text file in CSV format.

import json


class SatData:
    """SatData class"""

    def __init__(self):
        """init method that reads the file"""

        with open('sat.json', 'r') as file:  # reads the json file
            self.data = json.load(file)['data']

    def save_as_csv(self, dbns):
        s_data = []  # database storage location
        for data in self.data:
            if data[6] in dbns:
                s_data.append(data)

        with open('output.csv', 'w') as file:
            header = [str(i) for i in range(len(d_data[0]))]  # adding a row for column header
            file.write(','.join(header))
            file.write('\n')  # creating a new row

            for row in s_data:
                r_data = []
                for item in row:
                    if ',' in str(item):
                        r_data.append("\"" + item + "\"")
                    else:
                        r_data.append(str(item))
                file.write(','.join(r_data))
                file.write('\n')
