import requests
import tempfile

def convert_pdf_to_excel(pdf_file, supplier):
    temp_excel_path = tempfile.mktemp(suffix='.xlsx')  # Créer un fichier temporaire
    
    # Convertir le fichier PDF en Excel avec l'API PDFTables
    url = f"https://pdftables.com/api?key=o6xspb5x8fq4&format=xlsx-single"
    files = {'file': pdf_file}
    response = requests.post(url, files=files, stream=True)
    
    # Sauvegarder le fichier converti
    with open(temp_excel_path, 'wb') as f:
        f.write(response.content)
    
    print(f"Conversion réussie, fichier sauvegardé sous : {temp_excel_path}")
    return temp_excel_path
