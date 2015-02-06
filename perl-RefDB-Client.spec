%define module	RefDB-Client

Name:		perl-%{module}
Version:	1.18
Release:	5
Summary:	%{module} module for perl
License:	GPLv2+
Group:		Development/Perl
URL:		http://refdb.sourceforge.net
Source:		http://prdownloads.sourceforge.net/refdb/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl component for the MARC and Pubmed import filters.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
# tests requires a refdb base
#make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/RefDB
%{_mandir}/*/*



%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.18-2mdv2010.0
+ Revision: 440618
- rebuild

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2009.1
+ Revision: 354977
- import perl-RefDB-Client


* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2009.1
- initial release  
