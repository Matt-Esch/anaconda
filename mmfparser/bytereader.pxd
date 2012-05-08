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

from libc.stdio cimport FILE

cdef class ByteReader:
    cdef unsigned char * buffer
    cdef unsigned int start, pos, data_size, lastPosition
    cdef bytes original
    cdef bint shared
    cdef FILE * fp
    cdef object python_fp
    
    cpdef int tell(self)
    cpdef data(self)
    cpdef bint seek(self, int pos, int mode = ?)
    cpdef read(self, int size = ?)
    cpdef adjust(self, int to)
    cpdef size_t size(self)
    cpdef short readByte(self, bint asUnsigned = ?)
    cpdef int readShort(self, bint asUnsigned = ?)
    cpdef float readFloat(self)
    cpdef double readDouble(self)
    cpdef readInt(self, bint asUnsigned = ?)
    cpdef str readString(self, size = ?)
    cpdef unicode readUnicodeString(self)
    cpdef tuple readColor(self)
    cpdef ByteReader readReader(self, size_t size)
    cpdef bint write(self, bytes data)
    cpdef bint write_size(self, char * data, size_t size)
    cpdef bint skipBytes(self, size_t n)
    cpdef bint rewind(self, size_t n)
    cdef void _read(self, void * value, int size)