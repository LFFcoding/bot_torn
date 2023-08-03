from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, datetime

rodando = True
treinos = 0
forcaatl = ""

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument("--user-data-dir=D:/ambientes_pessoal/bot_torn_archives/UserData")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# func para reconhecer os status
def inter(n):
   nbr = n.split("/")
   nbr = int(nbr[0])
   return nbr

#func para ir para a página de treino e clicar no botão
def treinar():
    try:
        driver.get("https://www.torn.com/gym.php")
        forca = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "strength-val"))
            )
        botao = driver.find_elements(By.XPATH, "/html/body/div[5]/div/div[2]/div[4]/div/div[2]/div/ul/li[1]/div[2]/div[2]/button")
        botao[0].click()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Aguardando 20 minutos para reiniciar")
        time.sleep(1200)
        driver.get("https://www.torn.com/index.php")
    finally:
        print("Treino foi top!")

#func para marcar momento
def tmst():
    ct = datetime.datetime.now()
    ct = ct.strftime("%d/%m/%Y %H:%M:%S")
    return ct

#execução principal
while(rodando == True):
    try:
        driver.get("https://www.torn.com/index.php")
        aguarde = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bar-value___NTdce"))
        )

        elementos = driver.find_elements(By.CLASS_NAME, "bar-value___NTdce")

        textos = []

        for elemento in elementos:
            textos.append(elemento.text)

        energy = inter(textos[0])

        if(energy >= 6):
            print(f"Cheio de energia, bora treinar! " + tmst())
            treinar()
            forcaatl = driver.find_element(By.ID, "strength-val").text
            treinos += 1
        else:
            print("Calma que tu tá exausto! Descanso de 5 minutos " + tmst())
            time.sleep(300)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Aguardando 20 minutos para reiniciar... " + tmst())
        time.sleep(1200)
        print("Reiniciando. " + tmst())
        driver.get("https://www.torn.com/index.php")

    finally:
        print("Sucesso! " + tmst())
        print(f"Treinos: " + str(treinos))
        print(f"Força atual: " + forcaatl)
        time.sleep(5)
        driver.get("https://www.torn.com/index.php")