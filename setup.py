from setuptools import setup, find_packages

version = '2.3.dev0'

setup(name='collective.z3cform.mapwidget',
      version=version,
      description="z3c.form map widget",
      long_description=(
          open("README.rst").read() + "\n" +
          open("CHANGES.rst").read()
      ),
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
      packages=find_packages('src'),
      package_dir={'': 'src'},
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
