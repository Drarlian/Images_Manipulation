import base64
from PIL import Image
from io import BytesIO


def convert_image_to_base64() -> str:
    """
    Carrega a imagem e converte ela para Base64.
    :return: Retorna a imagem convertida em base64 como uma string
    """

    # Carregar a imagem
    imagem = Image.open("Screenshot_39.png")

    # Converter a imagem para base64
    # Salvar a imagem em um buffer de bytes
    buffer = BytesIO()
    imagem.save(buffer, format="PNG")  # -> A imagem é salva no buffer como se fosse um arquivo em memória no formato informado.

    # Codificar a imagem em base64
    imagem_base64: str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Agora 'imagem_base64' contém a imagem em formato base64 como uma string
    print(imagem_base64)
    return imagem_base64


def convert_base64_to_image(base64_image: str) -> Image.Image:
    """
    Convertendo Imagem em formato Base64 para Imagem normal.
    :param base64_image: Imagem em formato Base64
    :return: Retorna a imagem no formato Pillow
    """
    if base64_image.startswith('data:image'):
        base64_image = base64_image.split(',')[1]

    bytes_image = base64.b64decode(base64_image)
    buffer = BytesIO(bytes_image)
    image = Image.open(buffer)

    return image


if __name__ == '__main__':
    img_base64 = convert_image_to_base64()
    convert_base64_to_image(img_base64)
