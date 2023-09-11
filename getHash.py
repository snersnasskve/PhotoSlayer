import hashlib

def compute_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

file_path = "C:\\Users\\sners\\Desktop\\FolderName\\2009-03 - 03-09 Nott Nat Tra 01 copy.jpg"
result_hash = compute_md5(file_path)

print(result_hash)