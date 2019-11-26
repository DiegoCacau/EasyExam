from time import  sleep
from selenium import webdriver

# here you must insert the path to the Selenium chromedriver
driver = webdriver.Chrome('/home/ronaldmaymone/chromedriver')  # Optional argument, if not specified will search path.

def login():
    id_pass = "password"            # find_by_id
    id_login = "username"           # find_by_id
    id_login_button = "btn-primary"  # find_by_class
    login = "iaguff"
    password = "@iaguff123456"
    driver.get('http://127.0.0.1:8000/login/')
    input_login = driver.find_element_by_id(id_login)
    input_pass = driver.find_element_by_id(id_pass)
    btn_login = driver.find_element_by_class_name(id_login_button)
    input_login.send_keys(login)
    sleep(1)
    input_pass.send_keys(password)
    sleep(1)
    btn_login.click()
    sleep(4)

    # driver.close()


def addPatient(name, cpf, email, birthday, weight, height, gender):
    driver.get("http://127.0.0.1:8000/paciente/lista")
    driver.get("http://127.0.0.1:8000/paciente/cadastro")
    input_name = driver.find_element_by_name("user_name")
    input_email = driver.find_element_by_name("user_email")
    input_cpf = driver.find_element_by_id("user_cpf")
    input_birth = driver.find_element_by_name("user_birthday")
    input_weight = driver.find_element_by_name("user_weight")
    input_height = driver.find_element_by_name("user_height")
    input_gender = driver.find_element_by_name("user_sex")
    btn_save = driver.find_element_by_id("emit-term-btn")
    input_name.send_keys(name)
    sleep(1)
    input_cpf.send_keys(cpf)
    sleep(1)
    input_email.send_keys(email)
    sleep(1)
    input_birth.send_keys(birthday)
    sleep(1)
    input_weight.send_keys(weight)
    sleep(1)
    input_height.send_keys(height)
    sleep(1)
    input_gender.send_keys(gender)
    sleep(2)
    btn_save.click()
    sleep(2)
    driver.get("http://127.0.0.1:8000/paciente/lista")
    sleep(5)


login()
addPatient("Indiano Moreno", "15369844522", "India_IntelLover@saiAmd.com", "24/11/1922", "24", "2.11", "Masculino")
addPatient("Diego Cacau", "15977963215", "cacau_doce@hotmail.com", "22/01/1975", "85", "1.95", "Feminino")
driver.close()
