%define		documentid	46528
Summary:	Another tool for converting SVN repository to CVS repository
Name:		s2c
Version:	1.6
Release:	0.1
License:	BSD
Group:		Development/Version Control
Source0:	http://s2c.googlecode.com/files/svn2cvs-%{version}.gz
# Source0-md5:	9341587be3da321b7a4b0a7b8bc7c2c2
URL:		https://code.google.com/p/s2c/
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Another tool for converting SVN repository to CVS repository

The converting process is resumable. You can interrupt the converting
at any point, and resume it later.

%prep
%setup -qcT
gzip -dc %{SOURCE0} > %{name}
touch -r %{SOURCE0} %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/s2c
