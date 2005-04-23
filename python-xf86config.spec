%define pyver %(python -c 'import sys ; print sys.version[:3]')

Summary:	Python wrappers for libxf86config
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
Requires:	glib2
Requires:	python >= %{pyver}
ExcludeArch:	s390 s390x ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python wrappers for the X server config file library libxf86config.
It is used to read and write X server configuration files.

%prep
%setup -q -n pyxf86config-%{version}

%build
#export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --x-libraries=/usr/X11R6/%{_lib} --with-python-version=%{pyver}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -d %{_libdir}/python%{pyver}/site-packages/xf86config.pyc ] ; then
  rm -f %{_libdir}/python%{pyver}/site-packages/xf86config.pyc
fi

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%{_libdir}/python?.?/site-packages/ixf86configmodule.so
%{_libdir}/python?.?/site-packages/xf86config.py
