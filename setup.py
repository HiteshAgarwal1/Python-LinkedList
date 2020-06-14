from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name = "pylinkedlist",
    version = "0.0.2",
    description = "A Python package to work with LinkedList.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/HiteshAgarwal1/Python-LinkedList",
    download_url = "https://github.com/HiteshAgarwal1/Python-LinkedList/archive/0.0.1.tar.gz",
    author = "Hitesh Agarwal",
    author_email = "contact@hiteshagarwal.com",
    license = "MIT",
    keywords = ["linked list", "list", "python linked list"],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
    ],
    py_modules = ["pylinkedlist"],
    package_dir = {'': 'src'},
    include_package_data = True,
    install_requires = [],
)
