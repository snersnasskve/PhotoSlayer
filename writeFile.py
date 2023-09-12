import csv

csv_filepath = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019\\TestOutput.csv"

def write_to_csv(csv_filepath):
    with open(csv_filepath, 'w', newline='') as csvfile:
        fieldnames = ['File Name', 'File Path', 'MD5 Hash']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'File Name': 'photo.jpg', 'File Path': 'file_path', 'MD5 Hash': 'md5_hash'})

write_to_csv(csv_filepath)