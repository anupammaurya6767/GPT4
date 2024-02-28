from setuptools import setup, find_packages

setup(
    name='api_gpt4',
    version='1.0.0',
    description='The GPT-4 API is an interface for interacting with the powerful GPT-4 language model. It allows you to generate natural language text, perform question-answering tasks, and more. Whether you\'re building chatbots, content generators, or creative writing tools, GPT-4 has got you covered!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Anupam Maurya',
    author_email='anupammaurya981@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.11',
    ],
    packages=find_packages(),
    python_requires='>=3.11',  # Updated version specifier
    install_requires=[
        'selenium==4.18.1'
    ],
)
