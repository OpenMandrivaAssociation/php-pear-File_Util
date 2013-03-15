%define		_class		File
%define		upstream_name	%{_class}_Util

Summary:	Common file and directory utility functions
Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	4
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/File_Util/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
Conflicts:	php-pear-File < 1.4.0

%description
Common file and directory utility functions. Path handling, temp dir/file,
sorting of files, listDirs, isIncludable and more.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}/Util.php
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2011.0
+ Revision: 667499
- mass rebuild

* Tue Apr 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1
+ Revision: 650599
- import php-pear-File_Util


* Tue Apr 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2010.2
- initial Mandriva package
