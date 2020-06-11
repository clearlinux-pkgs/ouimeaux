#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ouimeaux
Version  : 0.8.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/42/d6/f7a8804e25b0831dd729b11e66b45e3ea2f72a1748aaabd56a58abaf7ad2/ouimeaux-0.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/d6/f7a8804e25b0831dd729b11e66b45e3ea2f72a1748aaabd56a58abaf7ad2/ouimeaux-0.8.2.tar.gz
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
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : gevent
BuildRequires : python-future
BuildRequires : requests
BuildRequires : six

%description
# ouimeaux
Open source control for Belkin WeMo devices
* Free software: BSD license
* Documentation: http://ouimeaux.rtfd.org.

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
Provides: pypi(ouimeaux)
Requires: pypi(future)
Requires: pypi(gevent)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the ouimeaux package.


%prep
%setup -q -n ouimeaux-0.8.2
cd %{_builddir}/ouimeaux-0.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591918075
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ouimeaux
cp %{_builddir}/ouimeaux-0.8.2/LICENSE %{buildroot}/usr/share/package-licenses/ouimeaux/bd94797889ab4f12d1037fa66c10dca1d6ab6cc3
cp %{_builddir}/ouimeaux-0.8.2/ouimeaux/pysignals/LICENSE.txt %{buildroot}/usr/share/package-licenses/ouimeaux/6b592f04d077053c80d47f3a8321d21aad45dd69
cp %{_builddir}/ouimeaux-0.8.2/ouimeaux/pysignals/license.python.txt %{buildroot}/usr/share/package-licenses/ouimeaux/e6e9a006706b5c1187a7ce23ca2135406cc0388d
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
/usr/share/package-licenses/ouimeaux/6b592f04d077053c80d47f3a8321d21aad45dd69
/usr/share/package-licenses/ouimeaux/bd94797889ab4f12d1037fa66c10dca1d6ab6cc3
/usr/share/package-licenses/ouimeaux/e6e9a006706b5c1187a7ce23ca2135406cc0388d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
