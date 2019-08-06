import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def knn_algo(file,SSID):



    computing = [7, 8, 9, "Computing building"]
    pyshics = [11, "Physics building"]

    business = ["Business building"]
    all_building = [computing, pyshics, business]
    model = KNeighborsClassifier(n_neighbors=1)

    concateddata = pd.read_csv("./staticfiles/merged.csv")
    received_file = pd.read_csv("./media/"+file,error_bad_lines=False)
    #result, received_file = check_and_remove_location(received_file, "test")
    result=True #for development
    if result==True:
        for i in concateddata.columns.values[:]:
            if i not in received_file.columns.values[:]:
                received_file.insert(1, i, 0)

        for i in received_file.columns.values[:]:
            if i not in concateddata.columns.values[:]:
                concateddata.insert(1, i, 0)

        concateddata = concateddata.reindex(sorted(concateddata.columns), axis=1)
        received_file = received_file.reindex(sorted(concateddata.columns), axis=1)

        buildingactual = concateddata["BuildingID"]
        concateddata = concateddata.drop(['BuildingID'], axis=1)
        concateddata["BuildingID"] = buildingactual

        buildingactual = received_file["BuildingID"]
        received_file = received_file.drop(['BuildingID'], axis=1)
        received_file["BuildingID"] = buildingactual

        t = concateddata.iloc[:, :-1]
        t = t.min()
        minimum_in_database = t.min()

        concateddata1 = concateddata.iloc[:, :-1].mask(concateddata.iloc[:, :-1] != 0,
                                                       concateddata.iloc[:, :-1] + abs(minimum_in_database))
        x = concateddata1.values
        y = concateddata.iloc[:, -1].values

        # lg251_1 =lg251.iloc[:,:-1].mask(lg251.iloc[:,:-1]==100,0)

        lg251_1 = received_file.iloc[:, :-1].mask(received_file.iloc[:, :] != 0,
                                                  received_file.iloc[:, :] + abs(minimum_in_database))

        model.fit(x, y)

        # prediction=model.predict(concateddata1.iloc[:20,:].values)

        prediction = model.predict(lg251_1.iloc[:20, :].values)
        # actual=concateddata.iloc[:20,-1].values
        #actual = received_file.iloc[:20, -1].values
        S_prediction = pd.Series(prediction).value_counts(normalize=True)
        print(S_prediction)
        predicted_location = S_prediction.index[0]


        for i in all_building:
            if predicted_location in i:
                return i[-1]
    else:
        return "location not comfirmed"



def check_and_remove_location(file, SSID):
    if SSID in file.columns.values[:]:
        file = file.drop([SSID], axis=1)
        return (True, file)
    else:
        return (False,file)
