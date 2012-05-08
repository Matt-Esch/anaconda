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

systemDict = {
    2 : {
        -81 : 'ObjectClicked' # SPRCLICK
    },
    4 : {
        -83 : 'AnswerMatches',
        -82 : 'AnswerFalse',
        -81 : 'AnswerTrue'
    },
    7 : {
        -81 : 'CompareCounter'
    },
    9 : {
        -84 : 'SubApplicationPaused',
        -83 : 'SubApplicationVisible',
        -82 : 'SubApplicationFinished',
        -81 : 'SubApplicationFrameChanged'
    },
    -2 : {
        -1 : 'SampleNotPlaying',
        -9 : 'ChannelPaused',
        -8 : 'ChannelNotPlaying',
        -7 : 'MusicPaused',
        -6 : 'SamplePaused',
        -5 : 'MusicFinished',
        -4 : 'NoMusicPlaying',
        -3 : 'NoSamplesPlaying',
        -2 : 'SpecificMusicNotPlaying'
    },
    -7 : {
        -1 : 'PLAYERPLAYING',
        -6 : 'PlayerKeyDown',
        -5 : 'PlayerDied',
        -4 : 'PlayerKeyPressed',
        -3 : 'NumberOfLives',
        -2 : 'CompareScore'
    },
    -6 : {
        -2 : 'KeyDown',
        -12 : 'MouseWheelDown',
        -11 : 'MouseWheelUp',
        -10 : 'MouseVisible',
        -9 : 'AnyKeyPressed',
        -8 : 'WhileMousePressed',
        -7 : 'ObjectClicked',
        -6 : 'MouseClickedInZone',
        -5 : 'MouseClicked',
        -4 : 'MouseOnObject',
        -3 : 'MouseInZone',
        -1 : 'KeyPressed'
    },
    -5 : {
        -2 : 'AllObjectsInZone', # AllObjectsInZone_Old
        -23 : 'PickObjectsInLine',
        -22 : 'PickFlagOff',
        -21 : 'PickFlagOn',
        -20 : 'PickAlterableValue',
        -19 : 'PickFromFixed',
        -18 : 'PickObjectsInZone',
        -17 : 'PickRandomObject',
        -16 : 'PickRandomObjectInZone',
        -15 : 'CompareObjectCount',
        -14 : 'AllObjectsInZone',
        -13 : 'NoAllObjectsInZone',
        -12 : 'PickFlagOff', # PickFlagOff_Old
        -11 : 'PickFlagOn', # PickFlagOn_Old
        -8 : 'PickAlterableValue', # PickAlterableValue_Old
        -7 : 'PickFromFixed', # PickFromFixed_Old
        -6 : 'PickObjectsInZone', # PickObjectsInZone_Old
        -5 : 'PickRandomObject', # PickRandomObject_Old
        -4 : 'PickRandomObjectInZoneOld',
        -3 : 'CompareObjectCount', # CompareObjectCount_Old
        -1 : 'NoAllObjectsInZone' # NoAllObjectsInZone_Old
    },
    -4 : {
    -2 : 'TimerLess',
    -5 : 'CompareAwayTime',
    -4 : 'Every',
    -3 : 'TimerEquals',
    -1 : 'TimerGreater'
    },
    -3 : {
        -1 : 'StartOfFrame',
        -10 : 'FrameSaved',
        -9 : 'FrameLoaded',
        -8 : 'ApplicationResumed',
        -7 : 'VsyncEnabled',
        -6 : 'IsLadder',
        -5 : 'IsObstacle',
        -4 : 'EndOfApplication',
        -3 : 'LEVEL',
        -2 : 'EndOfFrame'
    },
    -1 : {
        -11 : 'GroupEnd',
        -26 : 'Chance',
        -25 : 'OrLogical',
        -24 : 'OrFiltered',
        -23 : 'OnGroupActivation',
        -22 : 'ClipboardDataAvailable',
        -21 : 'CloseSelected',
        -20 : 'CompareGlobalString',
        -19 : 'MenuVisible',
        -18 : 'MenuEnabled',
        -17 : 'MenuChecked',
        -16 : 'OnLoop',
        -15 : 'FilesDropped',
        -14 : 'MenuSelected',
        -13 : 'RECORDKEY',
        -12 : 'GroupActivated',
        -2 : 'Never',
        -10 : 'NewGroup',
        -9 : 'Remark',
        -8 : 'CompareGlobalValue',
        -7 : 'NotAlways',
        -6 : 'Once',
        -5 : 'Repeat',
        -4 : 'RestrictFor',
        -3 : 'Compare',
        -1 : 'Always'
    }
}

extensionDict = {
    -11 : 'EnteringPlayfield',
    -40 : 'IsStrikeOut',
    -39 : 'IsUnderline',
    -38 : 'IsItalic',
    -37 : 'IsBold',
    -36 : 'CompareAlterableString',
    -35 : 'NamedNodeReached',
    -34 : 'PickRandom',
    -33 : 'AllDestroyed',
    -32 : 'NumberOfObjects',
    -31 : 'NoObjectsInZone',
    -30 : 'ObjectsInZone',
    -29 : 'ObjectVisible',
    -28 : 'ObjectInvisible',
    -27 : 'CompareAlterableValue',
    -26 : 'CompareFixedValue',
    -25 : 'FlagOn',
    -24 : 'FlagOff',
    -23 : 'IsOverlappingBackground',
    -22 : 'NearWindowBorder',
    -21 : 'PathFinished',
    -20 : 'NodeReached',
    -19 : 'CompareAcceleration',
    -18 : 'CompareDeceleration',
    -17 : 'CompareX',
    -16 : 'CompareY',
    -15 : 'CompareSpeed',
    -14 : 'OnCollision',
    -13 : 'OnBackgroundCollision',
    -12 : 'LeavingPlayfield',
    -2 : 'AnimationFinished',
    -10 : 'OutsidePlayfield',
    -9 : 'InsidePlayfield',
    -8 : 'FacingInDirection',
    -7 : 'MovementStopped',
    -6 : 'Bouncing',
    -5 : 'Reversed',
    -4 : 'IsOverlapping',
    -3 : 'AnimationPlaying',
    -1 : 'AnimationFrame'
}

