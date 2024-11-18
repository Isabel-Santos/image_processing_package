from setuptools import setup, find_packages

setup(
    name='image_processing_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'matplotlib',
    ],
    description='Pacote para processamento de imagens incluindo filtragem, detecção de bordas e operações morfológicas.',
    author='Isabel Santos',
    author_email='',
    url='https://github.com/Isabel-Santos/image_processing_package.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)