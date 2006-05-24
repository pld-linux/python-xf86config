Summary:	Python wrappers for libxf86config
Summary(pl):	Pythonowe dowi±zania do libxf86config
Name:		python-xf86config
Version:	0.3.24
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	pyxf86config-%{version}.tar.gz
# Source0-md5:	43488299e096b3fed4f080579f9e7fbb
URL:		http://www.redhat.com/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-libs
ExcludeArch:	ppc64 s390 s390x
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
cp -f /usr/share/automake/config.* .
%configure \
	--with-python-version=%{py_ver}
%{__make} \
	AM_CFLAGS="-fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root) %{py_sitedir}/ixf86configmodule.so
%{py_sitedir}/xf86config.py
