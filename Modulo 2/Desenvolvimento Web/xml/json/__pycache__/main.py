#Serializou


import json 

pythonValue = {'iscat': True, 'miceCaught':0, 'name':'zophie', 'felineIQ': None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)