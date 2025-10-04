# HEIC to JPG Converter

A simple Python script to convert all **HEIC files** in a folder to **JPG** format and save them in a specified destination folder. Works on Windows, macOS, and Linux.

---

## **Requirements**

- Python 3.8+
- Packages:

  ```bash
  pip install pillow pillow-heif
  ```

---

## **Installation**

1. Clone or download this repository.
2. Install the required packages:

   ```bash
   pip install pillow pillow-heif
   ```

---

## **Usage**

1. Open a terminal or command prompt.
2. Run the script:

   ```bash
   python heic_to_jpg.py
   ```

3. Enter the **source folder path** (the folder containing all HEIC files).
4. Enter the **destination folder path** (where all JPG files will be saved).

Example:

```
Enter source folder path with HEIC files: Tashin\HEIC_Folder
Enter destination folder path for JPG files: Tashin\JPG_Folder
```

The script will convert all `.heic` files in the source folder to `.jpg` and save them in the destination folder.

---

## **Notes**

- The destination folder will be **created automatically** if it does not exist.
- Works for **any number of HEIC files** in the source folder.
- If you want faster conversion for large batches, the script can be modified to run **in parallel using multithreading**.
