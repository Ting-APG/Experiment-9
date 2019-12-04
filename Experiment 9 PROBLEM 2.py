import pandas as pd
BoxData = {"Box": ["Box1", "Box1","Box1","Box2","Box2","Box2"], 
         "Dimension": ["Length","Width","Height","Length","Width","Height"],
         "Value": [6,4,2,5,3,4]}
BDataF = pd.DataFrame(BoxData, columns = ["Box", "Dimension", "Value"])
BDataFTidy = BDataF.pivot_table(index='Box', columns='Dimension', values='Value')
BDataFTidy['Volume'] = BDataFTidy['Height']*BDataFTidy['Length']*BDataFTidy['Width']