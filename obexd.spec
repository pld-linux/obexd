Summary:	D-Bus service providing high-level OBEX client and server side functionality
Summary(pl.UTF-8):	Usługa D-Bus dostarczająca wysokopoziomową funkcjonalność klienta i serwera OBEX
Name:		obexd
Version:	0.37
Release:	1
License:	GPL v2+
Group:		Applications/Communication
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.bz2
# Source0-md5:	3126eced7f9d36aa52c3684bb31421e8
URL:		http://www.bluez.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 4.2
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	libical-devel
BuildRequires:	libtool
BuildRequires:	openobex-devel >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires:	dbus >= 1.0
Requires:	glib2 >= 1:2.16
Provides:	dbus(org.openobex.client)
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
	--enable-usb \
	--enable-nokia-backup \
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
