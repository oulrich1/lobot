from setuptools import setup, find_packages
import lobot


setup(name='lobot',
      version=lobot.__version__,
      author='Scott LaVigne',
      author_email='pyrated@gmail.com',
      url='https://github.com/pyrated/lobot',
      license='MIT',
      description='An extensible IRC bot',
      download_url='https://github.com/pyrated/lobot.git',
      packages=find_packages(),
      scripts=['bin/lobot'],
      requires=open('requirements.txt').read().splitlines(),
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Environment :: Console',
            'Programming Language :: Python :: 3.5',
      ]
      )
