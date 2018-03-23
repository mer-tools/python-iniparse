%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Name:       python-iniparse
Summary:    Python Module for Accessing and Modifying Configuration Data in INI files
Version:    0
Release:    1
Group:      Development/Libraries
License:    MIT
BuildArch:  noarch
URL:        http://code.google.com/p/iniparse/
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  python-devel
%if 0%{?suse_version}
BuildRequires:  python-setuptools
%else
BuildRequires:  python-setuptools-devel
%endif

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
iniparse is an INI parser for Python which is API compatible
with the standard library's ConfigParser, preserves structure of INI
files (order of sections & options, indentation, comments, and blank
lines are preserved when data is updated), and is more convenient to
use.

%prep
%setup -q -n %{name}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

# fixes
chmod 644 html/index.html

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} -O1 --prefix=%{_prefix}

rm -rf $RPM_BUILD_ROOT/usr/share/doc/iniparse-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{_docdir}/*
%{python_sitelib}/*
