import setuptools 
with open("README.md", "r",encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Falcon-Text"
AUTHOR_USER_NAME = "Anshuman-Pattnaik"
SRC_REPO = "falcontext"
AUTHOR_EMAIL = "helloanshu04@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description = "FalconText",
    long_description_contect = "text/markdown",
    url = "https://github.com/ANSHPG/Falcon-Text",
    project_urls = {
        "Bug Tracker":"https://github.com/ANSHPG/Falcon-Text/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)