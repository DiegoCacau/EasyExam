from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from time import  sleep
from decouple import config
from dashboard.models import Patient
from dashboard.views import auth_user
from django.contrib.auth.models import User


def login(driver):
    id_pass = "password"            # find_by_id
    id_login = "username"           # find_by_id
    id_login_button = "btn-primary"  # find_by_class
    login = config('ADMIN_USER')
    password = config('ADMIN_PASS')
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

    try:
        element=driver.find_element_by_xpath('//*[@id="sidebar"]/div')
    except NoSuchElementException:
        return False

    return True



def addPatient(driver, name, cpf, email, birthday, weight, height, gender):
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
    

    try:
        element=driver.find_element_by_xpath('//*[@id="content"]/ul/li')
        if(element.text != "Paciente cadastrado com sucesso!"):
            return False
    except NoSuchElementException:
        return False

    driver.get("http://127.0.0.1:8000/paciente/lista")
    sleep(5)

    return True


def login_unit():
    User.objects.create_user(username="aaaaa",
                first_name="aaaaa",
                last_name="aaaaa",
                password="111111",
                email="aaaaa@aaaaa.com")

    user = auth_user("aaaaa", "111111")

    if user is not None:
        user.delete()
    else:
        return False 

    return True


def init():
    driver = webdriver.Chrome(config('WEB_DRIVER')) 

    try:
        print("Caso de teste 1 - Login...", end=' ')
        if(login(driver)):
            print("Sucesso!")
        else:
            print("Falhou!")
            raise(NoSuchElementException)

        print("Caso de teste 2 - Adicionar Paciente...", end=' ')
        if(addPatient(driver, "Indiano Moreno", "15369844522",
            "India_IntelLover@saiAmd.com", "24/11/1922",
            "24", "2.11", "Masculino")):
            print("Sucesso!")

            patient = Patient.objects.get(cpf="15369844522")
            patient.delete()
        else:
            print("Falhou!")
            raise(NoSuchElementException)
        
        # addPatient("Diego Cacau", "15977963215", "cacau_doce@hotmail.com", "22/01/1975", "85", "1.95", "Feminino")
        
    except NoSuchElementException:
        pass

    finally:
        driver.close()



    print("Caso de teste 3 - Teste Unitário de Login...", end=' ')
    if(login_unit()):
        print("Sucesso!")
    else:
        print("Falhou!")
