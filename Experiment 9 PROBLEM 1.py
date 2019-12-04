import pandas as pd
Data1 = {"Student": ["Ice Bear","Panda","Grizzly"], "Math":[80,95,79]}
Data1 = pd.DataFrame(Data1, columns=["Student","Math"])
Data2 = {"Student": ["Ice Bear","Panda","Grizzly"], "Electronics":[85,81,83]}
Data2 = pd.DataFrame(Data2, columns=["Student","Electronics"])
Data3 = {"Student": ["Ice Bear","Panda","Grizzly"], "GEAS":[90,79,93]}
Data3 = pd.DataFrame(Data3, columns=["Student","GEAS"])
Data4 = {"Student": ["Ice Bear","Panda","Grizzly"], "ESAT":[93,89,88]}
Data4 = pd.DataFrame(Data4, columns=["Student","ESAT"])
Merged1 = pd.merge(Data1,Data2, on='Student')
Merged2 = pd.merge(Data3,Data4, on='Student')
Merged3 = pd.merge(Merged1,Merged2, on='Student')
Melted = pd.melt(Merged3,id_vars=['Student'],value_vars=['Math','Electronics','GEAS','ESAT']
,value_name = 'Grades',var_name = 'Subject')
MeltedSorted = Melted.sort_values(by=['Subject','Grades'],ascending=False)