#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-urwid
Version  : 1.3.1
Release  : 2
URL      : https://pypi.python.org/packages/source/u/urwid/urwid-1.3.1.tar.gz
Source0  : https://pypi.python.org/packages/source/u/urwid/urwid-1.3.1.tar.gz
Summary  : A full-featured console (xterm et al.) user interface library
Group    : Development/Tools
License  : LGPL-2.1
Requires: python-urwid-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://travis-ci.org/wardi/urwid.png?branch=master
:alt: build status
:target: https://travis-ci.org/wardi/urwid/

%package python
Summary: python components for the python-urwid package.
Group: Default

%description python
python components for the python-urwid package.


%prep
%setup -q -n urwid-1.3.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
