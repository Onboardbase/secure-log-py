from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()
    
setup(
    name='secure_log',
    version='0.1.0',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Samuel Olusola',
    author_email='sola@onboardbase.com',
    description='A package for secure logging',
    packages=['secure_log'],
    install_requires=[
        # Add any dependencies required by your package here
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='secure logging package',
    project_urls={
        'Source': 'https://github.com/Onboardbase/secure-log-py',
    },
)
