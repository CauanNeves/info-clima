from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from run_spider import run_weather_spider
from time import sleep
import json
import os
import schedule

def start_driver():
    chromeOptions= Options()
    arguments= ['--lang=pt-BR', '--start-maximized', '--incognito', '--headless']

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

def main():
    print('Iniciando coleta de dados...')
    sleep(2)
    run_weather_spider()
    print('\n\nColeta concluída.')
    sleep(2)
    
    # Abrir o arquivo corretamente e carregar os dados JSON
    with open('weather_data.json', 'r', encoding='utf-8') as arquivo:
        data = json.load(arquivo)  # Usando json.load() para ler e parsear diretamente
    
    for i in range(3):
        print('Data: ', data[i]['date'])
        print('Condição: ', data[i]['condition'])
        print('Máximo: ', data[i]['max'])
        print('Mínimo: ', data[i]['min'])
        
    #Iniciando o driver
    email= input('insira o email no qual deseja enviar as informações climáticas:\n')
    print('\n\n Enviando os dados, aguarde.\nO programa será fechado assim que terminar.')
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
        wait_for_element(driver, By.XPATH, '//input[@id= "msgto"]').send_keys(email)
        #Assunto do email
        driver.find_element(By.XPATH, '//input[@id= "msgsubject"]').send_keys('Clima da Região de Angra dos Reis, RJ, Para os próximos 3 dias.')
        #Corpo do email       
        corpo_1 = '''
        Prezados,

    Segue abaixo a previsão do tempo para os próximos dias:
    '''
        corpo_2 = ''.join([
            f'''
            {data[i]['date']}
            Condição: {data[i]['condition']}
            Temperatura: Mínima de {data[i]['min']} e Máxima de {data[i]['max']}
            ''' for i in range(3)
        ])

        corpo_final = corpo_1 + corpo_2
        
        driver.find_element(By.XPATH, '//div[@id="msgbody"]').send_keys(corpo_final)
        #Corpo do Email finalizado
        
        driver.find_element(By.ID, 'msgsend').click()
        
        #Saindo do iframe
        driver.switch_to.default_content()
        
        driver.quit()
        
        print('Dados enviados ao usuário.')
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
    finally:
        #Excluindo os dados
        os.remove('weather_data.json')
        print('Programa finalizado!')

#Agendando programa
def start_scheduler():
    schedule.every().day.at('06:00').do(main)
    try:
        while True:
            schedule.run_pending()
            sleep(5)
            os.system('cls' if os.name== 'nt' else 'clear')
            sleep(1)
            
    except KeyboardInterrupt:
        print("Programa encerrado pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    start_scheduler()
