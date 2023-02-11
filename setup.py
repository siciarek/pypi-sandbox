from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Yet another Python fractal lib'
LONG_DESCRIPTION = 'A package that provides ready to use fractal classes. Output in SVG path descriptions.'

setup(
    name="pyfrctl",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Jacek Siciarek",
    url="https://github.com/siciarek/pypi-sandbox",
    author_email="siciarek@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='fractals',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
