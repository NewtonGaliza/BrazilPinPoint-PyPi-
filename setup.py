import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brazilpinpoint",
    version="0.0.1",
    author="Newton Galiza",
    author_email="newtonjgaliza@gmail.com",
    description="Using a latitude and longitude a pin point is marked on Brazil map",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NewtonGaliza/BrazilPinPoint-PyPi-",
    packages=setuptools.find_packages(),
    install_requires = ['folium'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
