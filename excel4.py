import os
import pandas as pd
from openpyxl import load_workbook
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from multiprocessing import cpu_count

# Set the directory where your Excel files are located
directory = '/Users/raffysonata/Library/CloudStorage/OneDrive-Personal/Documents/Work/UGM/Pertamina/SPBU/Form_12082024'

# Change the current working directory to the specified directory
os.chdir(directory)

# List of file names for the Excel files in the specified directory (1.xlsx to 967.xlsx)
file_paths = [f'{i}.xlsx' for i in range(1, 963)]

# Variables and their corresponding cell references, including title cells
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
    'grading': 'D17',
    'title_sales_pertamax_turbo': 'C31',
    'sales_pertamax_turbo': 'F31',
    'title_sales_pertamax': 'C32',
    'sales_pertamax': 'F32',
    'title_sales_pertamax_green': 'C33',
    'sales_pertamax_green': 'F33',
    'title_sales_pertamina_dex': 'C34',
    'sales_pertamina_dex': 'F34',
    'title_sales_dexlite': 'C35',
    'sales_dexlite': 'F35',
    'title_sales_pertalite': 'C36',
    'sales_pertalite': 'F36',
    'title_sales_biosolar': 'C37',
    'sales_biosolar': 'F37',
    'title_sales_fuel': 'C39',
    'sales_fuel': 'F39',
    'title_pangkalan_LPG_3kg': 'C43',
    'pangkalan_LPG_3kg': 'F43',
    'title_LPG_12kg': 'C45',
    'LPG_12kg': 'F45',
    'title_LPG_5.5kg': 'C46',
    'LPG_5.5kg': 'F46',
    'title_sales_non_fuel': 'C60',
    'sales_non_fuel': 'F60',
    'title_invest_tanah': 'C70',
    'invest_tanah': 'E70',
    'title_invest_dispenser': 'C72',
    'invest_dispenser': 'E72',
    'title_invest_digitalisasi': 'C73',
    'invest_digitalisasi': 'E73',
    'title_invest_instalasi': 'C74',
    'invest_instalasi': 'E74',
    'title_invest_gen_set': 'C79',
    'invest_gen_set': 'E79',
    'title_invest_pekerjaan_sipil': 'C76',
    'invest_pekerjaan_sipil': 'E76',
    'title_invest_perizinan': 'C81',
    'invest_perizinan': 'E81',
    'title_invest_total': 'C86',
    'invest_total': 'E86',
    'title_total_non_fuel': 'C100',
    'total_non_fuel': 'E100',
    'title_gaji_pegawai_fuel': 'C110',
    'gaji_pegawai_fuel': 'F110',
    'title_gaji_pegawai_non_fuel': 'C111',
    'gaji_pegawai_non_fuel': 'F111',
    'title_thr': 'C114',
    'thr': 'F114',
    'title_reward_pasti_pas': 'C118',
    'reward_pasti_pas': 'F118',
    'title_total_biaya_pegawai': 'C126',
    'total_biaya_pegawai': 'F126',
    'title_total_biaya_perawatan': 'C149',
    'total_biaya_perawatan': 'F149',
    'title_total_biaya_operasional_kantor': 'C171',
    'total_biaya_operasional_kantor': 'F171',
    'title_total_biaya_operasional': 'C179',
    'total_biaya_operasional': 'F179',
    'title_pph_21': 'C183',
    'pph_21': 'F183',
    'title_pajak_reklame': 'C184',
    'pajak_reklame': 'F184',
    'title_pbb': 'C185',
    'pbb': 'F185',
    'title_total_biaya_pajak': 'C204',
    'total_biaya_pajak': 'F204',
    'title_losses_pertamax_turbo': 'I207',
    'losses_pertamax_turbo': 'M207',
    'title_losses_pertamax': 'I208',
    'losses_pertamax': 'M208',
    'title_losses_pertamax_green': 'I209',
    'losses_pertamax_green': 'M209',
    'title_losses_pertamina_dex': 'I210',
    'losses_pertamina_dex': 'M210',
    'title_losses_dexlite': 'I211',
    'losses_dexlite': 'M211',
    'title_losses_pertalite': 'I212',
    'losses_pertalite': 'M212',
    'title_losses_biosolar': 'I213',
    'losses_biosolar': 'M213',
    'title_total_losses': 'I215',
    'total_losses': 'F215',
    'title_total_biaya_lain': 'C229',
    'total_biaya_lain': 'F229',
    'title_nominal_utang_1': 'C238',
    'nominal_utang_1': 'E238',
    'title_bunga_bank_1': 'C239',
    'bunga_bank_1': 'E239',
    'title_periode_utang_1': 'C240',
    'periode_utang_1': 'E240',
    'title_nominal_utang_2': 'C241',
    'nominal_utang_2': 'E241',
    'title_bunga_bank_2': 'C242',
    'bunga_bank_2': 'E242',
    'title_periode_utang_2': 'C243',
    'periode_utang_2': 'E243',
    'title_total_pinjaman': 'C245',
    'total_pinjaman': 'E245',
    'title_penebusan_pertamax_turbo': 'C255',
    'penebusan_pertamax_turbo': 'E255',
    'title_penebusan_pertamax': 'C256',
    'penebusan_pertamax': 'E256',
    'title_penebusan_green': 'C257',
    'penebusan_green': 'E257',
    'title_penebusan_pertamina_dex': 'C258',
    'penebusan_pertamina_dex': 'E258',
    'title_penebusan_dexlite': 'C259',
    'penebusan_dexlite': 'E259',
    'title_penebusan_pertalite': 'C260',
    'penebusan_pertalite': 'E260',
    'title_penebusan_biosolar': 'C261',
    'penebusan_biosolar': 'E261',
    'title_total_penebusan': 'C263',
    'total_penebusan': 'E263',
    'title_reference': 'C261',
    'reference': 'I261'
}

# Function to process a single file
def process_file(file_path):
    extracted_data = [os.path.basename(file_path).split('.')[0]]
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

def process_files_in_parallel(file_paths):
    data = []
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        futures = {executor.submit(process_file, file_path): file_path for file_path in file_paths}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Files"):
            data.append(future.result())
    return data

if __name__ == "__main__":
    # Process files in parallel
    data = process_files_in_parallel(file_paths)

    # Create a DataFrame with the combined data
    columns = ['No.'] + list(variables.keys())
    combined_df = pd.DataFrame(data, columns=columns)

    # Save the combined data to a new Excel file in the same directory
    combined_df.to_excel('combined_output_v4.xlsx', index=False)

    print("Data combined successfully into 'combined_output_v4.xlsx'")
