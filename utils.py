import pdftables_api
import tempfile

def convert_pdf_to_excel(pdf_path):
    # Crée un fichier temporaire pour stocker le fichier Excel converti
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        temp_excel_path = temp_file.name
    
    # Initialiser le client API avec la clé API
    client = pdftables_api.Client(o6xspb5x8fq4)

    try:
        # Convertir le PDF en Excel avec un seul onglet
        client.xlsx(pdf_path, temp_excel_path)
        print(f"Conversion réussie, fichier sauvegardé sous : {temp_excel_path}")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        return None

    return temp_excel_path


