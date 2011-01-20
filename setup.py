from setuptools import setup, find_packages

VERSION = '0.3.1'
LONG_DESC = """\
Fullhistory for Django
"""

setup(name='fullhistory',
      version=VERSION,
      description="Fullhistory for Django",
      long_description=LONG_DESC,
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      keywords='django history',
      author='Jason Kraus',
      author_email='zbyte64@gmail.com',
      url="http://code.google.com/p/fullhistory/",
      packages=find_packages(exclude=['ez_setup', 'examples', 'testproject', 'tests']),
      package_data = {
        'fullhistory': [
            'templates/admin/*.html',
            ],
        },
      zip_safe=False,
      install_requires=[
        'django',
      ],
      test_suite="testproject.runtests.runtests",
      )
