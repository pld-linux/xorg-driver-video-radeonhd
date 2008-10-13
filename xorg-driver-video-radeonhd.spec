Summary:	X.org video driver for AMD GPG r5xx/r6xx chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart z układami AMD GPG r5xx/r6xx
Name:		xorg-driver-video-radeonhd
Version:	1.2.3
Release:	2
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-radeonhd-%{version}.tar.bz2
# Source0-md5:	5463c6a1f77861947a1f56b349a42094
Patch0:		%{name}-am.patch
Patch1:		%{name}-be.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel	
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.1.0
Obsoletes:	xorg-driver-video-avivo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for AMD GPG r5xx/r6xx chipsets. Supported adapters:
- RV505 (Radeon X1550, X1550 64bit)
- RV515 (Radeon X1300, X1550, X1600; FireGL V3300, V3350)
- RV516 (Radeon X1300, X1550, X1550 64bit, X1600; FireMV 2250)
- R520 (Radeon X1800; FireGL V5300, V7200, V7300, V7350)
- RV530 (Radeon X1300 XT, X1600, X1600 Pro, X1650; FireGL V3400, V5200)
- RV535 (Radeon X1300, X1650
- RV550 (Radeon X2300 HD)
- RV560 (Radeon X1650)
- RV570 (Radeon X1950, X1950 GT; FireGL V7400)
- R580 (Radeon X1900, X1950; AMD Stream Processor)
- R600 (Radeon HD 2900 GT/Pro/XT; FireGL V7600, V8600, V8650)
- RV610 (Radeon HD 2350, HD 2400 Pro/XT, HD 2400 Pro AGP; FireGL V4000)
- RV630 (Radeon HD 2600 LE/Pro/XT, HD 2600 Pro/XT AGP; Gemini RV630; FireGL V3600/V5600)
- M52 (Mobility Radeon X1300)
- M54 (Mobility Radeon X1400; M54-GL)
- M56 (Mobility Radeon X1600; Mobility FireGL V5200)
- M58 (Mobility Radeon X1800, X1800 XT; Mobility FireGL V7100, V7200)
- M62 (Mobility Radeon X1350)
- M64 (Mobility Radeon X1450, X2300)
- M66 (Mobility Radeon X1700, X1700 XT; FireGL V5250)
- M68 (Mobility Radeon X1900)
- M71 (Mobility Radeon HD 2300)
- M72 (Mobility Radeon HD 2400; Radeon E2400)
- M74 (Mobility Radeon HD 2400 XT)
- M76 (Mobility Radeon HD 2600; (Gemini ATI) Mobility Radeon HD 2600 XT)
- RS690 (Radeon X1200)
- RS740, RS740, RS740M

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart z układami AMD GPG r5xx/r6xx.
Obsługiwane karty:
- RV505 (Radeon X1550, X1550 64bit)
- RV515 (Radeon X1300, X1550, X1600; FireGL V3300, V3350)
- RV516 (Radeon X1300, X1550, X1550 64bit, X1600; FireMV 2250)
- R520 (Radeon X1800; FireGL V5300, V7200, V7300, V7350)
- RV530 (Radeon X1300 XT, X1600, X1600 Pro, X1650; FireGL V3400, V5200)
- RV535 (Radeon X1300, X1650
- RV550 (Radeon X2300 HD)
- RV560 (Radeon X1650)
- RV570 (Radeon X1950, X1950 GT; FireGL V7400)
- R580 (Radeon X1900, X1950; AMD Stream Processor)
- R600 (Radeon HD 2900 GT/Pro/XT; FireGL V7600, V8600, V8650)
- RV610 (Radeon HD 2350, HD 2400 Pro/XT, HD 2400 Pro AGP; FireGL V4000)
- RV630 (Radeon HD 2600 LE/Pro/XT, HD 2600 Pro/XT AGP; Gemini RV630; FireGL V3600/V5600)
- M52 (Mobility Radeon X1300)
- M54 (Mobility Radeon X1400; M54-GL)
- M56 (Mobility Radeon X1600; Mobility FireGL V5200)
- M58 (Mobility Radeon X1800, X1800 XT; Mobility FireGL V7100, V7200)
- M62 (Mobility Radeon X1350)
- M64 (Mobility Radeon X1450, X2300)
- M66 (Mobility Radeon X1700, X1700 XT; FireGL V5250)
- M68 (Mobility Radeon X1900)
- M71 (Mobility Radeon HD 2300)
- M72 (Mobility Radeon HD 2400; Radeon E2400)
- M74 (Mobility Radeon HD 2400 XT)
- M76 (Mobility Radeon HD 2600; (Gemini ATI) Mobility Radeon HD 2600 XT)
- RS690 (Radeon X1200)
- RS740, RS740, RS740M

%prep
%setup -q -n xf86-video-radeonhd-%{version}
%patch0 -p1
%patch1 -p1

%ifarch %{ix86} %{x8664}
ln utils/conntest/README README.conntest
%endif

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
%doc COPYING README*
# x86-specific VBIOS memory access
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_bindir}/rhd_*
%endif
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/radeonhd_drv.so
%{_mandir}/man4/radeonhd.4*
