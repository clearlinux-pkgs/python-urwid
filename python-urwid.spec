#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-urwid
Version  : 2.0.1
Release  : 26
URL      : http://pypi.debian.net/urwid/urwid-2.0.1.tar.gz
Source0  : http://pypi.debian.net/urwid/urwid-2.0.1.tar.gz
Summary  : A full-featured console (xterm et al.) user interface library
Group    : Development/Tools
License  : LGPL-2.1
Requires: python-urwid-python3
Requires: python-urwid-license
Requires: python-urwid-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
About
        =====
        
        Urwid is a console user interface library for Python.

%package license
Summary: license components for the python-urwid package.
Group: Default

%description license
license components for the python-urwid package.


%package python
Summary: python components for the python-urwid package.
Group: Default
Requires: python-urwid-python3

%description python
python components for the python-urwid package.


%package python3
Summary: python3 components for the python-urwid package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-urwid package.


%prep
%setup -q -n urwid-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530329982
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-urwid
cp COPYING %{buildroot}/usr/share/doc/python-urwid/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/python-urwid/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
