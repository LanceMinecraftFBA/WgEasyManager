import urllib.request as req
from types import WgEasyManagerOptions

def download_file(options: WgEasyManagerOptions, uMethod: str, path: str):
  req.urlretrieve(options.url + "/" + uMethod, path)
  return true
