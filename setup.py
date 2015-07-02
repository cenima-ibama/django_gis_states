from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='django-gis-states',
      version='0.1',
      description="""Django app that provides gis models to applications that
          need to deal with State and Cities""",
      long_description=long_description,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: GIS',
          'Topic :: Utilities',
          'Framework :: Django',
          'Environment :: Web Environment',
      ],
      keywords=['gis', 'states', 'cities', 'django', 'geodjango'],
      author="Wille Marcel",
      author_email='wille@wille.blog.br',
      url='http://git.ibama.gov.br/csr/django-gis-states',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django',
          'simplejson'
      ]
      )
