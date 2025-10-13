#Deserializou 



import json 

dados_json = '{ "nome":"ana", "idade":25, "cidade":"São Paulo" }'

dados_py = json.loads(dados_json)

print(dados_py["nome"])
print(dados_py["idade"])