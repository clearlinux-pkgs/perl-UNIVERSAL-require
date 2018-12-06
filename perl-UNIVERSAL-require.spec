#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-UNIVERSAL-require
Version  : 0.18
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/UNIVERSAL-require-0.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/UNIVERSAL-require-0.18.tar.gz
Summary  : 'require() modules from a variable'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
This module lets you require other modules where the module
name is in a variable, something you can't do with the 'require' built-in.

%package dev
Summary: dev components for the perl-UNIVERSAL-require package.
Group: Development
Provides: perl-UNIVERSAL-require-devel = %{version}-%{release}

%description dev
dev components for the perl-UNIVERSAL-require package.


%prep
%setup -q -n UNIVERSAL-require-0.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/UNIVERSAL/require.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/UNIVERSAL::require.3
