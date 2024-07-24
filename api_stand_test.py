import sender_stand_request
import Data

# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_user_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = Data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body
#Test 1 Creación de un nuevo usuario
#Parametro con 2 caracteres
def test_create_user_with_2_letter_in_first_name():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)
    #Verifica si el resultado es 201
    assert user_response.status_code == 201
    #Verifica si se genera un Token con valor
    assert user_response.json()["authToken"] !=""
    #Valida que la información se encuentra en la tabla cargada adecuadamente
    users_table_response = sender_stand_request.get_docs()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 0


#Test 2 Crecion de nuevo usuario o usuaria
#El parametro "FirstName" contiene 15 caracteres
#Prueba positiva validar creación de usuario 15 digitos

def test_positive_name_whit_15_leters():
    user_body = get_user_body("Aaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code ==201
    assert user_response.json()["authToken"]!=""
    user_table_response = sender_stand_request.get_table_response()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert user_table_response.text.count(str_user)==1

#Prueba negativa nombres con 1 caracter
def test_negative_name_with_1_leter():
    user_body = get_user_body("a")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code ==400
    assert user_response.json()["code"]==400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

#negative prove with 16 letrers
def test_negative_name_with_16_letters():
    user_body = get_user_body("Aaaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code ==400
    assert user_response.json()["code"]==400
    assert user_response.json()["message"]=="El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

#negative prove with spaces
def test_negative_name_with_space():
    user_body = get_user_body("A Aaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code ==400
    assert user_response.json()["code"]==400
    assert user_response.json()["message"]== "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

#Negative pruve with special letters
def test_negative_name_with_special_characters():
    user_body = get_user_body("№%@")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code==400
    assert user_response.json()["code"]==400
    assert user_response.json()["message"]=="El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

#negative pruve with numbers in name
def test_negative_name_with_numbers():
    user_body = get_user_body("123")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code==400
    assert user_response.json()["code"]==400
    assert user_response.json()["message"]=="El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"

#negative pruve without name
def test_gegative_name_without_name():
    user_body = get_user_body("")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code==400
    assert user_response.json()["code"]==400
    assert user_response.json()["message"]=="No se enviaron todos los parámetros requeridos"

#negative prove with nombers as numbers
#definir variable
def test_negative_name_as_number():
#seleccionar fuentes
    user_body = get_user_body(123)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code==400
    assert user_response.json()["code"]==400