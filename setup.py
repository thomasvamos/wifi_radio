#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install

import platform
import os

data_files = [
        ('share/wifi_radio', ['LICENSE.md', 'LICENSE.md'])
    ]

class InstallSteps(install):

  def run(self):

    global data_files

    print "=== OS NAME: " + os.name 
    print "=== DISTRO : " + platform.dist()[0]
    print "=== MAJRVR : " + platform.dist()[1].split('.')[0]


    if os.name == 'nt':
      pass
    else:
      distro = platform.dist()[0]
      distro_major_version = platform.dist()[1].split('.')[0]

      if distro == 'debian' and distro_major_version >= 7:
        data_files.append(('/usr/lib/systemd/system',
                          ['install/wifi_radio.service']))

    install.run(self)
    



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
      data_files=data_files,
      install_requires=[
          'RPi.GPIO',
      ],
       # this will create the /usr/local/bin/wifi_radio entrypoint script
      entry_points={
        'console_scripts': [
          'wifi_radio = wifi_radio.wifi_radio:main'
        ]
      },
      cmdclass={'install': InstallSteps},
      zip_safe=False)