import pdftables_api
import os

def convert_pdf_to_excel(pdf_file, supplier):
    api_key = 'o6xspb5x8fq4'
    temp_excel_path = f'/tmp/{supplier}_converted.xlsx'
    
    client = pdftables_api.Client(api_key)
    if supplier == "yes_food":
        client.xlsx_single(pdf_file, temp_excel_path)
    elif supplier == "mtc":
        client.xlsx_single(pdf_file, temp_excel_path)
    
    return temp_excel_path
