# TODO:
# - build conntest on all archs
#
# Conditional build:
%define snap	20071125
Summary:	X.org video drivers for AMD GPG r5xx/r6xx chipsets
Summary(pl.UTF-8):	Sterowniki obrazu X.org dla kart z chipsetem AMD GPG r5xx/r6xx
Name:		xorg-driver-video-radeonhd
Version:	0.0.4
Release:	0.%{snap}.1
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	xf86-video-radeonhd-%{snap}.tar.bz2
# Source0-md5:	cd17f994796fdac69d735c6d2145bdcd
Patch0:		%{name}-am.patch
URL:		http://www.x.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video drivers for AMD GPG r5xx/r6xx chipsets.

%description -l pl.UTF-8
Sterowniki obrazu X.org dla kart z chipsetem AMD GPG r5xx/r6xx.

%prep
%setup -q -n xf86-video-radeonhd
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc utils/conntest/README
%attr(755,root,root) %{_bindir}/rhd_conntest
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/radeonhd_drv.so
%{_mandir}/man4/*.*
