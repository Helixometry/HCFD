from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="HCFD",
    version="1.0.0",
    author="Mohd Mujtaba Akhtar, Girish, Muskaan Singh",
    description="Audio Deepfake Detection in Healthcare with PHOENIX-Mamba",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Helixometry/HCFD",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
