from setuptools import setup, find_packages


setup(
    name='lacinizatar',
    version='0.0.1',
    description='Converter Belarusian Cyrillic to the Latin alphabet',
    author='Pavel Tyslacki',
    author_email='pavel.tyslacki@gmail.com',
    url='https://github.com/tbicr/lacinizatar',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ],
)
