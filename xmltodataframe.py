import xml.etree.ElementTree as et
import pandas as pd

tree=et.parse('source1.xml')
root=tree.getroot()
dataframe = pd.DataFrame(columns=["name", "height", "weight"]) 
for person in root:
    name=person.find("name").text
    height=float(person.find("height").text)
    weight=float(person.find("weight").text)
    dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True)
    print(dataframe)