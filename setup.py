import setuptools

setuptools.setup(
    name='osrs_net',
    version='0.2.0',
    author='Patrick Seute',
    author_email='patrick.seute@gmail.com',
    description='Simple OSRS API Wrapper',
    url = 'https://github.com/SuperRonJon/osrs-net',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'requests'
    ],
    package_data={'osrs_net': ['resources/items.json']}
)
