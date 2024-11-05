import pandas as pd
import json  # Import the json module

def excel_to_json(excel_file, json_file):
    # Read the specified sheet 'details' from the Excel file
    df = pd.read_excel(excel_file, sheet_name='details')

    # Select only the necessary columns
    selected_columns = df[['Naam', 'Uitvoerdatum', 'KG', 'Afvalsoort']]
    
    # Convert the 'Uitvoerdatum' to string format to avoid serialization issues
    selected_columns['Uitvoerdatum'] = selected_columns['Uitvoerdatum'].astype(str)

    # Replace NaN values in 'KG' with 0 (or any other value you prefer)
    selected_columns['KG'] = selected_columns['KG'].fillna(0)

    # Convert the selected DataFrame to a dictionary
    json_data = selected_columns.to_dict(orient='records')

    # Write the JSON data to a file using the json module
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)  # Use json.dump to write the data

    print(f"Successfully converted {excel_file} (sheet: 'details') to {json_file} with selected columns.")

# Example usage
excel_to_json('Hogeschool Zuyd - PreZero Weeg dashboard 2024-8.xlsx', 'output.json')
