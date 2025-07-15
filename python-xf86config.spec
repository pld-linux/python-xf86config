Summary:	Python wrappers for libxf86config
Summary(pl.UTF-8):	Pythonowe dowiązania do libxf86config
Name:		python-xf86config
Version:	0.3.37
Release:	6
License:	GPL
Group:		Libraries
# https://fedorahosted.org/releases/p/y/pyxf86config/ (not yet)
Source0:	pyxf86config-%{version}.tar.bz2
# Source0-md5:	0ea1b54c1a9cbff7f67126a6c048361e
Patch0:		%{name}-libtool.patch
URL:		https://fedoraproject.org/wiki/Pyxf86config
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	xorg-xserver-server-devel >= 1.1.0-0.3
%pyrequires_eq	python-libs
ExcludeArch:	ppc64 s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python wrappers for the X server config file library libxf86config. It
is used to read and write X server configuration files.

%description -l pl.UTF-8
Pythonowe dowiązania do biblioteki pliku konfiguracyjnego X serwera
libxf86config. Jest ona wykorzystywana do odczytywania i zapisywania
plików konfiguracyjnych X serwera.

%prep
%setup -q -n pyxf86config-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-python-version=%{py_ver}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%attr(755,root,root) %{py_sitedir}/ixf86configmodule.so
%{py_sitedir}/xf86config.py[co]
