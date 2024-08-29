import base64
from PIL import Image
from io import BytesIO

# Carregar a imagem
imagem = Image.open("Screenshot_39.png")

# Converter a imagem para base64
# Salvar a imagem em um buffer de bytes
buffer = BytesIO()
imagem.save(buffer, format="PNG")  # -> A imagem é salva no buffer como se fosse um arquivo em memória no formato informado.

# Codificar a imagem em base64
imagem_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

# Agora 'imagem_base64' contém a imagem em formato base64 como uma string
print(imagem_base64)
