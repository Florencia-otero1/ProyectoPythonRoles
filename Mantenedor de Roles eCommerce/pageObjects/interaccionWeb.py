from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import time
import time
import pandas as pd
from pageObjects.config import *
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.registroProceso import *

class InteraccionWeb:
    # elementos para login
    __tbx_email = (By.XPATH, '//*[@id="mat-input-0"]')
    __btn_continuar_login = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-login/div/div/div/div[1]/div[1]/ml-login/div[2]/mat-card/div[3]/p/at-button/at-basic-button/button')
    __tbx_password = (By.XPATH, '//*[@id="mat-input-2"]')
    __btn_ingresar_login = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-login/div/div/div/div[1]/div[1]/ml-login/div[2]/mat-card/div[3]/p/at-button/at-basic-button/button')

    # elementos para ingreso nuevos roles
    __btn_crear_rol = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/grid-admin-rol/div/div/div[1]/div[2]/div[4]/button')
    __tbx_nombre_rol = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[2]/step-data-roles/div/div/div/form/div/div[1]/div/at-input/mat-form-field/div/div[1]/div[1]/input')
    __btn_es_corredor = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[2]/step-data-roles/div/div/div/form/div/div[3]/div[1]/mat-radio-button')
    __btn_no_es_corredor = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[2]/step-data-roles/div/div/div/form/div/div[3]/div[1]/mat-radio-button')
    __tbx_rut_corredor = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[2]/step-data-roles/div/div/div/form/div/div[4]/div[2]/div[1]/at-input/mat-form-field/div/div[1]/div[1]/input')
    __btn_rol_esta_activo = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[2]/step-data-roles/div/div/div/form/div/div[6]/mat-slide-toggle')    
    __btn_requiere_visacion = (By.ID, "chkEnabledVisacion-input")
    __btn_rol_esta_activo_2 = (By.ID, "chkEnabledRol-input")
    __fondo = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section')     
    __btn_continuar_ingreso_nuevo_rol = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[3]/button')

    # Elementos para agregar productos al rol
    __btn_extender_seguros = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[2]/step-products-roles/div/div/div[2]/button')
    __btn_extender_convenios = (By.XPATH, '/html/body/app-root/app-page/div/div/main/app-templates/div/tpl-insurance-executive/div/section/div/div/tpl-admin-roles/div/div/div/div/div[2]/step-products-roles/div/div/div[3]/button')
    selector_productos = "body > app-root > app-page > div > div > main > app-templates > div > tpl-insurance-executive > div > section > div > div > tpl-admin-roles > div > div > div > div > div.steps.text-center.full-width > step-products-roles > div > div"    
    __tbx_comision = (By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/modal/div/div/div/div[1]/div/form/div/div[1]/at-input/mat-form-field/div/div[1]/div[1]/textarea')
    __bnt_confirmar_comision = (By.XPATH, "//button[contains(text(),'Confirmar')]")
    __btn_continuar_ingreso_nuevo_rol_productos = (By.XPATH, "//body/app-root[1]/app-page[1]/div[1]/div[1]/main[1]/app-templates[1]/div[1]/tpl-insurance-executive[1]/div[1]/section[1]/div[1]/div[1]/tpl-admin-roles[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]")    
    __btn_confirmar_nuevo_rol = (By.XPATH, "//button[contains(text(),'Confirmar Rol')]")
    
    #Elementos para modificación de roles 
    __txt_buscar_rol_rut = (By.XPATH, '/html[1]/body[1]/app-root[1]/app-page[1]/div[1]/div[1]/main[1]/app-templates[1]/div[1]/tpl-insurance-executive[1]/div[1]/section[1]/div[1]/div[1]/tpl-admin-roles[1]/div[1]/grid-admin-rol[1]/div[1]/div[1]/div[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]')
    __btn_modificar_rol = (By.XPATH, '/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]') 
    __btn_continuar_modificar1 = (By.XPATH, '/html[1]/body[1]/app-root[1]/app-page[1]/div[1]/div[1]/main[1]/app-templates[1]/div[1]/tpl-insurance-executive[1]/div[1]/section[1]/div[1]/div[1]/tpl-admin-roles[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]')    
    __btn_tres_puntitos = (By.XPATH, "//*[@id='icon-actions']")

    # Elementos desactivación roles
    __cbx_desactivar_activar = (By.XPATH, "//body[1]/app-root[1]/app-page[1]/div[1]/div[1]/main[1]/app-templates[1]/div[1]/tpl-insurance-executive[1]/div[1]/section[1]/div[1]/div[1]/tpl-admin-roles[1]/div[1]/grid-admin-rol[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/mat-slide-toggle[1]/label[1]/div[1]/input[1]")
    __btn_desactivar_activar_click = (By.XPATH, "//tbody/tr[1]/td[5]/mat-slide-toggle[1]/label[1]/div[1]/div[1]/div[1]")
    __btn_ver_todos = (By.XPATH, "//body/app-root[1]/app-page[1]/div[1]/div[1]/main[1]/app-templates[1]/div[1]/tpl-insurance-executive[1]/div[1]/section[1]/div[1]/div[1]/tpl-admin-roles[1]/div[1]/grid-admin-rol[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/mat-slide-toggle[1]/label[1]/div[1]/div[1]/div[1]")

    # POP UPs
    __btn_rut_con_rol = (By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/modal/div/div/div/div[2]/button[1]")
 
    

    def __init__(self, driver: WebDriver, registro_proceso):
        self.driver = driver
        self.registro_proceso = registro_proceso
          
    def login(self, usuario: str, contraseña: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_email)).send_keys(usuario)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_continuar_login)).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__tbx_password)).send_keys(contraseña)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_ingresar_login)).click()
        time.sleep(5)

    def crear_rol(self, file_path):
        df = pd.read_excel(file_path, sheet_name='Creacion de Roles')
        
        for index, row in df.iterrows():
            try:
                self.driver.get(url_qa_mantenedor)
                
                
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_crear_rol)).click()
                time.sleep(2)                              
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__tbx_nombre_rol)).send_keys(row['Nombre de ROL (Max. 20 Caracteres)'])
                print(f"Creando nuevo rol: {row['Nombre de ROL (Max. 20 Caracteres)']}")
                if row['Es Corredor'].upper() == 'SI':
                    boton_es_corredor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_es_corredor))
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_es_corredor)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(boton_es_corredor)).click()
                    time.sleep(1)
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__tbx_rut_corredor)).send_keys(row['RUT'])
                    time.sleep(2)
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__fondo)).click()
                else:
                    print("El boton es corredor es NO")

                try:                
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_rut_con_rol)).click()
                    time.sleep(2)
                except TimeoutException:
                    print("sigo con la ejecución")

                boton_rol_esta_activo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_rol_esta_activo_2))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_rol_esta_activo)
                time.sleep(2)
                if row['Rol Activo'].upper() == 'NO':                    
                    self.driver.execute_script("""
                    var radio = arguments[0];
                    radio.checked = false;  // Marca el radio button
                    radio.dispatchEvent(new Event('change', { bubbles: true }));  // Dispara el evento 'change'
                    radio.dispatchEvent(new Event('click', { bubbles: true }));  // Dispara el evento 'click'
                """, boton_rol_esta_activo)
                else:
                    print("el boton esta activo es SI")

                boton_requiere_visacion = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_requiere_visacion))
                #self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_requiere_visacion)
                time.sleep(1)
                if row['Requiere Visacion'].upper() == 'SI':
                    self.driver.execute_script("arguments[0].click();",boton_requiere_visacion)
                    time.sleep(4)
                else:
                    print("El boton requiere visación es NO")         
                
                boton_continuar_ingreso_nuevo_rol = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_continuar_ingreso_nuevo_rol))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_continuar_ingreso_nuevo_rol)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(boton_continuar_ingreso_nuevo_rol)).click()
                time.sleep(5)
                columnas_pyme = [col for col in df.columns if col.lower().startswith("pyme")]
                columnas_seguros = [col for col in df.columns if col.lower().startswith("seguro")]
                columnas_convenios = [col for col in df.columns if col.lower().startswith("convenio")]
                columnas_a_procesar = columnas_pyme + columnas_seguros + columnas_convenios    
                print(columnas_a_procesar)            
                producto_no_encontrado = self.test_roles(row,columnas_a_procesar)                
                if producto_no_encontrado == True:
                    print(f"Error en la creación del rol: {row['Nombre de ROL (Max. 20 Caracteres)']}")
                    estado_ejecucion = "No Cargado"
                    self.registro_proceso.escribir_resultado(
                            tipo_operacion="Creacion",
                            nombre_rol=row['Nombre de ROL (Max. 20 Caracteres)'],
                            rut=row['RUT'],
                            estado_ejecucion=estado_ejecucion,
                            error = "Alguno de los productos no fue encontrado"
                    )
                    continue
                
                boton_continuar_ingreso_nuevo_rol_productos = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_continuar_ingreso_nuevo_rol_productos))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_continuar_ingreso_nuevo_rol_productos)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(boton_continuar_ingreso_nuevo_rol_productos)).click()
                time.sleep(1)
                
                boton_confirmar_nuevo_rol = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_confirmar_nuevo_rol))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_confirmar_nuevo_rol)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(boton_confirmar_nuevo_rol)).click()
                #self.driver.get(url_qa_mantenedor)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_crear_rol))
                time.sleep(1)
                print(f"Rol {row['Nombre de ROL (Max. 20 Caracteres)']} creado con exito")
                estado_ejecucion = "Cargado"
            except Exception as e:
                print(f"Error en la creación del rol: {row['Nombre de ROL (Max. 20 Caracteres)']} {e}")
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado(
                        tipo_operacion="Creacion",
                        nombre_rol=row['Nombre de ROL (Max. 20 Caracteres)'],
                        rut=row['RUT'],
                        estado_ejecucion=estado_ejecucion,
                        error = "Error en la Creacion del Rol"
                )
                self.driver.get(url_qa_mantenedor)
                continue
            self.registro_proceso.escribir_resultado(
                        tipo_operacion="Creacion",
                        nombre_rol=row['Nombre de ROL (Max. 20 Caracteres)'],
                        rut=row['RUT'],
                        estado_ejecucion=estado_ejecucion,
                        error = ""
                )
            self.registro_proceso.escribir_ejecutivos(
                correo=row['Correo Solicitante'],
                rut=row['RUT'],
                nombre_rol=row['Nombre de ROL (Max. 20 Caracteres)'],
                tipo_carga="Alta"
            )

    def test_roles(self, row, columna_seguros):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_extender_seguros)).click()
            time.sleep(1)
            extender_convenio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_extender_convenios))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", extender_convenio)
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_extender_convenios)).click()
            
            for columna in columna_seguros:
                numero_seguro = str(row[columna]).strip()
                producto_encontrado = False
                
                contenedor = self.driver.find_element(By.CSS_SELECTOR, self.selector_productos)
                WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.selector_productos)))
                elemento_productos = contenedor.find_elements(By.CLASS_NAME, "ProductsRolesItem")
                print(f"Buscando Producto: {numero_seguro}")
                
                for elemento in elemento_productos:
                
                    input_element = elemento.find_element(By.TAG_NAME, "input")
                    code_element = elemento.find_element(By.CLASS_NAME, "CodeProducts")                    
                    code_element_split= code_element.text.split(" ")[0]                    

                    if code_element_split.strip() == numero_seguro.strip():
                        producto_encontrado = True
                        print(f"Codigo de producto encontrado: {numero_seguro}")
                        
                        name_element = elemento.find_element(By.CLASS_NAME, "NameProducts")                        
                        texto_producto = name_element.text.strip()
                        aria_checked = input_element.get_attribute("aria-checked")                        
                        print(f"Producto encontrado: {texto_producto}")
                        
                        if "pyme" in columna.lower():
                            mensaje = row['Mensaje Pyme']
                        else:
                            mensaje = row['Mensaje Seguros'] 
                        
                        if "convenio" in columna.lower():
                            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
                            time.sleep(2)
                            if aria_checked == "false":
                                elemento.click()
                                print("Producto agregado con exito")
                            else:
                                print("el producto ya estaba agregado en el rol") 
                            time.sleep(1)
                            continue
                        
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
                        time.sleep(2)                        
                        if aria_checked == "false":                                        
                            elemento.click()
                            print("Producto agregado con exito")
                        else:
                            print(f"el producto {texto_producto} ya se encuentra agregado en el rol")
                        time.sleep(1)
                                            
                        btn_porcentaje = elemento.find_element(By.CSS_SELECTOR, "label.lkComision.activelk")
                        self.driver.execute_script("arguments[0].click();", btn_porcentaje)
                        time.sleep(1)
                        
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__tbx_comision)).clear()
                        time.sleep(1)
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__tbx_comision)).send_keys(mensaje)
                        time.sleep(1)
                        boton_confirmar_comision = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__bnt_confirmar_comision))
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_confirmar_comision)
                        time.sleep(2)
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__bnt_confirmar_comision)).click()
                        
                
                if not producto_encontrado:
                    print(f"Producto con número {numero_seguro} no encontrado")
                    return True
            return False
        except:
            print(f"No se pudo asignar el producto {texto_producto}")
        
    def modificar_rol (self, file_path):
        df = pd.read_excel(file_path, sheet_name= 'Modificacion de Roles')
        for index, row in df.iterrows():
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__txt_buscar_rol_rut)).send_keys(row['Nombre ROL'])
                print(f"Modificando Rol: {row['Nombre ROL']}")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__btn_tres_puntitos))
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_tres_puntitos)).click()
                time.sleep(1)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_modificar_rol)).click()
                time.sleep(1)
                boton_continuar_modificar1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__btn_continuar_modificar1))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_continuar_modificar1)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__btn_continuar_modificar1)).click()
                time.sleep(2)
                
                columnas_pyme = [col for col in df.columns if col.lower().startswith("pyme")]
                columnas_seguros = [col for col in df.columns if col.lower().startswith("seguro")]
                columnas_convenios = [col for col in df.columns if col.lower().startswith("convenio")]
                columnas_a_procesar = columnas_pyme + columnas_seguros + columnas_convenios            
                producto_no_encontrado = self.test_roles(row,columnas_a_procesar)
                if producto_no_encontrado == True:
                    print("El producto no fue encontrado en la lista de productos")
                    print(f"No se pudo modificar el rol: {row['Nombre ROL']}")
                    estado_ejecucion = "No Cargado"
                    self.registro_proceso.escribir_resultado(
                        tipo_operacion="Modificacion",
                        nombre_rol=row['Nombre ROL'],
                        rut=row['RUT'],
                        estado_ejecucion=estado_ejecucion,
                        error = "Producto no encontrado"
                )
                    continue
                    
                boton_continuar_ingreso_nuevo_rol_productos = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_continuar_ingreso_nuevo_rol_productos))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_continuar_ingreso_nuevo_rol_productos)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(boton_continuar_ingreso_nuevo_rol_productos)).click()
                time.sleep(1)
                    
                boton_confirmar_nuevo_rol = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_confirmar_nuevo_rol))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_confirmar_nuevo_rol)
                time.sleep(2)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(boton_confirmar_nuevo_rol)).click()                
                #self.driver.get(url_qa_mantenedor)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.__btn_crear_rol))
                time.sleep(1)
                print(f"Rol {row['Nombre ROL']} modificado con exito.")
                estado_ejecucion = "Cargado"
            except:
                print(f"No se pudo modificar el rol: {row['Nombre ROL']}")
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado(
                        tipo_operacion="Modificacion",
                        nombre_rol=row['Nombre ROL'],
                        rut=row['RUT'],
                        estado_ejecucion=estado_ejecucion,
                        error = "Error en la modificacion del Rol"
                )
                self.driver.get(url_qa_mantenedor)                
                continue
            self.registro_proceso.escribir_resultado(
                        tipo_operacion="Modificacion",
                        nombre_rol=row['Nombre ROL'],
                        rut=row['RUT'],
                        estado_ejecucion=estado_ejecucion,
                        error = ""
                )

    def desactivar_activar_rol(self, file_path):
        df = pd.read_excel(file_path, sheet_name='Desactivar o Activar')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.__btn_ver_todos)).click()
        for index, row in df.iterrows():
            try:
                # Espera a que el campo de búsqueda esté listo y escribe el nombre del rol
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.__txt_buscar_rol_rut)).send_keys(row['Nombre ROL'])
                print(f"Rol a Activar/Desactivar: {row['Nombre ROL']}")
                # Espera a que el checkbox esté visible
                checkbox = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(self.__cbx_desactivar_activar)
                )

                # Verifica el estado actual del checkbox
                isChecked_desactivar_activar = checkbox.is_selected()
                print(f"Estado actual del botón: {isChecked_desactivar_activar}")

                # Lógica para activar o desactivar el rol
                if row['Accion'] == 'Baja' and isChecked_desactivar_activar:
                    # Si el estado es 'activo' y queremos desactivarlo, clickea el checkbox
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.__btn_desactivar_activar_click)).click()
                    time.sleep(2)
                    print("El rol fue desactivado con exito.")
                elif row['Accion'] == 'Alta' and not isChecked_desactivar_activar:
                    # Si el estado es 'inactivo' y queremos activarlo, clickea el checkbox
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.__btn_desactivar_activar_click)).click()
                    time.sleep(2)
                    print("El rol fue activado con exito.")
                else:
                    print(f"El elemento no se pudo encontrar dentro del tiempo especificado para el rol: {row['Nombre ROL']}")
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.__txt_buscar_rol_rut)).clear()
                time.sleep(1)
                estado_ejecucion = "Cargado"
            except:
                print(f"No se pudo Activar/Desactivar el rol: {row['Nombre ROL']}")
                estado_ejecucion = "No Cargado"
                self.registro_proceso.escribir_resultado_modificacion(
                        tipo_operacion="activacion desactivacion",
                        nombre_rol=row['Nombre ROL'],
                        rut=row['RUT'],
                        estado_ejecucion=estado_ejecucion,
                        tipo_modificacion=row["Accion"],
                        error = "Error en la activacion desactivacion del Rol"
                )
            self.registro_proceso.escribir_resultado_modificacion(
                        tipo_operacion="activacion desactivacion",
                        nombre_rol=row['Nombre ROL'],
                        rut=row['RUT'],
                        estado_ejecucion=estado_ejecucion,
                        tipo_modificacion=row["Accion"],
                        error = ""
                )


        







   
    
    