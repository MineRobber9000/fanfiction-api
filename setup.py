from setuptools import setup

setup(name='fanfiction-api',
      version='1.1',
      description='Simple API to fanfiction.net',
      download_url='https://github.com/MarsCapone/fanfiction-api',
      url='https://marscapone.github.io/fanfiction-api',
      author='Samson Danziger',
      author_email='samson.danziger@gmail.com',
      packages=['ff'],
      install_requires=[
          'PyYAML',
          'pdfkit',
          'beautifulsoup4',
          'Ebooklib',
          'requests',
          'weasyprint'
      ],
      entry_points={
          'console_scripts': [
              'ffdownload=ff.console:ffdownload',
          ],
      })
