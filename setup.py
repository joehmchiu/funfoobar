from setuptools import setup

# python setup.py bdist_wheel
# sudo rm -rf build/ dist/ funfoobar.egg-info/ funfoobar/__pycache__/
def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funfoobar',
      version='0.9',
      description='The funniest joke in the world',
      long_description=readme(),
      scripts=['bin/funniest-joke'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='http://github.com/joehmchiu/funfoobar',
      author='Joe Chiu',
      author_email='joehmchiu@gmail.com',
      license='MIT',
      packages=['funfoobar'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['funniest-joke=funfoobar.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False
)
