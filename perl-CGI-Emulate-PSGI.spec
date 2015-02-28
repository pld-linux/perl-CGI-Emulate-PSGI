#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	CGI
%define		pnam	Emulate-PSGI
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::Parse::PSGI - Parses CGI output and creates PSGI response out of it
Name:		perl-CGI-Emulate-PSGI
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a318c5fa2bcad36db83e575e86cf302
URL:		http://search.cpan.org/dist/CGI-Emulate-PSGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Message
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
use CGI::Parse::PSGI qw(parse_cgi_output);

my $output = YourApp->run; my $psgi_res = parse_cgi_output(\$output);

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/CGI/Emulate
%{perl_vendorlib}/CGI/Emulate/*.pm
%dir %{perl_vendorlib}/CGI/Parse
%{perl_vendorlib}/CGI/Parse/PSGI.pm
%{_mandir}/man3/*
