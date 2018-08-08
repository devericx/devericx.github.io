import os
import sys

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

directories = []
for (dirpath, dirnames, filenames) in os.walk("./"):
    directories.extend(dirnames)

print(directories)

template = """
<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="images/{path}" itemprop="contentUrl" data-size="{size}">
        <img data-src="thumbnails/{path}" itemprop="thumbnail" alt="{alt}" />
    </a>
    <figcaption itemprop="caption description">{alt}</figcaption>
</figure>
""".strip()

for d in directories:
    with cd(d):
        filenames = [f for f in os.listdir("./") if os.path.isfile(os.path.join("./", f)) and f != ".DS_Store"]
        print(sorted(filenames))