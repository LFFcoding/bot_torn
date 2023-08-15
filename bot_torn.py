from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, datetime
import json

with open("./selectors.json") as file:
    selectors = json.load(file)

#rodando = True
crimes = 0
treinos = 0

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument('--user-data-dir=c:/user')

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# func para reconhecer os status
def inter(n):
   nbr = n.split("/")
   nbr = int(nbr[0])
   return nbr

#func para ir para a página de treino e clicar no botão
def treinar():
    try:
        driver.get(selectors["gym"])
        train = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["spdbutton"]))
            )
        train.click()
#        botao = driver.find_elements(By.XPATH, "/html/body/div[5]/div/div[2]/div[4]/div/div[2]/div/ul/li[1]/div[2]/div[2]/button")
#        botao[0].click()
    except Exception as e:
        print(f"Ocorreu um erro no treino: {e}" + tmst())
    finally:
        print("Treinou" + tmst())

#func para consumir nerve
def commitCrime():
    try:
        driver.get(selectors["crimescreen"])
        slradio = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["crimeshoplift"]))
            )
        slradio.click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, selectors["docrime"]).click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, selectors["docrime"]).click()
#        botao = driver.find_elements(By.XPATH, "/html/body/div[5]/div/div[2]/div[4]/div/div[2]/div/ul/li[1]/div[2]/div[2]/button")
#        botao[0].click()
    except Exception as e:
        print(f"Ocorreu um erro no crime: {e}" + tmst())
    finally:
        print(f"Sucess on crime! " + tmst())


#func para marcar momento
def tmst():
    ct = datetime.datetime.now()
    ct = ct.strftime("%d/%m/%Y %H:%M:%S")
    return ct

#execução principal
while(True):
    try:
        driver.get(selectors["bigboxlink"])
        print(f"Início: " + tmst())
        while(True):
            energy = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["energy"]))
            )

            energy = inter(energy.text)
            nerve = inter(driver.find_element(By.CSS_SELECTOR, selectors["nerve"]).text)
            print(f"Energy: " + str(energy) + " | " + "Nerve: " + str(nerve) + " " + tmst())
            if energy > 5:
                treinar()
                treinos += 1
                print(f"Treinos: " + str(treinos))
            elif nerve > 4:
                commitCrime()
                crimes += 1
                print(f"Crimes: " + str(crimes))
            print("Pause 5 minutes.")
            time.sleep(300)
                


#               elementos = driver.find_elements(By.CLASS_NAME, "bar-value___NTdce")
#   
#               textos = []
#   
#               for elemento in elementos:
#                   textos.append(elemento.text)
#   
#               energy = inter(textos[0])
#   
#               if(energy >= 6):
#                   print(f"Cheio de energia, bora treinar! " + tmst())
#                   treinar()
#                   forcaatl = driver.find_element(By.ID, "strength-val").text
#                   treinos += 1
#               else:
#                   print("Calma que tu tá exausto! Descanso de 5 minutos " + tmst())
#                   time.sleep(300)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print(f"Aguardando 30 segundos para reiniciar... " + tmst())
        time.sleep(30)
#           print("Reiniciando. " + tmst())
#           driver.get("https://www.torn.com/index.php")

    finally:
        time.sleep(900)