import os
from tkinter import Tk, filedialog, messagebox, Toplevel, Label
from rembg import remove
from PIL import Image

def process_photos():
    
    root = Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Arka Planı Silinecek Fotoğrafları Seçin",
        filetypes=[("Resim Dosyaları", "*.jpg;*.jpeg;*.png;*.webp")]
    )
    if not file_paths:
        messagebox.showinfo("Bilgi", "Herhangi bir fotoğraf seçilmedi. İşlem iptal edildi.")
        return

    save_directory = filedialog.askdirectory(
        title="Düzenlenmiş Fotoğrafların Kaydedileceği Klasörü Seçin"
    )
    if not save_directory:
        messagebox.showinfo("Bilgi", "Kaydedilecek bir klasör seçilmedi. İşlem iptal edildi.")
        return

    output_directory = os.path.join(save_directory, "düzenlenmiş fotoğraflar")
    os.makedirs(output_directory, exist_ok=True)
    
    progress_window = Toplevel(root)
    progress_window.title("İşlem Devam Ediyor...")
    progress_label = Label(progress_window, text="Hazırlanıyor...", padx=20, pady=20)
    progress_label.pack()
    progress_window.update()

    total_photos = len(file_paths)
    
    for i, file_path in enumerate(file_paths):
        try:
            filename = os.path.basename(file_path)
            progress_label.config(text=f"{i+1}/{total_photos}: '{filename}' işleniyor...")
            progress_window.update()
            
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_silindi.png")
            input_image = Image.open(file_path)
            output_image = remove(input_image)
            output_image.save(output_path)

        except Exception as e:
            progress_label.config(text=f"Hata: '{filename}' işlenirken bir sorun oluştu.")
            progress_window.update()
            
    progress_window.destroy()
    messagebox.showinfo("Tamamlandı", f"{total_photos} fotoğraf başarıyla işlendi ve kaydedildi.")

if __name__ == "__main__":
    process_photos()