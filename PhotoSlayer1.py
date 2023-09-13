import os
import hashlib
import csv

def compute_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def walk_through_files(path, extensions):
   for (dirpath, dirnames, filenames) in os.walk(path):
      for filename in filenames:
          if filename.lower().endswith(extensions):
             yield (filename, os.path.join(dirpath, filename))

def create_csv(csv_filepath):
    with open(csv_filepath, 'w', newline='') as csvfile:
        fieldnames = ['name', 'path', 'hash']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        csvfile.close()

def write_to_csv(csv_filepath, csv_data):
    with open(csv_filepath, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_data.keys())
        writer.writerow(csv_data)
    csvfile.close()

        
def analyse_files(root_directory, extensions, csvfile):
    create_csv(csvfile)
    for fname, filepath in walk_through_files(root_directory, extensions):
        csv_data = {'File Name': fname, 'File Path' : filepath, 'MD5 Hash' : compute_md5(filepath)} 
        write_to_csv(csvfile, csv_data)


if __name__ == "__main__":
    root_directory = "\\\\fatsners\\Colin\\Photos"
    extensions = (".jpg", ".jpeg")
    csv_filename = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019\\PhotosOnServer.csv"
    analyse_files(root_directory, extensions, csv_filename)
