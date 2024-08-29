import requests
import os

ef convert_pdf_to_excel(pdf_path):
    url = f"https://pdftables.com/api?key=o6xspb5x8fq4}&format=xlsx-single"
    headers = {"Content-Type": "application/pdf"}
    
    with open(pdf_path, 'rb') as pdf_file:
        response = requests.post(url, headers=headers, files={'file': pdf_file})
        
    if response.status_code == 200:
        temp_excel_path = pdf_path.replace('.pdf', '_converted.xlsx')
        with open(temp_excel_path, 'wb') as f:
            f.write(response.content)
        print(f"Conversion réussie, fichier sauvegardé sous : {temp_excel_path}")
        return temp_excel_path
    else:
        print(f"Erreur de conversion: {response.status_code}, {response.text}")
        return None

