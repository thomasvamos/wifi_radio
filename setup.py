#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install

import platform
import os
import subprocess

data_files = [
        ('share/wifi_radio', ['LICENSE.md', 'LICENSE.md'])
    ]

class InstallSteps(install):

  def execute_command(self, command):
    try:
        try:
            path = subprocess.getoutput(command)
        except AttributeError:
            path = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return path.strip()
    except (subprocess.CalledProcessError, OSError):
        return "/lib/systemd/system"

  def run(self):

    global data_files

    if os.name == 'nt':
      pass
    else:
      distro = platform.dist()[0]
      distro_major_version = platform.dist()[1].split('.')[0]

      if distro == 'debian' and distro_major_version >= 7:
        data_files.append(('/usr/lib/systemd/system',
                          ['scripts/systemd/wifi_radio.service']))

    install.run(self)
    self.execute_command(["systemctl", "enable", "wifi_radio"])
    self.execute_command(["systemctl", "start", "wifi_radio"])

setup(name='wifi-radio',
      version='0.1',
      description='A wifi radio for raspberry pi',
      url='http://github.com/thomasvamos/wifi-radio',
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
          'RPi.GPIO==0.6.3',
          'python-mpd==0.3.0',
          'pyserial==3.4'
      ],
       # this will create the /usr/local/bin/wifi_radio entrypoint script
      entry_points={
        'console_scripts': [
          'wifi_radio = wifi_radio.wifi_radio:main'
        ]
      },
      cmdclass={'install': InstallSteps},
      zip_safe=False)
