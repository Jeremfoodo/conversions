import streamlit as st
import tempfile
import os
from utils import convert_pdf_to_excel

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
            # Sauvegarde temporaire du fichier PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                temp_pdf_path = temp_pdf.name
                temp_pdf.write(uploaded_file.read())
                temp_pdf.close()
            
            # Conversion du PDF en Excel
            temp_excel_path = convert_pdf_to_excel(temp_pdf_path)
            
            if temp_excel_path:
                # Téléchargement du fichier Excel
                with open(temp_excel_path, "rb") as f:
                    st.download_button(
                        label="Télécharger le fichier Excel",
                        data=f,
                        file_name=os.path.basename(temp_excel_path),
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                
                st.success("Conversion terminée ! Vous pouvez télécharger le fichier Excel.")
            else:
                st.error("Erreur lors de la conversion du fichier PDF.")
            
            # Nettoyer les fichiers temporaires
            os.remove(temp_pdf_path)
            if os.path.exists(temp_excel_path):
                os.remove(temp_excel_path)
        else:
            st.warning("Veuillez choisir un fournisseur et uploader un fichier PDF.")

if __name__ == "__main__":
    main()
