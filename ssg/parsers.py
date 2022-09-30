from typing import List
from pathlib import Path
import shutil


class Parser:
    """Base class for parsers"""
    extensions: List[str] = [] 


    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path, source, dest):
        raise NotImplementedError

    def read(self, path):

        with open(path, 'rb') as file: 
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        
        full_path = dest/path.with_suffix(ext).name
        with open(full_path, 'wb') as file:
            file.write(content)


    def copy(self, path, source, dest):

        shutil.copy2(path, dest/path.relative_to(source))

    def ResourceParser(Parser): 
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]

        def parse(self, path, source, dest):
            self.copy(path, source, dest)

        


