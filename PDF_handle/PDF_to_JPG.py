import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_to_jpg(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        image_list = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase the matrix values for higher resolution
        
        image = Image.frombytes("RGB", [image_list.width, image_list.height], image_list.samples)
        image.save(f"{output_folder}/page_{page_number+1}.jpg", "JPEG")

    pdf_document.close()

if __name__ == "__main__":
    pdf_path = "./datasets/65个思维模型地图.pdf"  # Replace with the path to your PDF file
    output_folder = "./results/PDFtoJPG"  # Folder where you want to save the output JPG images
    
    convert_pdf_to_jpg(pdf_path, output_folder)
    print("PDF to JPG conversion completed.")