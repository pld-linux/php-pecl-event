%define		php_name	php%{?php_suffix}
%define		modname	event
%define		status		beta
Summary:	%{modname} - event scheduling engine
Summary(pl.UTF-8):	%{modname} - silnik do planowania zdarzeń
Name:		%{php_name}-pecl-%{modname}
Version:	0.9.1
Release:	8
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	f009fd3519c14a027a8c85414208b61c
URL:		http://pecl.php.net/package/event/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension to efficiently schedule IO, time and signal based
events using the best available IO notification mechanism for your
system.

This is a port of libevent to the PHP infrastructure; the API is
similar but not identical.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
To rozszerzenie pozwala na efektywne planowanie We/Wy, czasu oraz
opartych na sygnałach zdarzeń za pomocą najlepszego dostępnego dla
systemu mechanizmu powiadamiania.

Jest to port biblioteki libevent do infrastruktury PHP; API jest
podobne, jednak nie identyczne.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS EXPERIMENTAL
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
