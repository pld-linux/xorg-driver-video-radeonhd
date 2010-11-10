Summary:	X.org video driver for AMD GPG R5xx/R6xx/R7xx chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart z układami AMD GPG R5xx/R6xx/R7xx
Name:		xorg-driver-video-radeonhd
Version:	1.3.0
Release:	4
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-radeonhd-%{version}.tar.bz2
# Source0-md5:	7b6641aa9d836f1621b9b220ad6771b8
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
BuildRequires:	zlib-devel
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.2
Requires:	xorg-xserver-libdri >= 1.1.0
Requires:	xorg-xserver-libglx >= 1.1.0
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
- RV620 (Radeon HD 3450, HD 3470)
- RV630 (Radeon HD 2600 LE/Pro/XT, HD 2600 Pro/XT AGP; Gemini RV630; FireGL V3600/V5600)
- RV635 (Radeon HD 3650, HD 3670)
- RV670 (Radeon HD 3690, HD 3850, HD 3870; FireGL V7700; FireStream 9170)
- R680 (Radeon HD 3870 X2)
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
- M82 (Mobility Radeon HD 3400)
- M86 (Mobility Radeon HD 3650, HD 3670; Mobility FireGL V5700)
- M88 (Mobility Radeon HD 3850, HD 3850 X2, HD 3870, HD 3870 X2)
- RS600 (Radeon Xpress 1200, Xpress 1250)
- RS690 (Radeon X1200, X1250, X1270)
- RS740 (RS740, RS740M)
- RS780 (Radeon HD 3100/3200/3300)
- R700 (Radeon R700)
- RV710 (Radeon HD 4570, HD 4350)
- RV730 (Radeon HD 4670, HD 4650)
- RV470 (Radeon HD 4770)
- RV770 (Radeon HD 4800; Everest, K2, Denali ATI FirePro)
- RV790 (Radeon HD 4890)
- M92 (Mobility Radeon HD 4330, HD 4530, HD 4570)
- M93 (Mobility Radeon M93)
- M96 (Mobility Radeon HD 4600)
- M97 (Mobility Radeon HD 4860)
- M98 (Mobility Radeon HD 4850, HD 4870)

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
- RV620 (Radeon HD 3450, HD 3470)
- RV630 (Radeon HD 2600 LE/Pro/XT, HD 2600 Pro/XT AGP; Gemini RV630; FireGL V3600/V5600)
- RV635 (Radeon HD 3650, HD 3670)
- RV670 (Radeon HD 3690, HD 3850, HD 3870; FireGL V7700; FireStream 9170)
- R680 (Radeon HD 3870 X2)
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
- M82 (Mobility Radeon HD 3400)
- M86 (Mobility Radeon HD 3650, HD 3670; Mobility FireGL V5700)
- M88 (Mobility Radeon HD 3850, HD 3850 X2, HD 3870, HD 3870 X2)
- RS600 (Radeon Xpress 1200, Xpress 1250)
- RS690 (Radeon X1200, X1250, X1270)
- RS740 (RS740, RS740M)
- RS780 (Radeon HD 3100/3200/3300)
- R700 (Radeon R700)
- RV710 (Radeon HD 4570, HD 4350)
- RV730 (Radeon HD 4670, HD 4650)
- RV470 (Radeon HD 4770)
- RV770 (Radeon HD 4800; Everest, K2, Denali ATI FirePro)
- RV790 (Radeon HD 4890)
- M92 (Mobility Radeon HD 4330, HD 4530, HD 4570)
- M93 (Mobility Radeon M93)
- M96 (Mobility Radeon HD 4600)
- M97 (Mobility Radeon HD 4860)
- M98 (Mobility Radeon HD 4850, HD 4870)

%prep
%setup -q -n xf86-video-radeonhd-%{version}

%ifarch %{ix86} %{x8664}
ln utils/conntest/README README.conntest
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

# V=1 because of shave
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README README.conntest
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/radeonhd_drv.so
%{_mandir}/man4/radeonhd.4*
