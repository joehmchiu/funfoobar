from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funfoobar',
      version='0.7',
      description='The funniest joke in the world',
      long_description='Really, the funniest around.',
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
      include_package_data=True,
      zip_safe=False
)
