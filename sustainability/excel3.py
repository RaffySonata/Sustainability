import os
import pandas as pd
from openpyxl import load_workbook
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from multiprocessing import cpu_count  # Correct import

# Set the directory where your Excel files are located
directory = '/Users/raffysonata/Library/CloudStorage/OneDrive-Personal/Documents/Work/UGM/Pertamina/SPBU/Form_12082024'

# Change the current working directory to the specified directory
os.chdir(directory)

# List of file names for the Excel files in the specified directory (1.xlsx to 967.xlsx)
file_paths = [f'{i}.xlsx' for i in range(1, 963)]

# Variables and their corresponding cell references
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
    'sales_fuel': 'F35',
    'sales_lpg': 'F39',
    'title_sales_non_fuel': 'C53',
    'sales_non_fuel': 'F53',
    'title_invest_tanah': 'C63',
    'invest_tanah': 'E63',
    'title_invest_dispenser': 'C65',
    'invest_dispenser': 'E65',
    'title_invest_pekerjaan_sipil': 'C69',
    'invest_pekerjaan_sipil': 'E69',
    'title_invest_perizinan': 'C74',
    'invest_perizinan': 'E74',
    'title_invest_total': 'C79',
    'invest_total': 'E79',
    'title_bright_store': 'C82',
    'bright_store': 'E82',
    'title_lpg': 'C83',
    'lpg': 'E83',
    'title_total_non_fuel': 'C93',
    'total_non_fuel': 'E93',
    'title_gaji_pegawai': 'C103',
    'gaji_pegawai': 'F103',
    'title_thr': 'C106',
    'thr': 'F106',
    'title_reward_pasti_pas': 'C110',
    'reward_pasti_pas': 'F110',
    'title_total_biaya_pegawai': 'C118',
    'total_biaya_pegawai': 'F118',
    'title_total_biaya_perawatan': 'C141',
    'total_biaya_perawatan': 'F141',
    'title_total_biaya_operasional_kantor': 'C163',
    'total_biaya_operasional_kantor': 'F163',
    'title_total_biaya_operasional': 'C171',
    'total_biaya_operasional': 'F171',
    'title_pph_21': 'C175',
    'pph_21': 'F175',
    'title_pajak_reklame': 'C176',
    'pajak_reklame': 'F176',
    'title_pbb': 'C177',
    'pbb': 'F177',
    'title_total_biaya_pajak': 'C196',
    'total_biaya_pajak': 'F196',
    'title_losses_pertamax_turbo': 'J199',
    'losses_pertamax_turbo': 'M199',
    'title_losses_pertamax': 'J200',
    'losses_pertamax': 'M200',
    'title_losses_pertamina_dex': 'J201',
    'losses_pertamina_dex': 'M201',
    'title_losses_dexlite': 'J202',
    'losses_dexlite': 'M202',
    'title_losses_pertalite': 'J203',
    'losses_pertalite': 'M203',
    'title_losses_biosolar': 'J204',
    'losses_biosolar': 'M204',
    'title_total_losses': 'O206',
    'total_losses': 'F206',
    'title_total_biaya_lain': 'C220',
    'total_biaya_lain': 'F220',
    'title_nominal_utang_1': 'C229',
    'nominal_utang_1': 'E229',
    'title_bunga_bank_1': 'C230',
    'bunga_bank_1': 'E230',
    'title_periode_utang_1': 'C231',
    'periode_utang_1': 'E231',
    'title_nominal_utang_2': 'C232',
    'nominal_utang_2': 'E232',
    'title_bunga_bank_2': 'C233',
    'bunga_bank_2': 'E233',
    'title_periode_utang_2': 'C234',
    'periode_utang_2': 'E234',
    'title_total_pinjaman': 'C236',
    'total_pinjaman': 'E236',
    'reference': 'I251'
}

# Function to process a single file
def process_file(file_idx):
    file_path = os.path.join(directory, file_paths[file_idx])
    extracted_data = [file_idx + 1]
    try:
        wb = load_workbook(file_path, data_only=True)
        sheet = wb.active
        for var_name, cell_ref in variables.items():
            cell_value = sheet[cell_ref].value
            extracted_data.append(cell_value)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        extracted_data.extend([None] * len(variables))
    return extracted_data

if __name__ == "__main__":
    data = []
    file_indices = list(range(len(file_paths)))

    # Process files using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        futures = {executor.submit(process_file, idx): idx for idx in file_indices}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Files"):
            data.append(future.result())

    # Create a DataFrame with the combined data
    columns = ['No.'] + list(variables.keys())
    combined_df = pd.DataFrame(data, columns=columns)

    # Save the combined data to a new Excel file in the same directory
    combined_df.to_excel('combined_output_v3_fast.xlsx', index=False)

    print("Data combined successfully into 'combined_output_v3_fast.xlsx'")
