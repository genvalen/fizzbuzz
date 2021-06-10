from setuptools import setup

with open('README.md', 'r') as fh:
      long_description= fh.read()


setup(name='fizzbuzzer',
      version='0.0.1',
      description='Return the output of an integer, x, according to the rules of FizzBuzz on your command line.',
      long_description=long_description, 
      long_description_content_type='text/markdown',
      url='https://github.com/genvalen/fizzbuzz',
      author='Genvalen',
      author_email='',
      license='MIT',
      packages=['fizzbuzzer'],
      package_dir={'' : 'src'},
      zip_safe=False,
      classifiers=[
            'Intended Audience :: Education',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.8',
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Testing :: Unit'
      ]
)
      
