
import pandas as pd


def split_and_save_excel(file_path):
    # Excel dosyasını yükleyin
    data = pd.read_excel(file_path)

    # 'tarih' sütununu datetime türüne çevirin ve saat bilgisini kaldırın
    data['tarih'] = pd.to_datetime(data['tarih']).dt.normalize()

    # 'uretim_yuzdesi' sütununda yüzde işaretini kaldırın ve tam sayıya yuvarlayın
    if 'uretim_yuzdesi' in data.columns:
        data['uretim_yuzdesi'] = data['uretim_yuzdesi'].replace('%', '', regex=True).astype(float).astype(int)

    # Veriyi aylara göre gruplayın ve her ay için ayrı bir Excel dosyası olarak kaydedin
    for month, group in data.groupby(data['tarih'].dt.to_period('M')):
        month_str = month.strftime('%Y%m')
        output_file = f'aylik_veri_{month_str}.xlsx'
        group.to_excel(output_file, index=False)
        print(f"{output_file} dosyası kaydedildi.")


if __name__ == "__main__":
    # Excel dosyasının yolunu buraya girin
    excel_file_path = r'C:\Users\ASUS\Desktop\Miuul Ders Videoları\ceyhan_aat_verileri_tumu.xlsx'
    split_and_save_excel(excel_file_path)
