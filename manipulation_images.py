from PIL import Image, ImageFilter, ImageDraw, ImageFont

# Abrir uma imagem
imagem = Image.open("Screenshot_39.png")

# Redimensionar
imagem_redimensionada = imagem.resize((800, 600))

# Converter para escala de cinza
imagem_cinza = imagem.convert("L")

# Recortar a imagem
caixa = (100, 100, 400, 400)
imagem_recortada = imagem.crop(caixa)

# Rotacionar a imagem
imagem_rotacionada = imagem.rotate(45)

# Aplicar um filtro de desfoque
imagem_desfocada = imagem.filter(ImageFilter.BLUR)

# Carregar uma fonte TrueType que suporte acentos (como Arial)
fonte = ImageFont.truetype("arial.ttf", 40)  # Certifique-se de que o arquivo arial.ttf esteja acessível

# Desenhar na imagem
desenho = ImageDraw.Draw(imagem)
desenho.text((50, 50), "Olá, Mundo!", font=fonte, fill="white")

# Salvar a imagem manipulada
imagem_redimensionada.save("imagem_modificada.png")

# Exibir a imagem manipulada
# imagem_recortada.show()

# imagem_rotacionada.show()

# imagem_desfocada.show()

# imagem.show()

# imagem_redimensionada.show()
