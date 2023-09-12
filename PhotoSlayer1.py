import os
import hashlib
import csv

def compute_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def traverse_and_hash(root_directory, extensions, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['File Path', 'MD5 Hash']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for dirpath, _, filenames in os.walk(root_directory):
            for filename in filenames:
                if filename.lower().endswith(extensions):
                    file_path = os.path.join(dirpath, filename)
                    md5_hash = compute_md5(file_path)
                    
                    # Write the file path and MD5 hash to the CSV file
                    writer.writerow({'File Path': file_path, 'MD5 Hash': md5_hash})

if __name__ == "__main__":
    root_directory = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019"
    extensions = (".jpg", ".jpeg")
    csv_filename = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019\\TestOutput.csv"

    traverse_and_hash(root_directory, extensions, csv_filename)
