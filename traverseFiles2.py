import os

root_directory = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019"
extensions = (".jpg", ".jpeg")

def walk_through_files(path, extensions):
   for (dirpath, dirnames, filenames) in os.walk(path):
      for filename in filenames:
          if filename.lower().endswith(extensions):
            yield (filename, os.path.join(dirpath, filename))

for fname in walk_through_files(root_directory, extensions):
    print(fname)