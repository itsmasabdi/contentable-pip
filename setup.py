from setuptools import setup, find_packages

setup(
    name='contentable',
    version='0.1.0',
    author='Mas Abdi',
    author_email='mas@contentable.ai',
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests',
    ],
    description='End to end testing platform for your LLM models',
)
