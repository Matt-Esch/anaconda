# Copyright (c) Mathias Kaerlev 2012.

# This file is part of Anaconda.

# Anaconda is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Anaconda is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Anaconda.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import glob
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ALL = '-f' in sys.argv

from Cython.Compiler import Options
directive_defaults = Options.directive_defaults
Options.docstrings = False
if sys.argv[0].count('profile'):
    directive_defaults['profile'] = True

directive_defaults['cdivision'] = True # WIN, PERFORMANCE! <3
directive_defaults['infer_types'] = True # WIN, PERFORMANCE! <3
directive_defaults['wraparound'] = False # WIN, PERFORMANCE! <3

ext_modules = []
libraries = []
include_dirs = ['./mmfparser/player']

names = open('names.txt', 'rb').read().splitlines()

for name in names:
    ext_modules.append(Extension(name, ['./' + name.replace('.', '/') + '.pyx'],
        include_dirs = include_dirs))

ext_modules.append(Extension('mmfparser.player.collision', 
    [
        './mmfparser/player/collision.pyx'
    ], include_dirs = include_dirs, libraries = libraries))

ext_modules.append(Extension('mmfparser.player.extensions.AdvGameBoard.wrapper', 
    [
        './mmfparser/player/extensions/AdvGameBoard/wrapper.pyx'
    ], include_dirs = include_dirs, libraries = libraries, language = 'c++'))

util_libraries = []
if sys.platform == 'win32':
    util_libraries.append('imagehlp')

ext_modules.append(Extension('utils.icon', 
    [
        './utils/icon.pyx'
    ], include_dirs = include_dirs, libraries = libraries + util_libraries,
    language = 'c++'))

extra_link_args = []
opengl_libraries = []
if sys.platform == 'win32':
    opengl_libraries.append('opengl32')
elif sys.platform == 'linux2':
    opengl_libraries.append('GL')
elif sys.platform == 'darwin':
    extra_link_args.extend(['-framework', 'OpenGL'])

ext_modules.append(Extension('mmfparser.player.sprite', 
    [
        './mmfparser/player/sprite.pyx'
    ], include_dirs = include_dirs, libraries = libraries + opengl_libraries,
    extra_link_args=extra_link_args))

# Lacewing

if sys.platform == 'win32':
    lacewing_libraries = ['Ws2_32', 'Advapi32', 'Secur32', 'Crypt32', 'Mswsock']
    lacewing_sources = (
        glob.glob('./extensions/Lacewing/liblacewing/src/*.cc') +
        glob.glob('./extensions/Lacewing/liblacewing/src/windows/*.cc') +
        glob.glob('./extensions/Lacewing/liblacewing/src/relay/*.cc')
    )
    lacewing_link_args = []
else:
    lacewing_sources = []
    lacewing_link_args = ['./extensions/Lacewing/liblacewing/liblacewing.a']
    lacewing_libraries = []
    if sys.platform == 'linux2':
        lacewing_libraries.extend(['rt'])

ext_modules.append(Extension('extensions.Lacewing.wrapper', 
    [
        './extensions/Lacewing/wrapper.pyx'
    ] + lacewing_sources,
    include_dirs = include_dirs + ['./extensions/Lacewing/liblacewing/include',
                                   './extensions/Lacewing/'],
    extra_link_args = lacewing_link_args, libraries = lacewing_libraries,
    language = 'c++'))

# Steam

steam_libraries = ['steam_api']

root_path = './extensions/Steamworks/sdk'

steam_os_name = {'linux2' : 'linux32', 'darwin' : 'osx32', 'win32' : ''}[
    sys.platform]

steam_library_dirs = [os.path.join(root_path, 'redistributable_bin', 
    steam_os_name)]

ext_modules.append(Extension('extensions.Steamworks.wrapper', 
    [
        './extensions/Steamworks/wrapper.pyx'
    ],
    include_dirs = include_dirs + ['./extensions/Steamworks/'], 
    library_dirs = steam_library_dirs, libraries = steam_libraries, 
    language = 'c++'))

# distutils setup

if ALL:
    setup(
        name = 'mmfparser extensions',
        cmdclass = {'build_ext': build_ext},
        ext_modules = ext_modules
    )

else:
    setup(
        name = 'mmfparser extensions',
        ext_modules = cythonize(ext_modules)
    )
