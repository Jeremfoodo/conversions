import requests
import os

def convert_pdf_to_excel(pdf_path):
    url = f"https://pdftables.com/api?key=o6xspb5x8fq4&format=xlsx-single"
    files = {'file': open(pdf_path, 'rb')}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        temp_excel_path = '/tmp/temp_converted.xlsx'
        with open(temp_excel_path, 'wb') as f:
            f.write(response.content)
        print(f"Conversion réussie, fichier sauvegardé sous : {temp_excel_path}")
        return temp_excel_path
    else:
        print(f"Erreur lors de la conversion : {response.status_code}")
        return None
