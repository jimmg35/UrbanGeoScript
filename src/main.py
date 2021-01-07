import os
import pandas as pd 
from os import listdir


##################
#   @self.multiClassData
#   3_classes
#   

class Parameter():
    DATA_PATH = r'D:\UrbanGeo\cleanData'
    CODBASE = "最小統計區代碼"
    DATA_COLUMN = ["0-14歲人口數" ,"15-64歲人口數", "65歲以上人口數"]

class Converter(Parameter):
    def __init__(self):
        self.data_path = [os.path.join(self.DATA_PATH, i) for i in listdir(self.DATA_PATH)]
        # MultiYear data (104~108)
        self.data_set = [pd.read_csv(i) for i in self.data_path]
    
    def extract_data(self):
        self.multiClassData = []
        for clmn in self.DATA_COLUMN:
            temp = []
            for i in range(0, len(self.data_set)):
                year_data = list(self.data_set[i][clmn])
                for j in range(0, len(year_data)):
                    if self.isNaN(j):
                        year_data[j] = 0
                temp.append(year_data)
            self.multiClassData.append(temp)
        
    def cal_yearly_delta(self):
        out = []
        for i in range(0, len(self.multiClassData)):
            temp = []
            for j in range(1, len(self.data_set)):
                result = self.column_subtract(self.multiClassData[i][j-1], self.multiClassData[i][j])
                temp.append(result)
            out.append(temp)
        return out
        
    def column_subtract(self, f, t):
        out = []
        for i in range(0, len(f)):
            out.append(t[i] - f[i])
        return out            
    
    def output_delta_csv(self, data):
        out = {}
        d = []
        columns = []
        
        for i in range(0, len(self.DATA_COLUMN)): # for a class
            for j in range(0, len(data[i])): # for years
                columns.append('d'+self.DATA_COLUMN[i]+'_'+str(j+4)+'to'+str(j+5))
                print('d'+self.DATA_COLUMN[i]+'_'+str(j+4)+'to'+str(j+5))
        
        for i in range(0, len(data)):
            for j in range(0, len(self.data_set)-1):
                d.append(data[i][j])
        
        for i in range(0, len(columns)):
            out[columns[i]] = d[i]
         
        for i in range(0, len(d)):
            for j in range(0, len(d[i])):
                if self.isNaN(d[i][j]):
                    d[i][j] = 0

        out["CODEBASE"] = self.data_set[0][self.CODBASE]
        processed = pd.DataFrame(data=out)
        processed.to_csv('output.csv')
    
    def isNaN(self, num):
        return num != num
            
        
if __name__ == '__main__':
    
    CT = Converter()
    CT.extract_data()
    t = CT.cal_yearly_delta()
    CT.output_delta_csv(t)
    
     