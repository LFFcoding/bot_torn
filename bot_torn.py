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

crimes = 0
treinos = 0

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument('--user-data-dir=c:/user')

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#função para pausa aleatória, simulando ação humana
#def randompause():
#    x = random.randint(20, 40) * 60
#    print("Pause " + str(x / 60) + " minutes. " + tmst())
#    time.sleep(x)

#func para coletar os valores das bars
def barvalues():
    energy = int(driver.find_element(By.CSS_SELECTOR, selectors["energy"]).text.split("/")[0])
    nerve = int(driver.find_element(By.CSS_SELECTOR, selectors["nerve"]).text.split("/")[0])
    return energy, nerve

# func para reconhecer os status
def stats():
    strengh = driver.find_element(By.CSS_SELECTOR, selectors["strval"]).text
    speed = driver.find_element(By.CSS_SELECTOR, selectors["spdval"]).text
    defence = driver.find_element(By.CSS_SELECTOR, selectors["defval"]).text
    print("Stats: Força: " + strengh + " | Velocidade: " + speed + " | Defesa: " + defence + " | " + tmst())

#func para ir para a página de treino e clicar no botão
def treinar():
    try:
        driver.get(selectors["gym"])
        train = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["spdbutton"]))
            )
        time.sleep(2)
        train.click()
        time.sleep(2)
    except Exception as e:
        print(f"Ocorreu um erro no treino: {e}" + tmst())
    finally:
        print("Treinou! " + tmst())
        stats()

#func para consumir nerve
def commitCrime():
    try:
        driver.get(selectors["crimescreen"])
        slradio = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectors["crimesfc"]))
            )
        time.sleep(2)
        slradio.click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, selectors["docrime"]).click()
        time.sleep(5)
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

        time.sleep(5)

        print(f"Início: " + tmst())

        while(True):

            energy, nerve = barvalues()
            print(f"Energy: " + str(energy) + " | " + "Nerve: " + str(nerve) + " " + tmst())

            while (energy >= 5):
                treinar()
                treinos += 1
                print(f"Treinos: " + str(treinos))
                energy, nerve = barvalues()
            while (nerve >= 2):
                commitCrime()
                crimes += 1
                print(f"Crimes: " + str(crimes))
                energy, nerve = barvalues()
            print("Pause 40 minutes. " + tmst())
            time.sleep(2400)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print(f"Aguardando 30 segundos para reiniciar... " + tmst())
        time.sleep(30)

    finally:
        time.sleep(300)