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

"""
KcArray.mfx
Array object - ClickTeam (http://www.clickteam.com)
Copyright 1996-2006 Clickteam

Numeric or text array (up to 3 dimensions).

Ported to Python by Mathias Kaerlev
"""

from mmfparser.player.common import convert_path
from mmfparser.player.extensions.common import UserExtension, HiddenObject
from mmfparser.player.event.actions.common import Action
from mmfparser.player.event.conditions.common import Condition
from mmfparser.player.event.expressions.common import Expression

from mmfparser.bitdict import BitDict
from mmfparser.bytereader import ByteReader
from mmfarray import MMFArray
from mmfparser.exceptions import InvalidData

try:
    from mmfparser.player.dialog import open_file_selector, save_file_selector
except ImportError:
    pass

# Actions

class SetXDimension(Action):
    """
    Change Current Position->Set X dimension index to...

    Parameters:
    0: Set X dimension index to... (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        instance.objectPlayer.set_index(
            x = self.evaluate_expression(self.get_parameter(0)))

class SetYDimension(Action):
    """
    Change Current Position->Set Y dimension index to...

    Parameters:
    0: Set Y dimension index to... (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        instance.objectPlayer.set_index(
            y = self.evaluate_expression(self.get_parameter(0)))

class SetZDimension(Action):
    """
    Change Current Position->Set Z dimension index to...

    Parameters:
    0: Set Z dimension index to... (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        instance.objectPlayer.set_index(
            z = self.evaluate_expression(self.get_parameter(0)))

class AddOneZ(Action):
    """
    Change Current Position->Add 1 to X dimension index
    """
    def execute(self, instance):
        instance.objectPlayer.arrayZ += 1

class AddOneY(Action):
    """
    Change Current Position->Add 1 to Y dimension index
    """
    def execute(self, instance):
        instance.objectPlayer.arrayY += 1

class AddOneZ(Action):
    """
    Change Current Position->Add 1 to Z dimension index
    """
    def execute(self, instance):
        instance.objectPlayer.arrayZ += 1

class WriteValue(Action):
    """
    Write->Write Value to current position

    Parameters:
    0: Write Value to current position (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        instance.objectPlayer.write_value(self.evaluate_expression(
            self.get_parameter(0)))

class WriteString(Action):
    """
    Write->Write String to current position

    Parameters:
    0: Write String to current position (EXPSTRING, ExpressionParameter)
    """
    def execute(self, instance):
        instance.objectPlayer.write_value(self.evaluate_expression(
            self.get_parameter(0)))

class Clear(Action):
    """
    Clear array
    """
    def execute(self, instance):
        instance.objectPlayer.array.clear()

class Load(Action):
    """
    Files->Load array from file

    Parameters:
    0: Please select an array file (FILENAME, String)
    """
    def execute(self, instance):
        filename = convert_path(
            self.get_filename(self.get_parameter(0)))
        try:
            reader = ByteReader(open(filename, 'rb'))
            instance.objectPlayer.array.read(reader)
        except IOError:
            pass

class LoadWithSelector(Action):
    """
    Files->Load array from file via a file selector
    """
    def execute(self, instance):
        try:
            filename = open_file_selector()
            reader = ByteReader(open(filename, 'rb'))
            instance.objectPlayer.array.read(reader)
            file.close()
        except IOError:
            pass

class Save(Action):
    """
    Files->Save array to file

    Parameters:
    0: Please select an array file (FILENAME, String)
    """
    def execute(self, instance):
        filename = convert_path(
            self.get_filename(self.get_parameter(0)))
        try:
            open(filename, 'wb').write(
                instance.objectPlayer.array.generate().data())
        except IOError:
            pass

class SaveWithSelector(Action):
    """
    Files->Save array to file via a file selector
    """
    def execute(self, instance):
        try:
            filename = save_file_selector()
            file = open(filename, 'wb')
            file.write(
                instance.objectPlayer.array.generate().data())
            file.close()
        except IOError:
            pass

class WriteX(Action):
    """
    Write->Write Value to X

    Parameters:
    0: Enter value to write (EXPRESSION, ExpressionParameter)
    1: Enter X index (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        value = self.evaluate_expression(self.get_parameter(0))
        x = self.evaluate_expression(self.get_parameter(1))
        instance.objectPlayer.write_value(value, x = x)

class WriteXY(Action):
    """
    Write->Write Value to XY

    Parameters:
    0: Enter value to write (EXPRESSION, ExpressionParameter)
    1: Enter X index (EXPRESSION, ExpressionParameter)
    2: Enter Y index (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        value = self.evaluate_expression(self.get_parameter(0))
        x = self.evaluate_expression(self.get_parameter(1))
        y = self.evaluate_expression(self.get_parameter(2))
        instance.objectPlayer.write_value(value, x = x, y = y)

class WriteXYZ(Action):
    """
    Write->Write Value to XYZ

    Parameters:
    0: Enter value to write (EXPRESSION, ExpressionParameter)
    1: Enter X index (EXPRESSION, ExpressionParameter)
    2: Enter Y index (EXPRESSION, ExpressionParameter)
    3: Enter Z index (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        value = self.evaluate_expression(self.get_parameter(0))
        x = self.evaluate_expression(self.get_parameter(1))
        y = self.evaluate_expression(self.get_parameter(2))
        z = self.evaluate_expression(self.get_parameter(3))
        instance.objectPlayer.write_value(value, x = x, y = y, z = z)

class WriteStringX(Action):
    """
    Write->Write String to X

    Parameters:
    0: Enter string to write (EXPSTRING, ExpressionParameter)
    1: Enter X index (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        value = self.evaluate_expression(self.get_parameter(0))
        x = self.evaluate_expression(self.get_parameter(1))
        instance.objectPlayer.write_value(value, x = x)

class WriteStringXY(Action):
    """
    Write->Write String to XY

    Parameters:
    0: Enter string to write (EXPSTRING, ExpressionParameter)
    1: Enter X index (EXPRESSION, ExpressionParameter)
    2: Enter Y index (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        value = self.evaluate_expression(self.get_parameter(0))
        x = self.evaluate_expression(self.get_parameter(1))
        y = self.evaluate_expression(self.get_parameter(2))
        instance.objectPlayer.write_value(value, x = x, y = y)

class WriteStringXYZ(Action):
    """
    Write->Write String to XYZ

    Parameters:
    0: Enter string to write (EXPSTRING, ExpressionParameter)
    1: Enter X index (EXPRESSION, ExpressionParameter)
    2: Enter Y index (EXPRESSION, ExpressionParameter)
    3: Enter Z index (EXPRESSION, ExpressionParameter)
    """
    def execute(self, instance):
        value = self.evaluate_expression(self.get_parameter(0))
        x = self.evaluate_expression(self.get_parameter(1))
        y = self.evaluate_expression(self.get_parameter(2))
        z = self.evaluate_expression(self.get_parameter(3))
        instance.objectPlayer.write_value(value, x = x, y = y, z = z)

# Conditions

class AtEndX(Condition):
    """
    Is the index to the X dimension at end?
    """
    def check(self, instance):
        return instance.objectPlayer.arrayX == instance.objectPlayer.array.size[0]-1

class AtEndY(Condition):
    """
    Is the index to the Y dimension at end?
    """
    def check(self, instance):
        return instance.objectPlayer.arrayX == instance.objectPlayer.array.size[1]-1


class AtEndZ(Condition):
    """
    Is the index to the Z dimension at end?
    """
    def check(self, instance):
        return instance.objectPlayer.arrayX == instance.objectPlayer.array.size[1]-1

# Expressions

class PositionX(Expression):
    """
    Current position of X index
    Return type: Int
    """
    def get(self, instance):
        return instance.objectPlayer.arrayX

class PositionY(Expression):
    """
    Current position of Y index
    Return type: Int
    """
    def get(self, instance):
        return instance.objectPlayer.arrayY

class PositionZ(Expression):
    """
    Current position of Z index
    Return type: Int
    """
    def get(self, instance):
        return instance.objectPlayer.arrayZ

class ReadValue(Expression):
    """
    Read Value from current position
    Return type: Int
    """
    def get(self, instance):
        return instance.objectPlayer.read_value()

class ReadValueX(Expression):
    """
    Read Value from X position

    Parameters:
    0: Enter X offset (Int)
    Return type: Int
    """
    def get(self, instance):
        x = self.next_argument()
        return instance.objectPlayer.read_value(x = x)

class ReadValueXY(Expression):
    """
    Read Value from XY position

    Parameters:
    0: Enter X offset (Int)
    1: Enter Y offset (Int)
    Return type: Int
    """
    def get(self, instance):
        x = self.next_argument()
        y = self.next_argument()
        return instance.objectPlayer.read_value(x = x, y = y)

class ReadValueXYZ(Expression):
    """
    Read Value from XYZ position

    Parameters:
    0: Enter X offset (Int)
    1: Enter Y offset (Int)
    2: Enter Z offset (Int)
    Return type: Int
    """
    def get(self, instance):
        x = self.next_argument()
        y = self.next_argument()
        z = self.next_argument()
        return instance.objectPlayer.read_value(x = x, y = y, z = z)

class ReadString(Expression):
    """
    Read String from current position
    Return type: String
    """
    def get(self, instance):
        return instance.objectPlayer.read_value()

class ReadStringX(Expression):
    """
    Read String from X position

    Parameters:
    0: Enter X offset (Int)
    Return type: String
    """
    def get(self, instance):
        x = self.next_argument()
        return instance.objectPlayer.read_value(x = x)

class ReadStringXY(Expression):
    """
    Read String from XY position

    Parameters:
    0: Enter X offset (Int)
    1: Enter Y offset (Int)
    Return type: String
    """
    def get(self, instance):
        x = self.next_argument()
        y = self.next_argument()
        return instance.objectPlayer.read_value(x = x, y = y)

class ReadStringXYZ(Expression):
    """
    Read String from XYZ position

    Parameters:
    0: Enter X offset (Int)
    1: Enter Y offset (Int)
    2: Enter Z offset (Int)
    Return type: String
    """
    def get(self, instance):
        x = self.next_argument()
        y = self.next_argument()
        z = self.next_argument()
        return instance.objectPlayer.read_value(x = x, y = y, z = z)

class DimensionX(Expression):
    """
    X dimension
    Return type: Int
    """
    def get(self, instance):
        return instance.objectPlayer.array.size[0]

class DimensionY(Expression):
    """
    Y dimension
    Return type: Int
    """
    def get(self, instance):
        return instance.objectPlayer.array.size[1]
    
class DimensionZ(Expression):
    """
    Z dimension
    Return type: Int
    """
    def get(self, instance):
        return instance.objectPlayer.array.size[2]

class DefaultObject(HiddenObject):
    arrayX = 0
    arrayY = 0
    arrayZ = 0

    array = None
    def created(self, data):
        storage = self.get_storage()
        if storage:
            self.array = storage['value']
            return
        xDimension = data.readInt()
        yDimension = data.readInt()
        zDimension = data.readInt()
        flags = BitDict('Numeric', 'Text', 'Base1', 'Global')
        flags.setFlags(data.readInt())
        if flags['Base1']:
            self.arrayX = self.arrayY = self.arrayZ = 1
        # yeah, I think this is comprehensive too.
        self.array = array = MMFArray()
        if flags['Numeric']:
            arrayType = 'Numeric'
        else:
            arrayType = 'Text'
        array.flags = flags
        array.setup(xDimension, yDimension, zDimension, arrayType)
        self.get_storage()['value'] = array
    
    def write_value(self, value, x = None, y = None, z = None):
        x = x or self.arrayX
        y = y or self.arrayY
        z = z or self.arrayZ
        self.array.set(x, y, z, value)
    
    def read_value(self, x = None, y = None, z = None):
        x = x or self.arrayX
        y = y or self.arrayY
        z = z or self.arrayZ
        try:
            return self.array.get(x, y, z)
        except KeyError:
            return self.array.default
    
    def set_index(self, x = None, y = None, z = None):
        if x is not None:
            self.arrayX = x
        if y is not None:
            self.arrayY = y
        if z is not None:
            self.arrayZ = z

class KcArray(UserExtension):
    objectPlayer = DefaultObject
    
    actions = {
        0 : SetXDimension,
        1 : SetYDimension,
        2 : SetZDimension,
        3 : AddOneZ,
        4 : AddOneY,
        5 : AddOneZ,
        6 : WriteValue,
        7 : WriteString,
        8 : Clear,
        9 : Load,
        10 : LoadWithSelector,
        11 : Save,
        12 : SaveWithSelector,
        13 : WriteX,
        14 : WriteXY,
        15 : WriteXYZ,
        16 : WriteStringX,
        17 : WriteStringXY,
        18 : WriteStringXYZ
    }
    
    conditions = {
        0 : AtEndX,
        1 : AtEndY,
        2 : AtEndZ
    }
    
    expressions = {
        0 : PositionX,
        1 : PositionY,
        2 : PositionZ,
        3 : ReadValue,
        4 : ReadString,
        5 : ReadValueX,
        6 : ReadValueXY,
        7 : ReadValueXYZ,
        8 : ReadStringX,
        9 : ReadStringXY,
        10 : ReadStringXYZ,
        11 : DimensionX,
        12 : DimensionY,
        13 : DimensionZ
    }

extension = KcArray()

def get_extension():
    return extension
