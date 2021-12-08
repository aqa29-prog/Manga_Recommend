# python class regarding file and array
class Regarding_file_array(object):
    def csvfile_open(self, file):
        import pandas as pd
        self.file = file
        df = pd.read_csv(file, encoding='utf-8', dtype=object).values.tolist()

        return df
    
    def textfile_open(file):
        # open file
        f = open(file, 'r')
        # read text data,one per line
        data = f.read().split('\n')
        # close file
        f.close()
        
        return data

    # convert 'str' to 'int' (two-dimensional array)
    def Converter_StrToInt_2dim(self, string):
        self.string = string
        integral = [[0 for j in range(len(string[0]))] for i in range(len(string))]
        for line in range(len(string)):
            for column in range(len(string[0])):
                if type(string[line][column]) == str:
                    integral[line][column] = int(string[line][column])

        return integral

    # Convert csv data to two-dimensional numpy array
    def Convert_csv_numpyarray(self, file):
        import numpy
        self.file = file
        df = self.csvfile_open(file)
        title_data = []
        evaluation_data = []
        for title in range(0,len(df)):
            # for evaluation in range(0,len(df[0])-1):
            title_data.append(df[title][0])
            df[title].pop(0)
            evaluation_data.append(df[title])
        
        # print(type(evaluation_data))
        evaluation_data = self.Converter_StrToInt_2dim(evaluation_data)
        # print(evaluation_data)
        data = numpy.array(evaluation_data)

        return data