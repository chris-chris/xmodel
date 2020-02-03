import setuptools

setuptools.setup(
    name="xmodel",
    version="0.0.1",
    license='MIT',
    author="Chris Hoyean Song",
    author_email="sjhshy@gmail.com",
    description="Model management framework for machine learning",
    long_description=open('README.md').read(),
    url="https://github.com/chris-chris/xmodel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)