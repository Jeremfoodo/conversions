import pdftables_api
import tempfile

def convert_pdf_to_excel(pdf_path):
    # Créez un fichier temporaire pour stocker le fichier Excel converti
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        temp_excel_path = temp_file.name

    # Initialiser le client API avec la clé API
    client = pdftables_api.Client(o6xspb5x8fq4)

    # Convertir le PDF en Excel avec un seul onglet
    client.xlsx-single(pdf_path, temp_excel_path)

    print(f"Conversion réussie, fichier sauvegardé sous : {temp_excel_path}")

    return temp_excel_path
