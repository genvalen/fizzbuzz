from setuptools import setup

setup(name='fizzbuzz',
      version='0.0.1',
      description='Python package that returns the output of an integer x according to the rules of FizzBuzz.',
      long_description=open('README.md').read(),
      url='https://github.com/genvalen/fizzbuzz',
      author='Genvalen',
      author_email='genvalencia@gmail.com',
      license='MIT',
      packages=[
            'fizzbuzz'
      ],
      zip_safe=False)
