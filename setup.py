# coding:utf-8

import os
import sys
import platform
from setuptools import setup, find_packages

config_sample = '''
qy_access_key_id: 'PETAEXPRESSACCESSKEYID'
qy_secret_access_key: 'PETAEXPRESSSECRETACCESSKEYEXAMPLE'
zone: 'ZONEID'
'''


def is_windows():
    return platform.system().lower() == 'windows'


def prepare_config_file():
    config_file = os.path.expanduser('~/.petaexpress/config.yaml')
    if os.path.exists(config_file):
        return

    d = os.path.dirname(config_file)
    if not os.path.exists(d):
        os.makedirs(d)

    with open(config_file, 'w') as fd:
        fd.write(config_sample)


def setup_petaexpress_completer():
    # only support linux
    if is_windows():
        return

    cmd = 'complete -C petaexpress_completer petaexpress'
    complete_file = '/etc/bash_completion.d/petaexpress-cli'
    complete_dir = os.path.dirname(complete_file)
    if os.path.exists(complete_dir) and os.access(complete_dir, os.W_OK):
        with open((complete_file), 'w') as fd:
            fd.write(cmd)
    else:
        with open(os.path.expanduser('~/.bash_profile'), 'a') as fd:
            fd.write('\n\n# PetaExpress CLI\n%s\n' % cmd)


if len(sys.argv) < 2 or sys.argv[1] != 'install':
    bin_scripts = ['bin/petaexpress', 'bin/petaexpress.cmd', 'bin/petaexpress_completer']
elif is_windows():
    bin_scripts = ['bin/petaexpress.cmd']
else:
    bin_scripts = ['bin/petaexpress', 'bin/petaexpress_completer']

setup(
    name='petaexpress-cli',
    version='1.3.12',
    description='Command Line Interface for PetaExpress.',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    keywords='petaexpress iaas qingstor cli',
    author='RAKSmart Team',
    author_email='zqiang@raksmart.com',
    url='https://docs.petaexpress.com',
    scripts=bin_scripts,
    packages=find_packages('.'),
    package_dir={'petaexpress-cli': 'petaexpress'},
    namespace_packages=['petaexpress'],
    include_package_data=True,
    install_requires=[
        'argparse>=1.1',
        'PyYAML>=3.1',
        'petaexpress-sdk>=1.2.12',
    ]
)

if len(sys.argv) >= 2 and sys.argv[1] == 'install':
    prepare_config_file()
    setup_petaexpress_completer()
