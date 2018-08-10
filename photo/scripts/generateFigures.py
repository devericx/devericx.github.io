from PIL import Image
import os
import sys
import pyperclip

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

if len(directories) == 0:
    print("No directories available.")
    exit(0)

template = """
<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="images/{path}" itemprop="contentUrl" data-size="{size}">
        <img data-src="thumbnails/{path}" itemprop="thumbnail" alt="{alt}" />
    </a>
    <figcaption itemprop="caption description">{alt}</figcaption>
</figure>
""".strip()

figures = []

for d in directories:
    with cd(d):
        raw_filenames = [f for f in os.listdir("./") if os.path.isfile(os.path.join("./", f)) and f != ".DS_Store"]
        sorted_filenames = sorted(raw_filenames)
        for file in sorted_filenames:
            im = Image.open(file)
            width, height = im.size
            im.close()
            figure = template.format(path = d + "/" + file, size = str(width) + "x" + str(height), alt = file.replace("-", " ")[:-4])
            figure = "<!--### {} ###-->\n".format(file) + figure
            figures.append(figure)

all_figures = ""

for figure in figures:
    all_figures += figure + "\n\n"
all_figures = all_figures.strip()
print(all_figures)
pyperclip.copy(all_figures)
print("All figures copied to clipboard.")