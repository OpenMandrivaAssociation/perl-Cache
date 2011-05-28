%define	upstream_name	 Cache
%define	upstream_version 2.04

%define	_requires_exceptions	perl(warnings::register)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	The Cache interface
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.bz2

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
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} perl module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
