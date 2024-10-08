import pdftables_api
import tempfile
import os

# Fonction pour convertir le PDF en Excel avec pdftables_api
def convert_pdf_to_excel(pdf_path):
    api_key = 'o6xspb5x8fq4'  # Remplacez par votre clé API
    # Crée un fichier temporaire pour stocker le fichier Excel converti
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        temp_excel_path = temp_file.name
    
    # Initialiser le client API avec la clé API
    client = pdftables_api.Client(api_key)
    
    try:
        # Convertir le PDF en Excel avec un seul onglet
        client.xlsx_single(pdf_path, temp_excel_path)
        print(f"Conversion réussie, fichier sauvegardé sous : {temp_excel_path}")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        return None

    return temp_excel_path
