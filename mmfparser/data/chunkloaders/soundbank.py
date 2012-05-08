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

import zlib

from mmfparser.loader import DataLoader
from mmfparser.bitdict import BitDict
from mmfparser.bytereader import ByteReader

class BaseSound(DataLoader):
    def getType(self):
        header = self.data[:4]
        if self.data[:4] == 'RIFF':
            return 'WAV'
        elif self.data[:4] == 'AIFF':
            return 'AIFF'
        elif self.data[:4] == 'OggS':
            return 'OGG'
        else:
            # assume MOD
            return 'MOD'

SOUND_FLAGS = BitDict(
    'Wave',
    'MIDI',
    None, None,
    'LoadOnCall',
    'PlayFromDisk',
    'Loaded'
)

class SoundItem(BaseSound):
    handle = None
    checksum = None
    references = None
    flags = None
    name = None
    data = None
    
    def initialize(self):
        self.flags = SOUND_FLAGS.copy()
    
    def read(self, reader):
        self.handle = reader.readInt(True)
        self.checksum = reader.readInt()
        self.references = reader.readInt()
        decompressedLenght = reader.readInt()
        self.flags.setFlags(reader.readInt(True))
        reserved = reader.readInt()
        nameLenght = reader.readInt()
        if self.settings.get('compressed', True):
            size = reader.readInt()
            data = zlib.decompress(reader.read(size))
        else:
            data = reader.read(decompressedLenght)
        self.data = data[nameLenght:]
        self.name = data[:nameLenght].replace("\x00", '')
    
    def write(self, reader):
        reader.writeInt(self.handle, True)
        reader.writeInt(self.checksum)
        reader.writeInt(self.references)
        reader.writeInt(len(self.data) + len(self.name) + 1)
        reader.writeInt(self.flags.getFlags())
        reader.writeInt(0)
        reader.writeInt(len(self.name) + 1)
        reader.write(self.name + '\x00')
        reader.write(self.data)

class JavaSound(BaseSound):
    handle = None
    name = None
    data = None
    def read(self, reader):
        self.handle = reader.readShort()
        size = reader.readInt()
        self.data = reader.read(size)

class FlashSound(BaseSound):
    handle = None
    name = None
    data = None
    def read(self, reader):
        self.handle = reader.readShort()
        self.name = reader.readString(reader.readShort())

class SoundBank(DataLoader):
    items = None
    
    def initialize(self):
        self.items = []

    def read(self, reader):
        debug = self.settings.get('debug', False)
        java = self.settings.get('java', False)
        flash = self.settings.get('flash', False)

        if debug:
            path = reader.readString()
            reader = ByteReader(open(path, 'rb'))
            reader.skipBytes(4)
    
        if java:
            numberOfItems = reader.readShort()
            itemsToRead = reader.readShort()
            if flash:
                itemClass = FlashSound
            else:
                itemClass = JavaSound
        else:
            itemsToRead = reader.readInt()
            itemClass = SoundItem

        compressed = not debug
            
        self.items = [self.new(itemClass, reader, compressed = compressed)
            for _ in xrange(itemsToRead)]
        
        self.names = dict([(item.name, item) for  item in self.items])
    
    def fromHandle(self, handle):
        return [item for item in self.items if item.handle == handle][0]
    
    def write(self, reader):
        reader.writeInt(len(self.items))
        for item in self.items:
            item.write(reader)

__all__ = ['SoundBank']