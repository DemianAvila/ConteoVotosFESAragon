#libreria para hacer webscrap, para consultar los documentos alojados en drive
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os.path
import time


#funcion que abre el documento y lo almacena temporalmente como imagen
def obtenerDocumento(link, file):
    #variable que verifica si la foto existe
    existe=False
    driver = webdriver.Chrome()
    driver.get(link)
    #ndfHFb-c4YZDc-cYSp0e-DARUcf-PLDbbf -> class de la primera pagina de todos los documentos de identificacion
    #documento=driver.find_element_by_class_name("ndfHFb-c4YZDc-cYSp0e-DARUcf-PLDbbf")
    extensionArchivo=driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[1]/div[2]/div[1]").text
    extensionArchivo=str(extensionArchivo)
    print(extensionArchivo)
    time.sleep(18)
    #acercar los archivos
    if extensionArchivo.endswith(".pdf"):
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div[3]").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div[3]").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div[3]").click()
    time.sleep(12)
    driver.save_screenshot(f"{file}.png")
    driver.quit()

