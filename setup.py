from setuptools import setup, find_packages

import os

long_description = open(os.path.join('Products', 'PloneHotfix2013XXXX', "README.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

version = '1.0'

setup(name='Products.PloneHotfix2013XXXX',
      version=version,
      description="Various Plone hotfixes, 2013-XX-XX",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone security hotfix patch',
      author='Plone Security Team',
      author_email='security@plone.org',
      url='http://github.com/plone',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """
      )
