import hashlib



def compute_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

filePath = "C:\\Users\\sners\\Desktop\\karen found\\2009-03 - 03-09 Nott Nat Tra 01 copy.jpg"
resultHash = compute_md5(filePath)

print(resultHash)