from setuptools import setup

setup(name='wifi-radio',
      version='0.1',
      description='A wifi radio for raspberry pi',
      url='http://github.com/th0m4d/wifi-radio',
      author='Thomas Vamos',
      author_email='mail@thomasvamos.de',
      classifiers=[  
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='wifi radio raspberrypi arduino retro',
      license='MIT',
      packages=['wifi_radio'],
      install_requires=[
          'RPi.GPIO',
      ],
      zip_safe=False)