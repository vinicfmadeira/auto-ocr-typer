# 🖥️ Auto OCR Typer

Um script safado em Python que automatiza a leitura de texto da tela usando OCR (Tesseract) e digita o conteúdo automaticamente com `pyautogui`.

Ideal pra:

- Bots de digitação (tipo monkeytype, 10fastfingers e afins)
- Automatizar entrada de texto a partir de imagens
- Fazer o PC trabalhar por você

---

## ⚙️ Requisitos

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Bibliotecas Python:
  - `pytesseract`
  - `pyautogui`
  - `Pillow`

---

## 🛠️ Instalação

```bash
pip install pytesseract pyautogui pillow
```

Baixe e instale o Tesseract OCR:

- [Download Tesseract para Windows](https://github.com/tesseract-ocr/tesseract/wiki)

Lembre de ajustar o caminho do executável no script:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## ▶️ Como usar

1. Ajuste as coordenadas de captura de tela no código:
   ```python
   capture_screen(x1, y1, x2, y2)
   ```
   Essas coordenadas definem a área da tela onde o texto será capturado.

2. Execute o script:
   ```bash
   python auto_ocr_typer.py
   ```

3. Em até 8 segundos, foque na área que o script vai capturar.

4. Depois, foque na área onde o texto será digitado.

5. Sente e observe a mágica acontecendo.

---

## 🧠 Funcionamento

- Captura uma região específica da tela.
- Converte a imagem capturada em texto com OCR (Tesseract).
- Digita o texto automaticamente onde estiver o foco do teclado.
- Repete esse processo em loop.

---

## ⚠️ Avisos

- Dependente da qualidade da imagem e da fonte usada na tela.
- Cuidado pra não usar em sites que proíbem automação — isso aqui é só pra fins educacionais e produtividade pessoal. 👀

---

## 📄 Licença

MIT — usa, abusa, e adapta como quiser.
