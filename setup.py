from codecs import open
from setuptools import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='app-store-scrapper',
    version='0.0.1',
    description='App Store application scrapper',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/tdle94/app-store-scrapper',
    author='Tuyen Le',
    author_email='tuyendle92@gmail.com',
    packages=['lib'],
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'beautifulsoup4>=4.6.1',
        'requests[security]>=2.20.0',
    ],
)
