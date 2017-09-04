import logging

logger = logging.getLogger("USB.Classes")

from .HID import HID

# Enumerate the handlers we have added
handlers = {
        0x3:  HID
        }

# Describe the base classes
classes = {
        0x0:  'Use Interface Descriptors',
        0x1:  'Audio',
        0x2:  'Communications and CDC Control',
        0x3:  'HID – Human Interface Device',
        0x5:  'Physical',
        0x6:  'Still Imaging',
        0x7:  'Printer',
        0x8:  'Mass Storage',
        0x9:  'Hub',
        0xa:  'CDC-Data',
        0xb:  'Smart Card',
        0xd:  'Content Security',
        0xe:  'Video',
        0xf:  'Personal Healthcare',
        0x10: 'Audio/Video Devices',
        0x11: 'Billboard Device',
        0x12: 'USB Type-C Bridge Device',
        0xdc: 'Diagnostic Device',
        0xe0: 'Wireless Controller',
        0xef: 'Miscellaneous',
        0xfe: 'Application Specific',
        0xff: 'Vendor Specific'
    }
