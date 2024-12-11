from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def start_driver():
    chromeOptions= Options()
    arguments= ['--lang=pt-BR', '--start-maximized', '--incognito']

    for argument in arguments:
        chromeOptions.add_argument(argument)
    
    chromeOptions.add_experimental_option('prefs', {
    'download.default_directory': 'C:\\Users\\secretario',
    'download.directory_upgrade': True,
    'download.prompt_for_download': False,
    'profile.default_content_setting_values.notfications': 2,
    'profile.default_content_setting_values.automatic_downloads': 1,
    
    })

    driver= webdriver.Chrome(options=chromeOptions)   

    return driver

def wait_for_element(driver, by, value, timeout=60):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )
    
def iframe_website_ads(driver):
    #Encontrando o iframe
    iframe = driver.find_element(By.NAME, 'ad_iframe')
    #Entrando no iframe
    driver.switch_to.frame(iframe)
    #interagindo com o iframe
    driver.find_element(By.XPATH, "//div[@id= 'dismiss-button']").click()
    #sair do iframe
    driver.switch_to.default_content()
    
def main():
    driver= start_driver()
    driver.get('https://yopmail.com/')
    
    try:
        #Entrando no inbox
        wait_for_element(driver, By.CLASS_NAME, 'ycptinput').send_keys('info_clima_angra')
        driver.find_element(By.XPATH, '//div[@id= "refreshbut"]/button').click()
        
        driver.find_element(By.ID, 'newmail').click()
        
        #Entrando em um iframe
        iframe= wait_for_element(driver, By.XPATH, '//iframe[@name= "ifmail"]')
        driver.switch_to.frame(iframe)
        #dentro do iframe
        #Email receptor
        driver.find_element(By.XPATH, '//input[@id= "msgto"]').send_keys('cauansurfista@yopmail.com')
        #Assunto do email
        driver.find_element(By.XPATH, '//input[@id= "msgsubject"]').send_keys('Clima da Região de Angra dos Reis, RJ, Para os próximos 3 dias.')
        #Corpo do email
        #----------------Para Completar----------------------------
        driver.find_element(By.ID, 'msgsend').click()
        
        #Saindo do iframe
        driver.switch_to.default_content()
        
        driver.quit()
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
    finally:
        try:
            if driver:
                driver.quit()
        except Exception as e:
            print(f'Erro ao fechar o WebDriver: {e}')
        print('Programa finalizado!')
        

if __name__ == '__main__':
    main()