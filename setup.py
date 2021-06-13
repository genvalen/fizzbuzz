from setuptools import setup

with open('README.md', 'r') as fh:
      long_description= fh.read()


setup(name='fizzbuzzer',
      version='0.0.2',
      author='Genvalen',
      author_email='',
      description='Return the output of an integer, x, according to the rules of FizzBuzz on your command line.',
      long_description=long_description, 
      long_description_content_type='text/markdown',
      url='https://github.com/genvalen/fizzbuzz',
      project_url= {
            'Bug Tracker' : 'https://github.com/genvalen/fizzbuzz/issues' 
      },
      license='MIT',
      packages=['fizzbuzzer'],
      package_dir={'' : 'src'},
      classifiers=[
            'Intended Audience :: Education',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.8',
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Testing :: Unit'
      ],
      python_requires=">=3.7"
)
      
