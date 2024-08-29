import streamlit as st
import tempfile
import os
from utils import convert_pdf_to_excel
from converters.yes_food_converter import process_yes_food
from converters.mtc_converter import process_mtc
from converters.easy_meat_converter import process_easymeat

# Fonction principale de l'application
def main():
    st.title("Conversion des Mercuriales")

    # Menu déroulant pour choisir le fournisseur
    supplier = st.selectbox("Choisissez le fournisseur", ["Select", "Yes Food", "MTC", "Easy Meat"])

    # Upload du fichier PDF
    uploaded_file = st.file_uploader(
        "Chargez la mercuriale que vous voulez convertir en PDF. Faites bien attention que son format est le même que celui de la dernière fois, en cas de changement, alertez votre category manager. ATTENTION, cette opération a un coût, ne la faites que si vous en avez besoin",
        type=["pdf"]
    )

    # Bouton de conversion
    if st.button("Convertir"):
        if uploaded_file and supplier != "Select":
            # Sauvegarde temporaire du fichier PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                temp_pdf_path = temp_pdf.name
                temp_pdf.write(uploaded_file.read())
                temp_pdf.close()
            
            # Conversion du PDF en Excel
            temp_excel_path = convert_pdf_to_excel(temp_pdf_path)
            
            if temp_excel_path:
                # Traitement spécifique au fournisseur
                if supplier == "Yes Food":
                    final_file_path = process_yes_food(temp_excel_path)
                elif supplier == "MTC":
                    final_file_path = process_mtc(temp_excel_path)
                elif supplier == "Easy Meat":
                    final_file_path = process_easy_meat(temp_excel_path)
                
                # Télécharger le fichier Excel final
                with open(final_file_path, "rb") as f:
                    st.download_button(
                        label="Télécharger le fichier Excel",
                        data=f,
                        file_name=os.path.basename(final_file_path),
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                
                st.success("Conversion terminée ! Vous pouvez télécharger le fichier Excel.")
            else:
                st.error("Erreur lors de la conversion du fichier PDF.")
            
            # Nettoyer les fichiers temporaires
            os.remove(temp_pdf_path)
            if os.path.exists(temp_excel_path):
                os.remove(temp_excel_path)
            if os.path.exists(final_file_path):
                os.remove(final_file_path)
        else:
            st.warning("Veuillez choisir un fournisseur et uploader un fichier PDF.")

if __name__ == "__main__":
    main()
