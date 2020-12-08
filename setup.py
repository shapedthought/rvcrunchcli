import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rvcrunch",  # Replace with your own username
    version="1.0.0",
    author="Ed Howard",
    author_email="exfhoward@protonmail.com",
    description="RvTools Analysis Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shapedthought/rvcrunchcli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "rvcrunch=rvcrunch.__main__:main",
        ]
    },
    python_requires=">=3.6",
)