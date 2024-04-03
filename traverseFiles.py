import os
import hashlib

class FileWalker:
# root_directory = "C:\\Users\\sners\\Desktop\\Team Turkey Run 2019"
# extensions = (".jpg", ".jpeg")

  def walkThroughFiles(self, inPath, extensions = (".jpg", ".jpeg")):
    """
        Walk Through Files recursively

        Parameters
        ----------
        inPath : str
          The name of the top level folder to use
        extensions : tuple (default is (".jpg", ".jpeg"))
          The extensions of files we are interested in
    """
    print(inPath)
    for (dirpath, dirnames, filenames) in os.walk(inPath):
        for filename in filenames:
            if filename.lower().endswith(extensions):
              yield (filename, os.path.join(dirpath, filename))

  def compute_md5(self, filePath):
      """
        Compute MD5 hash
        Parameters
        ----------
        filePath : str
      """
      md5_hash = hashlib.md5()
      with open(filePath, "rb") as f:
          for chunk in iter(lambda: f.read(4096), b""):
              md5_hash.update(chunk)
      return md5_hash.hexdigest()