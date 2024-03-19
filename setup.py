from setuptools import setup

setup(
    name='secure_log_py',
    version='1.0',
    author='Samuel Olusola',
    author_email='sola@onboardbase.com',
    description='A package for secure logging',
    packages=['src/secure_log_py'],
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
