
import pandas as pd
class csvReader():

    def __init__(self):
        #Leer todos los ficheros csv como matrices
        OGcsv=[]
        OGcsv.append(pd.read_csv('Original_Data/gt_2011.csv'))
        OGcsv.append(pd.read_csv('Original_Data/gt_2012.csv'))
        OGcsv.append(pd.read_csv('Original_Data/gt_2013.csv'))
        OGcsv.append(pd.read_csv('Original_Data/gt_2014.csv'))
        OGcsv.append(pd.read_csv('Original_Data/gt_2015.csv'))

        #Concatenar los datos
        self.ogData = pd.concat([OGcsv[0], OGcsv[1], OGcsv[2], OGcsv[3], OGcsv[4]], axis=0, ignore_index=True)


        # Convertir DataFrame a matriz de valores

        print(self.ogData.min())
    def _getMaxMin(self):
        return self.ogData.max().values, self.ogData.min().values


    def getNormalized(self):
        normData = self.ogData.values

        maxCol, minCol = self._getMaxMin()

        for i in range(len(normData)):
            for j in range(len(normData[i])):
                normData[i][j]=(normData[i][j]-minCol[j])/(maxCol[j]-minCol[j])

        normData=pd.DataFrame(normData)
        normData.columns=self.ogData.columns
        return normData

    def randomizeData(self):

        return self.getNormalized().sample(frac=1, random_state=0, ignore_index=True)

    def splitData(self):

        trainingData, validationData = self.randomizeData().split()


if __name__ == '__main__':
    a= csvReader()
    print(a.randomizeData())
