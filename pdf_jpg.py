import os
from pdf2image import convert_from_path 
from PIL import Image
from tkinter import messagebox, Tk
from tkinter.messagebox import Message
from _tkinter import TclError

project_dir = os.path.dirname(os.path.abspath(__file__))
poppler_path = os.path.join(project_dir, 'software', 'poppler-24.02.0', 'Library', 'bin')
pdf_folder = os.path.join(project_dir, 'pdf')
save_folder = os.path.join(project_dir, 'output', 'JPG')


os.makedirs(save_folder, exist_ok=True)

name_count = {}

def convert_pdf_to_images(pdf_file, pdf_path):
    try:
        pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
        for idx, page in enumerate(pages, start=1):
            base_name = f"{os.path.splitext(pdf_file)[0]}.jpg"
            new_name = f"AA{base_name[2:]}"
            
            if new_name in name_count:
                name_count[new_name] += 1
                new_name = f"{new_name[0:2]}{chr(65 + name_count[new_name] - 1)}{new_name[2:]}"
            else:
                name_count[new_name] = 1

            # Salva a imagem
            img_path = os.path.join(save_folder, new_name)
            page.save(img_path, "JPEG", quality=100)
    except Exception as e:
        print(f"Erro ao converter {pdf_file}: {e}")


def show_completion_message():
    root = Tk()
    root.withdraw()
    try:
        root.after(3000, root.destroy)
        Message(title="Concluído!", message="Conversão concluída!!!", master=root).show()
    except TclError:
        pass
    root.mainloop()


for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        convert_pdf_to_images(pdf_file, pdf_path)

show_completion_message()