from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="0.0.1",
    author="Holovetskyi Oleksandr",
    author_email="givis@meta.ua",
    description="Sort files in Folders by ext.",
    url="https://github.com/Oleksandr-Givi/goit-python/tree/main/lesson_7/clean_folder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = find_namespace_packages(),
    install_requires=['markdown'],
    entry_points = {'console_scripts' : ['clean-folder=clean_folder.clean:sort_files_in_dir']},
    
)