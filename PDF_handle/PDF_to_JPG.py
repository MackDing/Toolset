import fitz  # PyMuPDF
from PIL import Image


def convert_pdf_to_jpg(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        # Increase the matrix values for higher resolution
        image_list = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        image = Image.frombytes(
            "RGB", [image_list.width, image_list.height], image_list.samples)
        image.save(f"{output_folder}/page_{page_number+1}.jpg", "JPEG")

    pdf_document.close()


if __name__ == "__main__":
    # Replace with the path to your PDF file
    pdf_path = r"D:\ExtremeVision\DeskTop\ExtremeVision算法测试.pdf"
    # Folder where you want to save the output JPG images
    output_folder = r"D:\ExtremeVision\Github\Toolset\results\PDFtoJPG\Q&A"

    convert_pdf_to_jpg(pdf_path, output_folder)
    print("PDF to JPG conversion completed.")
