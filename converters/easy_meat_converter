import pandas as pd

def process_easymeat(file_path):
    df = pd.read_excel(file_path)

    # Initialiser une liste pour stocker les données formatées
    data = {
        "Produit": [],
        "Variante": [],
        "Prix (€)": []
    }

    # Traiter les produits Boeuf
    for index, row in df.iterrows():
        if 14 <= index < 63:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"Boeuf {str(row[0]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            ue_price = row[1]  # Prix pour la variante UE en colonne 2
            ue_sup_price = row[2]  # Prix pour la variante UE SUP en colonne 3
            
            # Ajouter les prix pour UE
            data["Produit"].append(product_name)
            data["Variante"].append("UE")
            data["Prix (€)"].append(ue_price if pd.notna(ue_price) else "N/A")
            
            # Ajouter les prix pour UE SUP
            data["Produit"].append(product_name)
            data["Variante"].append("UE SUP")
            data["Prix (€)"].append(ue_sup_price if pd.notna(ue_sup_price) else "N/A")


     # Traiter les produits Canard
    for index, row in df.iterrows():
        if 73 <= index < 83:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"Canard {str(row[0]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            regular_price = row[1]  # Prix pour la variante UE en colonne 2
            
            
            # Ajouter les prix pour regular
            data["Produit"].append(product_name)
            data["Variante"].append("Regular")
            data["Prix (€)"].append(regular_price if pd.notna(ue_price) else "N/A")

    
    # Traiter les produits DINDE
    for index, row in df.iterrows():
        if 84 <= index < 88:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"Dinde {str(row[0]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            regular2_price = row[1]  # Prix pour la variante UE en colonne 2
            
            
            # Ajouter les prix pour regular
            data["Produit"].append(product_name)
            data["Variante"].append("Regular")
            data["Prix (€)"].append(regular2_price if pd.notna(ue_price) else "N/A")

     # Traiter les produits POULET
    for index, row in df.iterrows():
        if 90 <= index < 97:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"Poulet {str(row[0]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            regular3_price = row[1]  # Prix pour la variante UE en colonne 2
            
            
            # Ajouter les prix pour regular
            data["Produit"].append(product_name)
            data["Variante"].append("Regular")
            data["Prix (€)"].append(regular3_price if pd.notna(ue_price) else "N/A")

    # Traiter les produits muscles et abats
    for index, row in df.iterrows():
        if 4 <= index < 24:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"muscles et abats {str(row[3]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            ue_price1 = row[5]  # Prix pour la variante UE en colonne 2
            ue_sup1_price = row[6]  # Prix pour la variante UE SUP en colonne 3
            
            # Ajouter les prix pour UE
            data["Produit"].append(product_name)
            data["Variante"].append("UE")
            data["Prix (€)"].append(ue_price1 if pd.notna(ue_price) else "N/A")
            
            # Ajouter les prix pour UE SUP
            data["Produit"].append(product_name)
            data["Variante"].append("UE SUP")
            data["Prix (€)"].append(ue_sup1_price if pd.notna(ue_sup_price) else "N/A")

    # Traiter les produits Boeuf Francais
    for index, row in df.iterrows():
        if 28 <= index < 42:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"boeuf {str(row[3]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            FR_price = row[6]  # Prix pour la variante UE en colonne 2
            
            # Ajouter les prix pour FRE
            data["Produit"].append(product_name)
            data["Variante"].append("Francais")
            data["Prix (€)"].append(FR_price if pd.notna(ue_price) else "N/A")
            
    
    # Traiter les produits AGNEAU
    for index, row in df.iterrows():
        if 47 <= index < 63:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"Agneau {str(row[3]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            nz_price = row[4]  
            ue3_price = row[5]
            uesup_price = row[6]
            
            # Ajouter les prix pour NZ
            data["Produit"].append(product_name)
            data["Variante"].append("NZ/AUS")
            data["Prix (€)"].append(nz_price if pd.notna(ue_price) else "N/A")
            
            # Ajouter les prix pour UE 
            data["Produit"].append(product_name)
            data["Variante"].append("UE")
            data["Prix (€)"].append(ue3_price if pd.notna(ue_sup_price) else "N/A")

             # Ajouter les prix pour UE 
            data["Produit"].append(product_name)
            data["Variante"].append("UE SUP")
            data["Prix (€)"].append(uesup_price if pd.notna(ue_sup_price) else "N/A")
            

      # Traiter les produits VEAU
    for index, row in df.iterrows():
        if 69 <= index < 97:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"Veau {str(row[5]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            extra_price = row[6]  
            blanc_price = row[7]
            rose_price = row[8]
            
            # Ajouter les prix pour extra
            data["Produit"].append(product_name)
            data["Variante"].append("Extra")
            data["Prix (€)"].append(extra_price if pd.notna(ue_price) else "N/A")
            
            # Ajouter les prix pour UE 
            data["Produit"].append(product_name)
            data["Variante"].append("blanc")
            data["Prix (€)"].append(blanc_price if pd.notna(ue_sup_price) else "N/A")

             # Ajouter les prix pour UE 
            data["Produit"].append(product_name)
            data["Variante"].append("Rose")
            data["Prix (€)"].append(rose_price if pd.notna(ue_sup_price) else "N/A")


    # Traiter les produits Viande de Prestige
    for index, row in df.iterrows():
        if 100 <= index <= 125:  # Ajuster les indices pour les lignes de produits Viande de Prestige
            product_name = f"Prestige {str(row[0]).strip()}"  # Nom du produit avec le préfixe "Prestige"
            angus_price = row[1]  # Prix pour la variante Angus en colonne 2
            simmental_price = row[2]  # Prix pour la variante Simmental en colonne 3
            hereford_price = row[3]  # Prix pour la variante Hereford en colonne 4
            bio_price = row[5]  # Prix pour la variante Bio en colonne 6
            baltic_price = row[6]  # Prix pour la variante Baltic en colonne 7
            galice_price = row[8]  # Prix pour la variante Galice en colonne 9
            
            # Ajouter les prix pour Angus
            data["Produit"].append(product_name)
            data["Variante"].append("Angus")
            data["Prix (€)"].append(angus_price if pd.notna(angus_price) else "N/A")

            # Ajouter les prix pour Simmental
            data["Produit"].append(product_name)
            data["Variante"].append("Simmental")
            data["Prix (€)"].append(simmental_price if pd.notna(simmental_price) else "N/A")

            # Ajouter les prix pour Hereford
            data["Produit"].append(product_name)
            data["Variante"].append("Hereford")
            data["Prix (€)"].append(hereford_price if pd.notna(hereford_price) else "N/A")

            # Ajouter les prix pour Bio
            data["Produit"].append(product_name)
            data["Variante"].append("Bio")
            data["Prix (€)"].append(bio_price if pd.notna(bio_price) else "N/A")

            # Ajouter les prix pour Baltic
            data["Produit"].append(product_name)
            data["Variante"].append("Baltic")
            data["Prix (€)"].append(baltic_price if pd.notna(baltic_price) else "N/A")

            # Ajouter les prix pour Galice
            data["Produit"].append(product_name)
            data["Variante"].append("Galice")
            data["Prix (€)"].append(galice_price if pd.notna(galice_price) else "N/A")

    
    # Traiter les produits Viande piecee
    for index, row in df.iterrows():
        if 136 <= index < 154:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"viande piecee {str(row[0]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            piece_price = row[4]  # Prix pour la variante UE en colonne 2
            
            # Ajouter les prix pour FRE
            data["Produit"].append(product_name)
            data["Variante"].append("regular")
            data["Prix (€)"].append(piece_price if pd.notna(ue_price) else "N/A")


     # Traiter les produits Viande congelee
    for index, row in df.iterrows():
        if 132 <= index < 154:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"viande congelee {str(row[5]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            congel_price = row[9]  # Prix pour la variante UE en colonne 2
            
            # Ajouter les prix pour FRE
            data["Produit"].append(product_name)
            data["Variante"].append("congele")
            data["Prix (€)"].append(congel_price if pd.notna(ue_price) else "N/A")

    # Traiter les produits PORC
    for index, row in df.iterrows():
        if 69 <= index < 97:  # Ajuster les indices pour les lignes de produits Boeuf
            product_name = f"Porc {str(row[2]).strip()}"  # Nom du produit avec le préfixe "Boeuf"
            reg1_price = row[4]  # Prix pour la variante UE en colonne 2
            
            # Ajouter les prix pour FRE
            data["Produit"].append(product_name)
            data["Variante"].append("regular")
            data["Prix (€)"].append(reg1_price if pd.notna(ue_price) else "N/A")

    
    for index, row in df.iterrows():
        if 158 <= index <= 178:  # Ajuster les indices pour les lignes de produits Viande du Monde (commence à la ligne 160)
         # Construire le nom du produit
            product_name = "Monde " + str(row[0]).strip()  # Concaténer "Monde" et le contenu de la colonne 1
        
             # Extraire les prix pour chaque variante
            usa_black_angus_price = row[3]  # Prix pour la variante USA/Black Angus en colonne 4
            australie_price = row[4]  # Prix pour la variante Australie en colonne 5
            argentine_price = row[5]  # Prix pour la variante Argentine en colonne 6
            uruguay_price = row[6]  # Prix pour la variante Uruguay en colonne 7
            japon_wagyu_price = row[7]  # Prix pour la variante Japon Wagyu en colonne 8
            ecosse_igp_price = row[8]  # Prix pour la variante Ecosse IGP en colonne 9
            espagne_rubia_price = row[9]  # Prix pour la variante Espagne Rubia en colonne 10
        
             # Ajouter les prix pour chaque variante
            data["Produit"].append(product_name)
            data["Variante"].append("USA/Black Angus")
            data["Prix (€)"].append(usa_black_angus_price if pd.notna(usa_black_angus_price) else "N/A")

            data["Produit"].append(product_name)
            data["Variante"].append("Australie")
            data["Prix (€)"].append(australie_price if pd.notna(australie_price) else "N/A")

            data["Produit"].append(product_name)
            data["Variante"].append("Argentine")
            data["Prix (€)"].append(argentine_price if pd.notna(argentine_price) else "N/A")

            data["Produit"].append(product_name)
            data["Variante"].append("Uruguay")
            data["Prix (€)"].append(uruguay_price if pd.notna(uruguay_price) else "N/A")

            data["Produit"].append(product_name)
            data["Variante"].append("Japon Wagyu")
            data["Prix (€)"].append(japon_wagyu_price if pd.notna(japon_wagyu_price) else "N/A")

            data["Produit"].append(product_name)
            data["Variante"].append("Ecosse IGP")
            data["Prix (€)"].append(ecosse_igp_price if pd.notna(ecosse_igp_price) else "N/A")

            data["Produit"].append(product_name)
            data["Variante"].append("Espagne Rubia")
            data["Prix (€)"].append(espagne_rubia_price if pd.notna(espagne_rubia_price) else "N/A")

    # Convertir les données en DataFrame
    output_df = pd.DataFrame(data)

    output_path = '/tmp/processed_easymeat.xlsx'
    output_df.to_excel(output_path, index=False)

    return output_path
