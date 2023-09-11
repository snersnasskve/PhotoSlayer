import os

root_directory = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019"
extensions = (".jpg", ".jpeg")

for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.lower().endswith(extensions):
                file_path = os.path.join(dirpath, filename)
                print(file_path)