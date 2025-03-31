import pytesseract
import pyautogui
from PIL import Image
import time

# Caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Atualize o caminho conforme necessário

# Captura a área da tela
def capture_screen(x1, y1, x2, y2):   
    # Calcule a largura e altura
    width = x2 - x1
    height = y2 - y1
    screen = pyautogui.screenshot(region=(x1, y1, width, height))  # Captura a tela
    # Salva a tela
    screen.save("screen.png")  # Salva a tela capturada  

# Função para capturar o texto da imagem usando Tesseract
def get_text_from_image():
    img = Image.open("screen.png")  # Abre a imagem capturada
    text = pytesseract.image_to_string(img)  # Converte a imagem em texto
    print(f"Texto Capturado: {text}")  # Mostra o texto capturado

    # Remover quebras de linha e outros caracteres indesejados
    text = text.replace("\n", " ").replace("\r", " ")  # Substitui quebras de linha por espaço
    return text

# Função para digitar o texto
def type_text(text):
    pyautogui.typewrite(text, interval=0.001)  # Digita o texto capturado na tela sem adicionar Enter entre as frases




# Espera 3 segundos antes de capturar a tela
time.sleep(8)
    
# Captura a tela
# Alterar resolução inicial , Paramentros sao esquerda cima x e y, direita baixo x e y
capture_screen(1051, 423, 1800, 593)  # Captura a tela
  
# Obtém o texto da imagem
text = get_text_from_image()
    
# Tempo para o usuário clicar na área de digitação
time.sleep(4)  # Espera 7 segundos para o usuário focar na área de digitação
    
# Digita o texto capturado
type_text(text)
    
# Espera um pouco antes de repetir (ajuste conforme necessário)
time.sleep(1)  # Tempo para reiniciar o processo




# Loop contínuo
while True:
    # Espera 3 segundos antes de capturar a tela
    time.sleep(5)
    
    # Captura a tela
    capture_screen(1051, 492, 1800, 593)  # Captura a tela  
    # Obtém o texto da imagem
    text = get_text_from_image()
    
    # Tempo para o usuário clicar na área de digitação
    #time.sleep(7)  # Espera 7 segundos para o usuário focar na área de digitação
    
    # Digita o texto capturado
    type_text(text)
    
    # Espera um pouco antes de repetir (ajuste conforme necessário)
    #time.sleep(1)  # Tempo para reiniciar o processo
