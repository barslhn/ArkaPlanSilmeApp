# ArkaPlanSilmeApp 🖼️✨

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
