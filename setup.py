from setuptools import setup, find_packages

setup(
    name='utiliseapp',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Application Django pour ,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='amah esther',
    author_email='estherkouao9@gmail.com',
    url='https://github.com/Estherkouao/packagecreation.git',
    install_requires=[
        'django>=5.2.4',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)

