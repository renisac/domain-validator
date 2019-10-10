from setuptools import setup, find_packages

setup(name='domain_validator',
      version='0.0.1',
      description='Validates domains from a list',
      url='https://github.com/renisac/domain_validator',
      author='Calvin Krzywiec',
      author_email='calvin@ren-isac.net',
      packages=find_packages(),
      zip_safe=False,
      entry_points = {
              'console_scripts': ['domain-validator=domain_validator:main'],
          }
)