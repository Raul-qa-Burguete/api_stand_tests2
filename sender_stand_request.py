#Importar configuración inicial
import Configuration
import requests

import Data


#Inicio solicitud Get
def get_docs():
    return requests.get(Configuration.URL_SERVICE + Configuration.DOC_PATH)
response = get_docs()
print(response.status_code)
print(response.text)
#Solicitud Post (Solicitar alta de un nuevo usuario)
def post_new_user(body):
    return requests.post(Configuration.URL_SERVICE + Configuration.CREATE_USER_PATH,json=body,headers=Data.headers)
response = post_new_user(Data.user_body)
print(response.status_code)

def get_logs():
    return requests.get(Configuration.URL_SERVICE + Configuration.LOG_MAIN_PATH)
responses = get_logs()
print(responses.status_code)