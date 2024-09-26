from setuptools import setup, find_packages

setup(
    name='cryptohelper',
    version='0.3',
    packages=find_packages(),
    description='Данный хелпер облегчит вам жизнь',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='cocoin',
    author_email='soon',
    url='https://github.com/cocoin123/CryptoHelper',  # или другая ссылка
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=['requests', 'json', 'aiocryptopay']
)
