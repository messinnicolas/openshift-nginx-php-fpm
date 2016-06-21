%global cartridgedir %{_libexecdir}/openshift/cartridges/nginx-php-fpm
%global frameworkdir %{_libexecdir}/openshift/cartridges/nginx-php-fpm

Name:          openshift-cartridge-nginx-php-fpm
Version:       0.0.0.9
Release:       1%{?dist}
Summary:       Php-fpm cartridge
Group:         Development/Languages
License:       ASL 2.0
URL:           https://getupcloud.com
Source0:       https://github.com/getupcloud/origin-server/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
BuildArch:     noarch
# php-5.4 scl
Requires:      php54-php-pdo
Requires:      php54-php-enchant
Requires:      php54-php
Requires:      php54-php-dba
Requires:      php54-php-xml
Requires:      php54-php-pspell
Requires:      php54-php-interbase
Requires:      php54-php-pecl-xdebug
Requires:      php54-php-pear
Requires:      php54-php-gd
Requires:      php54-php-snmp
Requires:      php54-php-imap
Requires:      php54-php-ldap
Requires:      php54-php-cli
Requires:      php54-php-devel
Requires:      php54-php-tidy
Requires:      php54-php-recode
Requires:      php54-php-odbc
Requires:      php54-php-intl
Requires:      php54-php-fpm
Requires:      php54-php-pecl-mongo
Requires:      php54-php-xmlrpc
Requires:      php54-php-soap
Requires:      php54-php-process
Requires:      php54-php-mbstring
Requires:      php54-php-mysqlnd
Requires:      php54-php-mcrypt
Requires:      php54-php-pecl-imagick
Requires:      php54-php-common
Requires:      php54-php-mssql
Requires:      php54-php-pgsql
Requires:      php54-php-bcmath

#Obsoletes: openshift-origin-cartridge-php-5.3

%description
PHP-FPM cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__mkdir -p %{buildroot}%{cartridgedir}/versions/shared/configuration/etc/conf/

%files
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md


%changelog
* Tue Jun 21 2016 Nicolas MESSIN <nicolas.messin@worldline.com> 0.0.0.9-1
- Add  variable in php_context file (nicolas.messin@worldline.com)

* Tue Jun 21 2016 Nicolas MESSIN <nicolas.messin@worldline.com> 0.0.0.8-1
- Update .spec file (nicolas.messin@worldline.com)

* Tue Jun 21 2016 Nicolas MESSIN <nicolas.messin@worldline.com> 0.0.0.7-1
- Up bin conf file (nicolas.messin@worldline.com)

* Tue Jun 21 2016 Nicolas MESSIN <nicolas.messin@worldline.com> 0.0.0.6-1
- First build PHP (nicolas.messin@worldline.com)

* Tue Jun 21 2016 Nicolas MESSIN <nicolas.messin@worldline.com> 0.0.0.5-1
- new package built with tito

* Tue Jun 21 2016 Nicolas MESSIN <nicolas.messin@worldline.com>
- new package built with tito

* Wed Nov 13 2013 Getup Builder <getup@getupcloud.com> 0.0.0.3-1
- new package built with tito

* Wed Nov 13 2013 Getup Builder <getup@getupcloud.com> 0.0.0.2-1
- new package built with tito

