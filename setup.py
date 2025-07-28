from setuptools import setup, find_packages

setup(
    name="guaskd",
    version="0.1.0",
    description="Spatial and Bilateral filtering using Gaussian KDTree data \
structures",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Manideepu Reddy Enugala",
    email="enugalamanideepreddy99@gmail.com",
    url="https://github.com/enugalamanideepreddy/guaskd",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "scikit-learn",
        "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
