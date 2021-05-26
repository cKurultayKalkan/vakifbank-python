import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kuveytturk_pos",  # Replace with your own username
    version="0.0.1",
    author="Çağdaş Kurultay Kalkan",
    author_email="kurultay@codeck.com.tr",
    description="Kuveyt Türk Payment Gateway Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cKurultayKalkan/kuveytturk-pos.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'xmltodict',
        'requests'
    ],

    python_requires='>=3.6',
)
