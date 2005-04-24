# $Revision: 1.3 $
Summary:	Python wrappers for libxf86config
Summary(pl):	Pythonowe dowi±zania do libxf86config
Name:		python-xf86config
Version:	0.3.19
Release:	1
License:	GPL
Group:		System Environment/Libraries
Source0:	pyxf86config-%{version}.tar.gz
# Source0-md5:	5421d1bc0038344df6bd11e8d0db435d
URL:		http://www.redhat.com/
BuildRequires:	X11-devel
BuildRequires:	glib2-devel
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python
Requires:	glib2
ExcludeArch:	s390 s390x ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python wrappers for the X server config file library libxf86config.
It is used to read and write X server configuration files.

%description -l pl
Pythonowe dowi±zania do biblioteki pliku konfiguracyjnego X serwera
libxf86config. Jest ona wykorzystywana do odczytywania i zapisywania
plików konfiguracyjnych X serwera.

%prep
%setup -q -n pyxf86config-%{version}

%build
#export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure \
	--x-libraries=/usr/X11R6/%{_lib} \
	--with-python-version=%{py_ver}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -d %{py_sitedir}/xf86config.pyc ] ; then
  rm -f %{py_sitedir}/xf86config.pyc
fi

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%{py_sitedir}/ixf86configmodule.so
%{py_sitedir}/xf86config.py
