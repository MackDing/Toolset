import PyPDF2

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

pdf_to_txt('./datasets/萤火虫PTE真题机经8.0.17.11 WFD.pdf', './results/萤火虫PTE真题机经8.0.17.11 WFD.txt')