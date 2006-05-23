%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	AT
%define		_status		alpha
%define		_pearname	Validate_AT

Summary:	%{_pearname} - Validation class for AT
Summary(pl):	%{_pearname} - Klasa sprawdzaj±ca poprawno¶æ dla Austrii
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7e3b9bec0e062dd4252a1101d18f8106
URL:		http://pear.php.net/package/Validate_AT/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for AT such as:
- SSN
- Postal Code

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa sprawdzaj±ca poprawno¶æ dla Austrii danych takich jak:
- numer ubezpieczenia (SSN)
- kod pocztowy

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/AT.php
%dir %{php_pear_dir}/data/Validate_AT
%{php_pear_dir}/data/Validate_AT/AT_postcodes.txt
