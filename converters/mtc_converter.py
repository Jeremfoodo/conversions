import pandas as pd

def process_mtc(file_path):
    df = pd.read_excel(file_path)

    # Initialiser une liste pour stocker les données formatées
    data = {
        "Produit": [],
        "Variante": [],
        "Prix (€)": []
    }

    # Variantes disponibles
    variants = ["UE", "AT/DE", "UK/SUP", "Irlande", "Hereford", "Angus", "Simmental", "Galice", "Halal"]

    # Traiter les produits
    for index, row in df.iterrows():
        if 7 <= index < 75:  # Ajuster les indices pour les lignes de produits (commence à la ligne 7)
            # Nettoyer et concaténer les colonnes 1, 2 et 3 pour obtenir le nom du produit selon les règles spécifiées
            col1 = str(row[0]).strip()
            col2 = str(row[1]).strip()
            col3 = str(row[2]).strip()
        
            if col1 == '' and col2 == '' and col3 == '':
                continue  # Ignore les lignes où toutes les colonnes sont vides
        
            # Construire le nom du produit
            parts = []
            if col1:
                parts.append(col1)
            if col2:
                parts.append(col2)
            if col3:
                parts.append(col3)
        
            product_name = ' '.join(parts)
        
            # Extraire les prix pour chaque variante
            for i, variant in enumerate(variants):
                price = row[3 + i]  # Les prix commencent à la colonne 4
                if pd.isna(price):
                    price = "N/A"
                data["Produit"].append(product_name)
                data["Variante"].append(variant)
                data["Prix (€)"].append(price)

    # Traiter les produits Viande Pièce
    for index, row in df.iterrows():
        if 84 <= index <= 91:  # Ajuster les indices pour les lignes de produits VIANDE PIECEE (commence à la ligne 86)
            product_name = row[0]  # Le nom du produit est en colonne 8
            blanc_price = row[2]  # Prix pour la variante Irlande en colonne 9
            rose_price = row[3]  # Prix pour la variante Galice en colonne 10
        
            # Ajouter les prix pour Irlande
            data["Produit"].append(product_name)
            data["Variante"].append("Irlande")
            data["Prix (€)"].append(irlande_price if pd.notna(irlande_price) else "N/A")
        
            # Ajouter les prix pour Galice
            data["Produit"].append(product_name)
            data["Variante"].append("Galice")
            data["Prix (€)"].append(galice_price if pd.notna(galice_price) else "N/A")



    # Traiter les produits Veau
    for index, row in df.iterrows():
        if 97 <= index <= 123:  # Ajuster les indices pour les lignes de produits VIANDE PIECEE (commence à la ligne 86)
            product_name = row[0]  # Le nom du produit est en colonne 8
            blanc_price = row[2]  # Prix pour la variante Irlande en colonne 9
            rose_price = row[3]  # Prix pour la variante Galice en colonne 10
        
            # Ajouter les prix pour Irlande
            data["Produit"].append(product_name)
            data["Variante"].append("Blanc")
            data["Prix (€)"].append(blanc_price if pd.notna(blanc_price) else "N/A")
        
            # Ajouter les prix pour Galice
            data["Produit"].append(product_name)
            data["Variante"].append("rose")
            data["Prix (€)"].append(rose_price if pd.notna(rose_price) else "N/A")


    # Traiter les produits Porcelet
    for index, row in df.iterrows():
        if 132 <= index <= 141:  # Ajuster les indices pour les lignes de produits Porcelet (commence à la ligne 134)
            col1 = str(row[0]).strip()  # Nom du produit dans la colonne 1
            col2 = str(row[1]).strip()  # Nom du produit additionnel dans la colonne 2
        
            # Construire le nom du produit
            if col2:
                product_name = f"{col1} {col2}"
            else:
                product_name = col1
        
            # Extraire le prix pour la variante unique en colonne 4
            price = row[3]  # Prix pour la variante unique en colonne 4
        
            # Ajouter le produit et le prix pour Porcelet
            data["Produit"].append(product_name)
            data["Variante"].append("UNI")  # Variante unique pour Porcelet
            data["Prix (€)"].append(price if pd.notna(price) else "N/A")



    # Traiter les produits Volaille
    for index, row in df.iterrows():
        if 85 <= index <= 103:  # Ajuster les indices pour les lignes de produits Volaille (commence à la ligne 87)
            # Vérifier si la colonne 5 (index 4) n'est pas vide
            if pd.notna(row[4]) and row[4].strip() != '':
                # Construire le nom du produit
                col5 = str(row[4]).strip()  # Nom dans la colonne 5
                col6 = str(row[5]).strip()  # Nom additionnel dans la colonne 6
                product_name = f"{col5} {col6}"
            
                # Extraire les prix pour les variantes
                neutral_price = row[6]  # Prix pour la variante Neutre en colonne 7
                halal_price = row[7]  # Prix pour la variante Halal en colonne 8
            
                # Ajouter le produit et le prix pour la variante Neutre
                data["Produit"].append(product_name)
                data["Variante"].append("Neutre")
                data["Prix (€)"].append(neutral_price if pd.notna(neutral_price) else "N/A")
            
                # Ajouter le produit et le prix pour la variante Halal
                data["Produit"].append(product_name)
                data["Variante"].append("Halal")
                data["Prix (€)"].append(halal_price if pd.notna(halal_price) else "N/A")

    # Traiter les produits Volaille
    for index, row in df.iterrows():
        if 86 <= index <= 103:  # Ajuster les indices pour les lignes de produits Volaille (commence à la ligne 87)
            # Vérifier si la colonne 5 (index 4) n'est pas vide
            if pd.notna(row[4]) and row[4].strip() != '':
                # Construire le nom du produit
                col5 = str(row[4]).strip()  # Nom dans la colonne 5
                col6 = str(row[5]).strip()  # Nom additionnel dans la colonne 6
                product_name = f"{col5} {col6}"
            
                # Extraire les prix pour les variantes
                neutral_price = row[6]  # Prix pour la variante Neutre en colonne 7
                halal_price = row[7]  # Prix pour la variante Halal en colonne 8
            
                # Ajouter le produit et le prix pour la variante Neutre
                data["Produit"].append(product_name)
                data["Variante"].append("Neutre")
                data["Prix (€)"].append(neutral_price if pd.notna(neutral_price) else "N/A")
            
                # Ajouter le produit et le prix pour la variante Halal
                data["Produit"].append(product_name)
                data["Variante"].append("Halal")
                data["Prix (€)"].append(halal_price if pd.notna(halal_price) else "N/A")


    # Traiter les produits Agneau
    for index, row in df.iterrows():
        if 115 <= index <= 131:  # Ajuster les indices pour les lignes de produits Agneau (commence à la ligne 117)
            product_name = str(row[4]).strip()  # Nom du produit dans la colonne 5

            # Extraire les prix pour les variantes
            frais_price = row[5]  # Prix pour la variante Frais en colonne 6
            sous_vide_price = row[6]  # Prix pour la variante Sous-vide en colonne 7
            mouton_price = row[7]  # Prix pour la variante Mouton en colonne 8

            # Ajouter le produit et le prix pour la variante Frais
            data["Produit"].append(product_name)
            data["Variante"].append("Frais")
            data["Prix (€)"].append(frais_price if pd.notna(frais_price) else "N/A")

            # Ajouter le produit et le prix pour la variante Sous-vide
            data["Produit"].append(product_name)
            data["Variante"].append("Sous-vide")
            data["Prix (€)"].append(sous_vide_price if pd.notna(sous_vide_price) else "N/A")

            # Ajouter le produit et le prix pour la variante Mouton
            data["Produit"].append(product_name)
            data["Variante"].append("Mouton")
            data["Prix (€)"].append(mouton_price if pd.notna(mouton_price) else "N/A")


    # Traiter les produits Porc
    for index, row in df.iterrows():
        if 135 <= index <= 142:  # Ajuster les indices pour les lignes de produits Porc (commence à la ligne 137)
            product_name = str(row[4]).strip()  # Nom du produit dans la colonne 5
  
            # Extraire les prix pour les variantes
            ue_price = row[5]  # Prix pour la variante UE en colonne 6
            at_de_price = row[6]  # Prix pour la variante AT/DE en colonne 7
            irlande_price = row[7]  # Prix pour la variante Irlande en colonne 8

            # Ajouter le produit et le prix pour la variante UE
            data["Produit"].append(product_name)
            data["Variante"].append("UE")
            data["Prix (€)"].append(ue_price if pd.notna(ue_price) else "N/A")

            # Ajouter le produit et le prix pour la variante AT/DE
            data["Produit"].append(product_name)
            data["Variante"].append("AT/DE")
            data["Prix (€)"].append(at_de_price if pd.notna(at_de_price) else "N/A")

            # Ajouter le produit et le prix pour la variante Irlande
            data["Produit"].append(product_name)
            data["Variante"].append("Irlande")
            data["Prix (€)"].append(irlande_price if pd.notna(irlande_price) else "N/A")

    # Traiter les produits Congelés de la première plage
    for index, row in df.iterrows():
        if 150 <= index <= 160:  # Ajuster les indices pour les lignes de produits Congelés (commence à la ligne 151)
            product_name_parts = [
                "congelé",  # Préfixe
                str(row[0]).strip(),  # Colonne 1
                str(row[1]).strip(),  # Colonne 2
                str(row[2]).strip()   # Colonne 3
            ]
            product_name = ' '.join(filter(None, product_name_parts))  # Concaténer les parties, en ignorant les vides
        
            price = row[3]  # Prix en colonne 4
        
            # Ajouter le produit et le prix
            data["Produit"].append(product_name)
            data["Variante"].append("CONGELÉ")  # Variantes fixées ici comme "CONGELÉ"
            data["Prix (€)"].append(price if pd.notna(price) else "N/A")

    # Traiter les produits Congelés de la seconde plage
    for index, row in df.iterrows():
        if 176 <= index <= 192:  # Ajuster les indices pour les lignes de produits Congelés (commence à la ligne 177)
            product_name_parts = [
                "congelé",  # Préfixe
                str(row[0]).strip(),  # Colonne 1
                str(row[1]).strip(),  # Colonne 2
                str(row[2]).strip()   # Colonne 3
            ]
            product_name = ' '.join(filter(None, product_name_parts))  # Concaténer les parties, en ignorant les vides
        
            price = row[3]  # Prix en colonne 4
        
            # Ajouter le produit et le prix
            data["Produit"].append(product_name)
            data["Variante"].append("CONGELÉ")  # Variantes fixées ici comme "CONGELÉ"
            data["Prix (€)"].append(price if pd.notna(price) else "N/A")


    # Traiter les produits Surgelé
    for index, row in df.iterrows():
        if 150 <= index <= 186:  # Ajuster les indices pour les lignes de produits Surgelé
            # Vérifier si la colonne 8 est un chiffre
            try:
                 if pd.notna(row[7]) and isinstance(float(row[7]), (int, float)):  # Colonne 8 en index 7
                    # Construire le nom du produit
                    product_name = "CONGEL2 " + str(row[4]).strip() + " " + str(row[5]).strip() + " " + str(row[6]).strip()
                  
                    # Ajouter les prix pour la variante unique
                    price = row[7]  # Prix en colonne 8

                    data["Produit"].append(product_name)
                    data["Variante"].append("CONGELE")
                    data["Prix (€)"].append(price if pd.notna(price) else "N/A")
            except ValueError:
                continue

    # Convertir les données en DataFrame
    output_df = pd.DataFrame(data)

    output_path = '/tmp/processed_mtc.xlsx'
    output_df.to_excel(output_path, index=False)

    return output_path
