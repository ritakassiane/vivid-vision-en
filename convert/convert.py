import fitz
from PIL import Image
import os

def save_pdf_as_png(folder_name, pdf_filename, resolution=(3840, 2160), dpi=96):
    # Define o caminho completo do arquivo PDF
    pdf_filepath = os.path.join(os.getcwd(), pdf_filename)

    # Define o caminho completo da pasta onde as imagens serão salvas
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Verifica se o caminho da pasta existe, caso contrário, cria a pasta
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Abre o arquivo PDF
    with fitz.open(pdf_filepath) as doc:
        for i, page in enumerate(doc):
            # Renderiza a página como imagem rasterizada
            pixmap = page.get_pixmap(alpha=False)
        
            # Cria um objeto Image do Pillow a partir da imagem rasterizada
            img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        
            # Redimensiona a imagem para a resolução desejada
            img = img.resize(resolution)
        
            # Define o nome e o formato do arquivo PNG
            png_filename = f'{i}.png'
        
            # Define o caminho completo do arquivo PNG
            png_filepath = os.path.join(folder_path, png_filename)
        
            # Salva a imagem PNG com a resolução definida e o caminho completo do arquivo
            img.save(png_filepath, dpi=(dpi, dpi))


save_pdf_as_png('../assets/images', 'vivid-vision-en.pdf')