from setuptools import setup, find_packages

setup(
    name='CryptoHelper',
    version='0.1',
    packages=find_packages(),
    description='Данный хелпер облегчит вам жизнь для использования AioCryptoPay',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='cocoin',
    author_email='test@exemple.com',
    url='https://github.com/soon',  # или другая ссылка
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
