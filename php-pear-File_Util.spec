%define	_class	File
%define	modname	%{_class}_Util

Summary:	Common file and directory utility functions
Name:		php-pear-%{modname}
Version:	1.0.0
Release:	13
License:	PHP License
Group:		Development/PHP
Url:		https://pear.php.net/package/File_Util/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Conflicts:	php-pear-File < 1.4.0

%description
Common file and directory utility functions. Path handling, temp dir/file,
sorting of files, listDirs, isIncludable and more.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}/Util.php
%{_datadir}/pear/packages/%{modname}.xml

