Summary:	ALSA 0.9.x output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS odtwarzaj±ca przez ALSA 0.9.x
Name:		xmms-output-alsa
Version:	0.9
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	alsa-xmms-%{version}.tar.gz
Requires:	xmms
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
This plugin allows xmms to play sounds though final ALSA drivers
(versions 0.9 and above).

%description -l pl
Ta wtyczka pozwala xmms'owi odtwarzaæ muzykê poprzez finalne
sterowniki ALSA (wersje 0.9 i nowsze).

%prep
%setup -q -n alsa-xmms-%{version}

%build
aclocal
automake -a -c -f
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip README NEWS AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/Output/*
