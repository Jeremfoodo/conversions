import requests

def convert_pdf_to_excel(pdf_file_path, api_key):
    """
    Convertit un fichier PDF en un fichier Excel avec un seul onglet en utilisant l'API PDFTables via requests.
    
    :param pdf_file_path: Chemin vers le fichier PDF à convertir.
    :param api_key: Clé API pour PDFTables.
    :return: Chemin vers le fichier Excel converti.
    """
    temp_excel_path = f'/tmp/converted.xlsx'
    
    # URL de l'API PDFTables avec le format xlsx-single
    url = f"https://pdftables.com/api?key={api_key}&format=xlsx-single"
    
    # Chargement du fichier PDF
    with open(pdf_file_path, 'rb') as file:
        files = {'f': file}
        
        # Effectuer la demande POST pour convertir le fichier
        response = requests.post(url, files=files)
        
        # Vérifier si la demande a réussi
        if response.status_code == 200:
            with open(temp_excel_path, 'wb') as f:
                f.write(response.content)
            print(f"Conversion réussie, fichier sauvegardé sous : {temp_excel_path}")
        else:
            print(f"Erreur lors de la conversion : {response.status_code} - {response.text}")
            temp_excel_path = None
    
    return temp_excel_path
