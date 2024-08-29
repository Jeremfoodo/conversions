import pandas as pd

def process_yes_food(file_path):
    df = pd.read_excel(file_path)

    # Initialiser une liste pour stocker les données formatées
    data = {
        "Produit": [],
        "Variante": [],
        "Prix (€)": []
    }

    # Variantes disponibles pour Bœuf
    bovine_variants = ["UE", "SUP", "EXTRA", "ANGUS", "SIMMENTAL"]

    # Variantes disponibles pour Veau
    veal_variants = ["BLANC", "ROSE"]

    # Variantes disponibles pour Porc
    pork_variants = ["UE", "SUP"]

    # Variantes disponibles pour Agneau
    lamb_variants = ["UE/NZ", "SUP"]

    # Variantes disponibles pour VIANDE PIECEE
    piece_variants = ["UE/NZ", "SUP"]

    # Variantes disponibles pour Volaille
    poultry_variant = ["UNI"]

    # Traiter les produits Bœuf
    for index, row in df.iterrows():
        if 8 <= index < 59:
            product_name = row[0]
            prices = row[1:6]  # Colonnes 2 à 6 contiennent les prix pour les variantes

            for i, variant in enumerate(bovine_variants):
                price = prices[i]
                if pd.isna(price):
                    price = "N/A"
                data["Produit"].append(product_name)
                data["Variante"].append(variant)
                data["Prix (€)"].append(price)

    # Traiter les produits Veau
    for index, row in df.iterrows():
        if 8 <= index <= 29:
            product_name = row[6]  # Le nom du produit est en colonne 7
            blanc_price = row[8]  # Prix pour la variante BLANC en colonne 9
            rose_price = row[9]  # Prix pour la variante ROSE en colonne 10
            
            # Ajouter les prix pour BLANC
            data["Produit"].append(product_name)
            data["Variante"].append("BLANC")
            data["Prix (€)"].append(blanc_price if pd.notna(blanc_price) else "N/A")
            
            # Ajouter les prix pour ROSE
            data["Produit"].append(product_name)
            data["Variante"].append("ROSE")
            data["Prix (€)"].append(rose_price if pd.notna(rose_price) else "N/A")

    # Traiter les produits Porc
    for index, row in df.iterrows():
        if 32 <= index < 42:  # Ajuster les indices pour les lignes de produits Porc
            product_name = row[6]  # Le nom du produit est en colonne 7
            ue_price = row[8]  # Prix pour la variante UE en colonne 9
            sup_price = row[9]  # Prix pour la variante SUP en colonne 10
            
            # Ajouter les prix pour UE
            data["Produit"].append(product_name)
            data["Variante"].append("UE")
            data["Prix (€)"].append(ue_price if pd.notna(ue_price) else "N/A")
            
            # Ajouter les prix pour SUP
            data["Produit"].append(product_name)
            data["Variante"].append("SUP")
            data["Prix (€)"].append(sup_price if pd.notna(sup_price) else "N/A")

    # Traiter les produits Agneau
    for index, row in df.iterrows():
        if 50 <= index <= 58:  # Ajuster les indices pour les lignes de produits Agneau
            product_name = row[6]  # Le nom du produit est en colonne 7
            ue_nz_price = row[8]  # Prix pour la variante UE/NZ en colonne 9
            sup_price = row[9]  # Prix pour la variante SUP en colonne 10
            
            # Ajouter les prix pour UE/NZ
            data["Produit"].append(product_name)
            data["Variante"].append("UE/NZ")
            data["Prix (€)"].append(ue_nz_price if pd.notna(ue_nz_price) else "N/A")
            
            # Ajouter les prix pour SUP
            data["Produit"].append(product_name)
            data["Variante"].append("SUP")
            data["Prix (€)"].append(sup_price if pd.notna(sup_price) else "N/A")

    # Traiter les produits VIANDE PIECEE
    for index, row in df.iterrows():
        if 60 <= index <= 63:  # Ajuster les indices pour les lignes de produits VIANDE PIECEE
            product_name = row[7]  # Le nom du produit est en colonne 8
            ue_nz_price = row[8]  # Prix pour la variante UE/NZ en colonne 9
            sup_price = row[9]  # Prix pour la variante SUP en colonne 10
            
            # Ajouter les prix pour UE/NZ
            data["Produit"].append(product_name)
            data["Variante"].append("UE/NZ")
            data["Prix (€)"].append(ue_nz_price if pd.notna(ue_nz_price) else "N/A")
            
            # Ajouter les prix pour SUP
            data["Produit"].append(product_name)
            data["Variante"].append("SUP")
            data["Prix (€)"].append(sup_price if pd.notna(sup_price) else "N/A")

    # Traiter les produits Volaille
    for index, row in df.iterrows():
        if 60 <= index <= 62:  # Ajuster les indices pour les lignes de produits Volaille
            product_name = row[0]  # Le nom du produit est en colonne 1
            price = row[1]  # Prix pour la variante unique en colonne 2
            
            # Ajouter les prix pour la seule variante
            data["Produit"].append(product_name)
            data["Variante"].append("UNI")
            data["Prix (€)"].append(price if pd.notna(price) else "N/A")

    # Convertir les données en DataFrame
    output_df = pd.DataFrame(data)


    output_path = '/tmp/processed_yes_food.xlsx'
    output_df.to_excel(output_path, index=False)

    return output_path
