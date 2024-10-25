import os
import hashlib
from fileHashStore import FileHashStore

class FileWalker:
  """
      A class which knows how to walk through files in a folder
  """

  def collectForPath(self, topFolder):
    """
        Collect for Path

        Parameters
        ----------
        topFolder : str
          The folder to collect for
    """ 
    hashStore = FileHashStore()
    hashStore.createCsv()

    for fname, filepath in self.walkThroughFiles(topFolder):

      csvData = {'File Name': fname, 'File Path' : filepath, 'MD5 Hash' : self.computeMd5(filepath)} 
      hashStore.writeToCsv(csvData)

    return hashStore


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


  def computeMd5(self, filePath):
      """
        Compute MD5 hash

        Parameters
        ----------
        filePath : str
          The file path to hash
      """
      md5_hash = hashlib.md5()
      with open(filePath, "rb") as f:
          for chunk in iter(lambda: f.read(4096), b""):
              md5_hash.update(chunk)
      return md5_hash.hexdigest()