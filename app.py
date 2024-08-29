import streamlit as st
import tempfile
from utils import convert_pdf_to_excel
from converters.yes_food_converter import process_yes_food
from converters.mtc_converter import process_mtc

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
            # Confirmation avant conversion
            if st.confirm("Vous allez convertir la mercuriale pour le fournisseur {}. Attention, cela coûte de l'argent à chaque fois. Êtes-vous certain de ce fichier ?".format(supplier), options=["Annuler", "OUI"], on_confirm=lambda: run_conversion(uploaded_file, supplier)):
                st.spinner("Conversion en cours...")
                file_path = convert_pdf_to_excel(uploaded_file, supplier)
                
                # Appel à la fonction de conversion spécifique au fournisseur
                if supplier == "Yes Food":
                    process_yes_food(file_path)
                elif supplier == "MTC":
                    process_mtc(file_path)

                st.success("Conversion terminée ! Vous pouvez télécharger le fichier Excel.")
                with open(file_path, 'rb') as file:
                    st.download_button("Télécharger le fichier Excel", file, file_name="Produits_Prix_{}.xlsx".format(supplier), mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.warning("Veuillez choisir un fournisseur et uploader un fichier PDF.")

if __name__ == "__main__":
    main()
