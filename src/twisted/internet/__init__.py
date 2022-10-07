# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Twisted Internet: Asynchronous I/O and Events.

Twisted Internet is a collection of compatible event-loops for Python. It contains
the code to dispatch events to interested observers and a portable API so that
observers need not care about which event loop is running. Thus, it is possible
to use the same code for different loops, from Twisted's basic, yet portable,
select-based loop to the loops of various GUI toolkits like GTK+ or Tk.
"""

from twisted.python.deprecate import deprecatedModuleAttribute
from twisted.python.versions import Version

deprecatedModuleAttribute(
    Version("Twisted", "NEXT", 0, 0),
    "Please use twisted.internet.gireactor instead.",
    "twisted.internet",
    "gtk2reactor",
)

deprecatedModuleAttribute(
    Version("Twisted", "NEXT", 0, 0),
    "Please use twisted.internet.gireactor instead.",
    "twisted.internet",
    "gtk3reactor",
)

deprecatedModuleAttribute(
    Version("Twisted", "NEXT", 0, 0),
    "Please use twisted.internet.gireactor instead.",
    "twisted.internet",
    "glib2reactor",
)

del Version, deprecatedModuleAttribute
