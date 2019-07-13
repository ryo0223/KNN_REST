import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
def knn_algo():
    model=KNeighborsClassifier(n_neighbors=1)
    """""
    with open("../../../../Documents/UJIndoorLoc/trainingData.csv", newline='') as csvfile:
        macdic=[]
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
            for i in range(row,step=2):
                if i in macdic:
                    macdic.append(i)"""
    busi=pd.read_csv("/home/ryo_nuc/Documents/Physics1@@.csv")
    lib=pd.read_csv("/home/ryo_nuc/Documents/LG27_0221_data@.csv")

    for i in lib.columns.values[:-1]:
        if i not in busi.columns.values[:-1]:
            busi.insert(1, i, 0)

    for i in busi.columns.values[:-1]:
        if i not in lib.columns.values[:-1]:
            lib.insert(1, i, 0)
    lib = lib.rename(columns={'BuildingID': 'BuildingID'})
    concateddata=pd.concat([lib.iloc[:,:],busi.iloc[:,:]])
    buildingactual=concateddata["BuildingID"]
    concateddata=concateddata.drop(['BuildingID'],axis=1)
    concateddata["BuildingID"]=buildingactual

    t=concateddata.iloc[:,:-1]
    t=t.min()
    minimum_in_database=t.min()
    concateddata1 =concateddata.iloc[:,:-1].mask(concateddata.iloc[:,:-1]==100,0)
    print(concateddata1.dtypes)
    concateddata1 =concateddata.iloc[:,:-1].mask(concateddata.iloc[:,:-1]!=0,concateddata.iloc[:,:-1]+abs(minimum_in_database))
    x=concateddata1.values
    y = concateddata.iloc[:,-1].values
    model.fit(x,y)
    print(concateddata.iloc[:20,:-1])
    prediction=model.predict(concateddata1.iloc[:20,:].values)
    actual=concateddata.iloc[:20,-1].values
    print(busi.head())
    print(sum(prediction==actual)/20)