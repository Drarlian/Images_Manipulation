"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="GEMINI_API_KEY")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# model = genai.GenerativeModel(
#   model_name="gemini-1.5-flash",
#   generation_config=generation_config,
#   # safety_settings = Adjust safety settings
#   # See https://ai.google.dev/gemini-api/docs/safety-settings
# )

# chat_session = model.start_chat(
#   history=[
#   ]
# )
#
# response = chat_session.send_message("Que dia é hoje?")
#
# print(response.text)

number_test = int(input('Digite o número do teste que deseja fazer: '))

if number_test == 0:
    # Teste 0: (Verificando os modelos disponiveis)
    for models in genai.list_models():
        if 'generateContent' in models.supported_generation_methods:
            print(models.name)

elif number_test == 1:
    # Teste 1:
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content("Quantos dias tem no ano de 2001?")
    print(response.text)

elif number_test == 2:
    # Teste 2: (Digitando em tempo real, como o chat gpt faz ao digital linha por linha)
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content("Qual o significado da vida?", stream=True)
    for chunk in response:
        print(chunk.text)
        print('-' * 30)

elif number_test == 3:
    # Teste 3:
    # Carregar a imagem usando Pillow
    imagem = Image.open('Screenshot_40.png')
    # imagem.show()

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(["De qual banco é o boleto a seguir:", imagem], stream=True)
    response.resolve()
    print(response.text)
else:
    pass
