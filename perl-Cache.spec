%define	upstream_name	 Cache
%define upstream_version 2.09

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(warnings::register\\)'
%else
%define	_requires_exceptions perl(warnings::register)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	The Cache interface
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Cache/Cache-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.40.0-2mdv2011.0
+ Revision: 680708
- mass rebuild

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.40.0-1mdv2011.0
+ Revision: 409015
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.04-7mdv2009.0
+ Revision: 241153
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-5mdv2008.0
+ Revision: 85921
- rebuild


* Sat Apr 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-4mdk
- spec cleanup
- better summary
- better buildrequires syntax
- better source URL
- buildrequires perl(Diget::SHA1)

* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.04-3mdk
- Fix BuildRequires

* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.04-2mdk
- Fix BuildRequires

* Fri Feb 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.04-1mdk
- 2.04
- enable tests
- fix URL
- BuildRequires

* Fri Jan 06 2006 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 2.03-1mdk
- initial Mandriva release



