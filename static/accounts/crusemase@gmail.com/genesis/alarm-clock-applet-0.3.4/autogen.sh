#!/bin/sh
# Run this to generate all the initial makefiles, etc.

srcdir=`dirname $0`
test -z "$srcdir" && srcdir=.

PKG_NAME="alarm-clock-applet"

(test -f $srcdir/configure.ac \
  && test -f $srcdir/src/alarm-applet.c) || {
    echo -n "**Error**: Directory "\`$srcdir\'" does not look like the"
    echo " top-level $PKG_NAME directory"
    exit 1
}


which gnome-autogen.sh || {
    echo "You need to install gnome-common"
    exit 1
}

REQUIRED_AUTOMAKE_VERSION=1.9
REQUIRED_INTLTOOL_VERSION=0.40.0

#USE_GNOME2_MACROS=1 \
#USE_COMMON_DOC_BUILD=yes \
. gnome-autogen.sh
