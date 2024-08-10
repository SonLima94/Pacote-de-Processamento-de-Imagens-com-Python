from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author='Rayrison_Lima',
    author="Son_Lima@hotmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_types="text_mackdown",
    url="https://github.com/SonLima94/Pacote-de-Processamento-de-Imagens-com-Python",
    packages=find_packages(),
    install_requirement=requirements,
    python_requires='>=3.5',
)
