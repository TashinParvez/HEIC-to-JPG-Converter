from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()  # Allows Pillow to open HEIC

def heic_to_jpg(source_folder, dest_folder):
    import os
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(source_folder, filename)
            image = Image.open(heic_path)
            
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(dest_folder, jpg_filename)
            image.save(jpg_path, "JPEG")
            print(f"Converted: {filename} -> {jpg_filename}")

if __name__ == "__main__":
    source = input("Enter source folder path with HEIC files: ")
    destination = input("Enter destination folder path for JPG files: ")
    heic_to_jpg(source, destination)
    print("All files converted successfully!")
