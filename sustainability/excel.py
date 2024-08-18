import os
import pandas as pd
from openpyxl import load_workbook
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

# Set the directory where your Excel files are located
directory = '/Users/raffysonata/Library/CloudStorage/OneDrive-Personal/Documents/Work/UGM/Pertamina/SPBU/Form'

# Change the current working directory to the specified directory
os.chdir(directory)

# List of file names for the Excel files in the specified directory (1.xlsx to 561.xlsx)
file_paths = [f'{i}.xlsx' for i in range(1, 562)]

# Variables and their corresponding cell references
variables = {
    'nomor_spbu': 'D4',
    'skema_spbu': 'D5',
    'jenis_spbu': 'D6',
    'lokasi_spbu': 'D8',
    'desa': 'D9',
    'kecamatan': 'D10',
    'kab_kota': 'D11',
    'provinsi': 'D12',
    'tahun_berdiri': 'D15',
    'grading': 'D16',
    'sales_pertamax_turbo': 'F28',
    'sales_pertamax': 'F29',
    'sales_pertamina_dex': 'F30',
    'sales_dexlite': 'F31',
    'sales_pertalite': 'F32',
    'sales_biosolar': 'F33',
    'sales_fuel': 'F34',
    'sales_lpg': 'F39',
    'sales_non_fuel': 'F53',
    'invest_tanah': 'E63',
    'invest_dispenser': 'E65',
    'invest_pekerjaan_sipil': 'E67',
    'invest_perijinan': 'E72',
    'invest_total_fuel': 'E79',
    'bright_store': 'E82',
    'lpg': 'E83',
    'total_non_fuel': 'E93',
    'gaji_pegawai': 'F103',
    'thr': 'F106',
    'reward_pasti_pas': 'F110',
    'total_biaya_pegawai': 'F118',
    'total_biaya_perawatan': 'F141',
    'total_biaya_operasional_kantor': 'F163',
    'total_biaya_operasional_listrik': 'F171',
    'pph_21': 'F175',
    'pajak_reklame': 'F176',
    'pbb': 'F177',
    'total_biaya_pajak': 'F196',
    'losses_pertamax_turbo': 'F199',
    'losses_pertamax': 'F200',
    'losses_pertamina_dex': 'F201',
    'losses_dexlite': 'F202',
    'losses_pertalite': 'F203',
    'losses_biosolar': 'F204',
    'total_losses': 'F206',
    'total_biaya_lain': 'F220',
    'nominal_utang_1': 'E229',
    'bunga_bank_1': 'E230',
    'periode_utang_1': 'E231',
    'nominal_utang_2': 'E232',
    'bunga_bank_2': 'E233',
    'periode_utang_2': 'E234',
    'total_pinjaman': 'E236',
    'penebusan_pertamax_turbo': 'E246',
    'penebusan_pertamax': 'E247',
    'penebusan_pertamina_dex': 'E248',
    'penebusan_dexlite': 'E249',
    'penebusan_pertalite': 'E250',
    'penebusan_biosolar': 'E251',
    'total_penebusan': 'E253'
}

# Initialize an empty list to store data
data = []

# Function to get value from a cell using openpyxl
def get_cell_value(file_path, cell):
    try:
        wb = load_workbook(file_path, data_only=True)
        sheet = wb.active
        cell_value = sheet[cell]
        return cell_value.value
    except Exception as e:
        print(f"Error reading {file_path}, cell {cell}: {e}")
        return None

# Function to process a single file
def process_file(file_path):
    extracted_data = [os.path.basename(file_path)]
    for var_name, cell_ref in variables.items():
        extracted_data.append(get_cell_value(file_path, cell_ref))
    return extracted_data

# Use ProcessPoolExecutor to process files in parallel
with ProcessPoolExecutor() as executor:
    # Submit tasks
    futures = {executor.submit(process_file, os.path.join(directory, file_path)): file_path for file_path in file_paths}

    # Process results as they complete with a progress bar
    for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Files"):
        try:
            data.append(future.result())
        except Exception as e:
            print(f"Error processing file: {e}")

# Create a DataFrame with the combined data
columns = ['File'] + list(variables.keys())
combined_df = pd.DataFrame(data, columns=columns)

# Save the combined data to a new Excel file in the same directory
combined_df.to_excel('combined_output.xlsx', index=False)

print("Data combined successfully into 'combined_output.xlsx'")
