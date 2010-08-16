Summary:	D-Bus service providing high-level OBEX client and server side functionality
Summary(pl.UTF-8):	Usługa D-Bus dostarczająca wysokopoziomową funkcjonalność klientą i serwera OBEX
Name:		obexd
Version:	0.29
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
# Source0-md5:	d6e4884e7ab11b1f048ba32bc963fa80
URL:		http://www.bluez.org/
BuildRequires:	GConf2-devel >= 2.6
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 4.2
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libical-devel
BuildRequires:	openobex-devel >= 1.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,preun):	GConf2 >= 2.6
Requires:	dbus-glib >= 0.60
Provides:	dbus(org.openobex.client)
Obsoletes:	obex-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obexd is D-Bus service providing high-level OBEX client and server
side functionality.

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-bip=gdk-pixbuf \
	--enable-shared \
	--enable-usb \
	--enable-nokia-backup \
	--enable-debug \
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
