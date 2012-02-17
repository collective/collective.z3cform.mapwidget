from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.z3cform.mapwidget',
      version=version,
      description="z3c.form map widget",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='z3c.form form widget collective.geo map OpenLayers',
      author='collective.geo Project',
      author_email='collectivegeo-discussion@lists.coactivate.org',
      url='http://www.coactivate.org/projects/collectivegeo/project-home',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.z3cform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.geo.mapwidget',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
