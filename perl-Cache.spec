%define	module	Cache
%define	name	perl-%{module}
%define	version	2.04
%define	release	%mkrel 4
%define	_requires_exceptions	perl(warnings::register)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The Cache interface
License:	GPL
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Cache/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(File::NFSLock)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Heap)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Digest::SHA1)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
%{module} perl module

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README TODO
%{perl_vendorlib}/Cache*
%{_mandir}/man3/*

