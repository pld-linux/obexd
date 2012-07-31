Summary:	D-Bus service providing high-level OBEX client and server side functionality
Summary(pl.UTF-8):	Usługa D-Bus dostarczająca wysokopoziomową funkcjonalność klienta i serwera OBEX
Name:		obexd
Version:	0.47
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
# Source0-md5:	8f5810e39403b0825abbce3527eea077
URL:		http://www.bluez.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	dbus-devel >= 1.4
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	libical-devel
BuildRequires:	libtool
BuildRequires:	openobex-devel >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	bluez-libs >= 4.99
Requires:	dbus >= 1.4
Requires:	glib2 >= 1:2.28
Provides:	dbus(org.openobex.client)
Provides:	obex-data-server = %{version}
Obsoletes:	obex-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obexd is D-Bus service providing high-level OBEX client and server
side functionality.

%description -l pl.UTF-8
obexd to usługa D-Bus dostarczająca wysokopoziomową funkcjonalność
klienta i serwera OBEX.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--enable-pcsuite \
	--enable-usb \
	--with-gnu-ld
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/obexd
%attr(755,root,root) %{_libdir}/obex-client
%{_datadir}/dbus-1/services/obexd.service
%{_datadir}/dbus-1/services/obex-client.service
