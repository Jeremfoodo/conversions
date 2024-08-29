import streamlit as st
import os
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
            st.write(f"Vous allez convertir la mercuriale pour le fournisseur **{supplier}**. Attention, cela coûte de l'argent à chaque fois. Êtes-vous certain de ce fichier ?")

            # Ajouter les boutons pour la confirmation
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Annuler"):
                    st.write("Conversion annulée.")
            with col2:
                if st.button("OUI"):
                    run_conversion(uploaded_file, supplier)
        else:
            st.warning("Veuillez choisir un fournisseur et uploader un fichier PDF.")

def run_conversion(file, supplier):
    st.spinner("Conversion en cours...")

    # Sauvegarder le fichier PDF temporairement
    pdf_path = '/tmp/uploaded_file.pdf'
    with open(pdf_path, 'wb') as f:
        f.write(file.getvalue())

    # Convertir le fichier PDF en Excel
    temp_excel_path = convert_pdf_to_excel(pdf_path)  
    
    if temp_excel_path:
        # Appel à la fonction de conversion spécifique au fournisseur
        if supplier == "Yes Food":
            process_yes_food(temp_excel_path)  # Traitement spécifique pour Yes Food
        elif supplier == "MTC":
            process_mtc(temp_excel_path)  # Traitement spécifique pour MTC
        
        # Afficher le bouton de téléchargement
        with open(temp_excel_path, 'rb') as f:
            st.download_button("Télécharger le fichier Excel", f, file_name="Produits_Prix_MTC.xlsx")
        
        st.success("Conversion terminée ! Vous pouvez télécharger le fichier Excel.")
    else:
        st.error("Erreur lors de la conversion. Veuillez réessayer.")

if __name__ == "__main__":
    main()
