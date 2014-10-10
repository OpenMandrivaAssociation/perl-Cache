%define	upstream_name	 Cache
%define upstream_version 2.10

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(warnings::register\\)'
%else
%define	_requires_exceptions perl(warnings::register)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	The Cache interface

License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Module::Build)
BuildRequires:	perl(File::NFSLock)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Heap)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Digest::SHA1)
BuildArch:	noarch

%description
%{upstream_name} perl module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README TODO
%{perl_vendorlib}/Cache*
%{_mandir}/man3/*



