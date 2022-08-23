#!/usr/bin/env python3
#
# ls data/* | awk '{print "\""$1"\""}' | tr "\n" ","
#

import os
from setuptools import setup


setup(
    name='viaconstructor',
    version='0.3.4',
    author='Oliver Dippel',
    author_email='o.dippel@gmx.de',
    packages=['viaconstructor', 'viaconstructor.ext.cavaliercontours', 'viaconstructor.ext.HersheyFonts', 'viaconstructor.ext.meshcut', 'viaconstructor.ext.stl', 'viaconstructor.ext.svgpathtools', 'viaconstructor.input_plugins', 'viaconstructor.output_plugins', 'viaconstructor.preview_plugins', 'gcodepreview', 'dxfpreview'],
    package_data={'viaconstructor.ext.cavaliercontours': ['lib/libCavalierContours.so']},
    scripts=['bin/viaconstructor','bin/gcodepreview','bin/dxfpreview'],
    url='https://github.com/multigcs/viaconstructor',
    license='LICENSE',
    description='python based cam-tool to convert dxf into gcode',
    long_description=open('README.md').read(),
    install_requires=["PyQt5", "ezdxf", "PyOpenGL", "Pillow", "pygame", "pyclipper", "setproctitle", "freetype-py", "python-utils", "svgwrite", "matplotlib"],
    include_package_data=True,
    data_files = [ ('data', ["data/delete.png","data/exit.png","data/flip-x.png","data/flip-y.png","data/load-setup-gcode.png","data/load-setup.png","data/open.png","data/repair.png","data/rotate.png","data/save-gcode.png","data/save.png","data/save-setup-as.png","data/save-setup.png","data/scale.png","data/select.png","data/start.png","data/tab-selector.png","data/view-2d.png","data/view-reset.png"]) ]
)

