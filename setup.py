from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="pylinkedlist",
    version="0.0.1",
    description="A Python package to work with LinkedList.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    author="Hitesh Agarwal",
    author_email="contact@hiteshagarwal.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    py_modules=["pylinkedlist"],
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[],
)
