Summary:	fatattr - display or change attributes on a FAT filesystem
Summary(pl.UTF-8):	fatattr - odczyt i zmiana atrybutów na systemie plików FAT
Name:		fatattr
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/fs/fat/fatattr/%{name}-%{version}.tar.bz2
# Source0-md5:	efd7edaf48f2dfb56ef5db02a54e577a
BuildRequires:	linux-libc-headers >= 7:2.6.11
Requires:	uname(release) >= 2.6.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fatattr displays or changes attributes on an MS-DOS FAT filesystem.

%description -l pl.UTF-8
fatattr odczytuje i zmienia atrybuty plików i katalogów na systemie
plików FAT znanym z MS-DOS-a.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALLROOT=$RPM_BUILD_ROOT \
	MAN1PAGES=fatattr.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fatattr
%{_mandir}/man1/fatattr.1*
