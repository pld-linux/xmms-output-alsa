
%define		_realname	alsa-xmms

Summary:	ALSA 0.9.x output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS odtwarzaj�ca przez ALSA 0.9.x
Name:		xmms-output-alsa
Version:	0.9.12
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/%{_realname}/%{_realname}-%{version}.tar.gz
# Source0-md5:	3b16eb619b48d8bb878e626f9091ec75
URL:		http://savannah.nongnu.org/download/alsa-xmms/
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows xmms to play sounds though final ALSA drivers
(versions 0.9 and above).

%description -l pl
Ta wtyczka pozwala programowi xmms odtwarza� muzyk� za pomoc�
sterownik�w ALSA (wersje 0.9 i nowsze).

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root) %{xmms_output_plugindir}/*
