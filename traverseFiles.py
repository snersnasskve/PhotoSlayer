import os

class FileWalker:
# root_directory = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019"
# extensions = (".jpg", ".jpeg")

  def walkThroughFiles(self, inPath, extensions = (".jpg", ".jpeg")):
    print('i cot:')
    print(inPath)
    for (dirpath, dirnames, filenames) in os.walk(inPath):
        for filename in filenames:
            if filename.lower().endswith(extensions):
              yield (filename, os.path.join(dirpath, filename))

# for fname in walk_through_files(root_directory, extensions):
#     print(fname)