%{?scl:%scl_package perl-Inline-Files}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Inline-Files
Version:        0.68
Release:        9%{?dist}
Summary:        Allows for multiple inline files in a single perl file
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Inline-Files/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AM/AMBS/Inline/Inline-Files-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Tests only:
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(Filter::Util::Call)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test)
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(Data::Dumper)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
Inline::Files generalizes the notion of the `__DATA__' marker and the
associated `<DATA>' file handle, to an arbitrary number of markers and
associated file handles.

%prep
%setup -q -n Inline-Files-%{version}
chmod -R a-x demo/* README Changes lib/Inline/Files.pm \
    lib/Inline/Files/Virtual.pm

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README demo/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Nov 22 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.68-9
- Rebuilt for SCL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.68-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Petr Šabata <contyk@redhat.com> - 0.68-5
- Modernize the spec a bit
- Update the dep list
- Drop command macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.68-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Sabata <contyk@redhat.com> - 0.68-1
- 0.68 bump

* Mon Jul 18 2011 Petr Sabata <contyk@redhat.com> - 0.67-2
- Perl mass rebuild

* Mon Jul 11 2011 Petr Sabata <contyk@redhat.com> - 0.67-1
- 0.67 bump

* Mon Jun 20 2011 Petr Pisar <ppisar@redhat.com> - 0.65-1
- 0.65 bump
- Remove defattr
- Correct spelling in description

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.64-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 01 2011 Petr Pisar <ppisar@redhat.com> - 0.64-1
- 0.64 bump
- Remove BuildRoot stuff and empty lines
- Consolidate dependencies

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.63-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jul 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-1
- update to 0.63

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.62-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.62-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.62-3
- rebuild for new perl

* Wed Nov 14 2007 Robin Norwood <rnorwood@redhat.com> - 0.62-2
- Fix permissions per package review.

* Wed Oct 24 2007 Robin Norwood <rnorwood@redhat.com> - 0.62-1
- Initial build
