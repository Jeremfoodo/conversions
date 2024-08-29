import streamlit as st
from utils import convert_pdf_to_excel
from converters.yes_food_converter import process_yes_food
from converters.mtc_converter import process_mtc
import tempfile

# Fonction principale de l'application
def main():
    st.title("Conversion des Mercuriales")

    # Menu déroulant pour choisir le fournisseur
    supplier = st.selectbox("Choisissez le fournisseur", ["Select", "Yes Food", "MTC"])

    # Upload du fichier PDF
    uploaded_file = st.file_uploader(
        "Chargez la mercuriale que vous voulez convertir en PDF. Faites bien attention que son format est le même que celui de la dernière fois, en cas de changement, alertez votre category manager.",
        type=["pdf"]
    )

    # Bouton de conversion
    if st.button("Convertir"):
        if uploaded_file and supplier != "Select":
            # Afficher un message de confirmation
            confirm = st.selectbox(
                "Vous allez convertir la mercuriale pour le fournisseur. Attention, cela coûte de l'argent à chaque fois. Êtes-vous certain de ce fichier ?",
                ["Annuler", "OUI"]
            )
            
            if confirm == "OUI":
                run_conversion(uploaded_file, supplier)
        else:
            st.warning("Veuillez choisir un fournisseur et uploader un fichier PDF.")

def run_conversion(file, supplier):
    st.spinner("Conversion en cours...")

    # Créer un fichier temporaire pour le PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(file.getvalue())
        temp_pdf_path = temp_pdf.name

    # Convertir le fichier PDF en Excel
    temp_excel_path = convert_pdf_to_excel(temp_pdf_path)

    if temp_excel_path:
        # Appel à la fonction de conversion spécifique au fournisseur
        if supplier == "Yes Food":
            process_yes_food(temp_excel_path)  # Traitement spécifique pour Yes Food
        elif supplier == "MTC":
            process_mtc(temp_excel_path)  # Traitement spécifique pour MTC
        
        # Définir le nom du fichier de sortie
        output_file_name = f"Produits_Prix_{supplier.replace(' ', '_')}.xlsx"

        # Afficher le bouton de téléchargement
        with open(temp_excel_path, 'rb') as f:
            st.download_button(
                "Télécharger le fichier Excel", 
                f, 
                file_name=output_file_name, 
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        st.success("Conversion terminée ! Vous pouvez télécharger le fichier Excel.")
    else:
        st.error("Erreur lors de la conversion. Veuillez réessayer.")

if __name__ == "__main__":
    main()
