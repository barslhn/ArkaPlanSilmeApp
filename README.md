# ArkaPlanSilmeApp

Bu proje, seçilen fotoğrafların arka planını otomatik olarak kaldıran bir masaüstü uygulamasıdır.  
Kullanıcı dostu arayüzü sayesinde, fotoğrafları kolayca işleyebilir ve düzenlenmiş halleri istediğiniz klasöre kaydedebilirsiniz.

## Özellikler
- Çoklu fotoğraf seçme ve arka planlarını otomatik temizleme
- İşlem sırasında ilerleme penceresi ile bilgi verme
- Düzenlenmiş fotoğrafları, seçilen bölgede otomatik olarak **`düzenlenmiş fotoğraflar`** adlı bir alt klasöre kaydetme
- Çıktıları şeffaf arka planlı `.png` formatında alma
- Hata durumlarında kullanıcıya bilgilendirme mesajları gösterme

## Kullanım
1. Uygulamayı çalıştırın (`app.py` veya derlenmiş `.exe` dosyası).
2. Arka planı silinecek fotoğrafları seçin (.jpg, .jpeg, .png, .webp).
3. Düzenlenmiş fotoğrafların kaydedileceği yeri seçin.  
   → Örneğin **Masaüstü** seçerseniz, orada otomatik olarak **`düzenlenmiş fotoğraflar`** klasörü oluşur.
4. İlerleme penceresinden işlemi takip edin.
5. İşlem tamamlandığında bilgilendirme penceresi çıkacak ve tüm fotoğraflar seçtiğiniz klasörde kaydedilmiş olacak.

## Gereksinimler
- Python 3.8+
- Pillow (PIL)

Gerekli bağımlılıkları yüklemek için:
```bash
pip install -r requirements.txt

---

# BackgroundRemovalApp

This project is a desktop application that automatically removes the background from selected photos.  
Thanks to its user-friendly interface, users can easily process photos and save the edited versions to a desired folder.

## Features
- Select multiple photos and automatically remove their backgrounds
- Display a progress window during processing
- Save edited photos automatically into a subfolder named **`düzenlenmiş fotoğraflar` / `edited_photos`**
- Export outputs in `.png` format with transparent background
- Show informative messages to the user in case of errors

## Usage
1. Run the application (`app.py` or the compiled `.exe` file).
2. Select the photos whose background you want to remove (.jpg, .jpeg, .png, .webp).
3. Choose the folder where edited photos will be saved.  
   → For example, if you choose **Desktop**, a folder named **`düzenlenmiş fotoğraflar` / `edited_photos`** will be created automatically.
4. Track the progress through the progress window.
5. Once the process is complete, an information window will appear and all photos will be saved in the folder you selected.

## Requirements
- Python 3.8+
- Pillow (PIL)

To install the required dependencies:
```bash
pip install -r requirements.txt

## 📝 Notes  

- `/tr` indicates the Turkish translation of the preceding English text.



