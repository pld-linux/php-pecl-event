%define		_modname	event
%define		_status		beta

Summary:	%{_modname} - event scheduling engine
Summary(pl):	%{_modname} - silnik do planowania zdarzeñ
Name:		php-pecl-%{_modname}
Version:	0.9.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	f009fd3519c14a027a8c85414208b61c
URL:		http://pecl.php.net/package/event/
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This is an extension to efficiently schedule IO, time and signal based
events using the best available IO notification mechanism for your
system.

This is a port of libevent to the PHP infrastructure; the API is
similar but not identical.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie pozwala na efektywne planowanie We/Wy, czasu oraz
opartych na sygna³ach zdarzeñ za pomoc± najlepszego dostêpnego dla
systemu mechanizmu powiadamiania.

Jest to port biblioteki libevent do infrastruktury PHP; API jest
podobne, jednak nie identyczne.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
