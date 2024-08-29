import streamlit as st
from utils import convert_pdf_to_excel
from converters.yes_food_converter import process_yes_food
from converters.mtc_converter import process_mtc

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
            st.confirm(
                f"Vous allez convertir la mercuriale pour le fournisseur {supplier}. Attention, cela coûte de l'argent à chaque fois. Êtes-vous certain de ce fichier ?",
                options=["Annuler", "OUI"],
                on_confirm=lambda: run_conversion(uploaded_file, supplier)
            )
        else:
            st.warning("Veuillez choisir un fournisseur et uploader un fichier PDF.")

def run_conversion(file, supplier):
    st.spinner("Conversion en cours...")
    
    # Appel à la fonction de conversion spécifique au fournisseur
    if supplier == "Yes Food":
        convert_pdf_to_excel(file, "yes_food")  # Convertir le PDF
        process_yes_food(file)  # Traitement spécifique pour Yes Food
    elif supplier == "MTC":
        convert_pdf_to_excel(file, "mtc")  # Convertir le PDF
        process_mtc(file)  # Traitement spécifique pour MTC

    st.success("Conversion terminée ! Vous pouvez télécharger le fichier Excel.")
    st.download_button("Télécharger le fichier Excel", file)

if __name__ == "__main__":
    main()
