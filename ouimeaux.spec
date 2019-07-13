#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ouimeaux
Version  : 0.8
Release  : 4
URL      : https://files.pythonhosted.org/packages/a3/3a/7b3677d29896282314e492d123a1e72fa29f263be4892188aa7d54aa769f/ouimeaux-0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/a3/3a/7b3677d29896282314e492d123a1e72fa29f263be4892188aa7d54aa769f/ouimeaux-0.8.tar.gz
Summary  : Open source control for Belkin WeMo devices
Group    : Development/Tools
License  : BSD-3-Clause Python-2.0
Requires: ouimeaux-bin = %{version}-%{release}
Requires: ouimeaux-license = %{version}-%{release}
Requires: ouimeaux-python = %{version}-%{release}
Requires: ouimeaux-python3 = %{version}-%{release}
Requires: PyYAML
Requires: gevent
Requires: python-future
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3

%description
==============================
ouimeaux
==============================
.. image:: https://badge.fury.io/py/ouimeaux.png
:target: http://badge.fury.io/py/ouimeaux

.. image:: https://travis-ci.org/iancmcc/ouimeaux.png?branch=develop
:target: https://travis-ci.org/iancmcc/ouimeaux

%package bin
Summary: bin components for the ouimeaux package.
Group: Binaries
Requires: ouimeaux-license = %{version}-%{release}

%description bin
bin components for the ouimeaux package.


%package license
Summary: license components for the ouimeaux package.
Group: Default

%description license
license components for the ouimeaux package.


%package python
Summary: python components for the ouimeaux package.
Group: Default
Requires: ouimeaux-python3 = %{version}-%{release}

%description python
python components for the ouimeaux package.


%package python3
Summary: python3 components for the ouimeaux package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ouimeaux package.


%prep
%setup -q -n ouimeaux-0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549313579
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ouimeaux
cp LICENSE %{buildroot}/usr/share/package-licenses/ouimeaux/LICENSE
cp ouimeaux/pysignals/LICENSE.txt %{buildroot}/usr/share/package-licenses/ouimeaux/ouimeaux_pysignals_LICENSE.txt
cp ouimeaux/pysignals/license.python.txt %{buildroot}/usr/share/package-licenses/ouimeaux/ouimeaux_pysignals_license.python.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wemo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ouimeaux/LICENSE
/usr/share/package-licenses/ouimeaux/ouimeaux_pysignals_LICENSE.txt
/usr/share/package-licenses/ouimeaux/ouimeaux_pysignals_license.python.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
