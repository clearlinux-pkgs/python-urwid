#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-urwid
Version  : 2.1.2
Release  : 55
URL      : https://files.pythonhosted.org/packages/94/3f/e3010f4a11c08a5690540f7ebd0b0d251cc8a456895b7e49be201f73540c/urwid-2.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/3f/e3010f4a11c08a5690540f7ebd0b0d251cc8a456895b7e49be201f73540c/urwid-2.1.2.tar.gz
Summary  : A full-featured console (xterm et al.) user interface library
Group    : Development/Tools
License  : LGPL-2.1
Requires: python-urwid-license = %{version}-%{release}
Requires: python-urwid-python = %{version}-%{release}
Requires: python-urwid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

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
Requires: python-urwid-python3 = %{version}-%{release}

%description python
python components for the python-urwid package.


%package python3
Summary: python3 components for the python-urwid package.
Group: Default
Requires: python3-core
Provides: pypi(urwid)

%description python3
python3 components for the python-urwid package.


%prep
%setup -q -n urwid-2.1.2
cd %{_builddir}/urwid-2.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612915777
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-urwid
cp %{_builddir}/urwid-2.1.2/COPYING %{buildroot}/usr/share/package-licenses/python-urwid/4df5d4b947cf4e63e675729dd3f168ba844483c7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-urwid/4df5d4b947cf4e63e675729dd3f168ba844483c7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
