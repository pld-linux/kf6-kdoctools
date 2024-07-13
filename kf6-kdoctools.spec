#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# - runtime Requires if any
# - package manual pages
%define		kdeframever	6.4
%define		qtver		5.15.2
%define		kfname		kdoctools

Summary:	Create documentation from DocBook
Name:		kf6-%{kfname}
Version:	6.4.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	33a84cb162ef66682d12614eae90008e
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-karchive-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel
BuildRequires:	ninja
BuildRequires:	perl-URI
BuildRequires:	perl-base
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qtver}
Requires:	docbook-style-xsl
Requires:	kf6-dirs
Requires:	kf6-karchive >= %{version}
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Provides tools to generate documentation in various format from
DocBook files.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qtver}
Requires:	cmake >= 3.16
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/checkXML6
%attr(755,root,root) %{_bindir}/meinproc6
%ghost %{_libdir}/libKF6DocTools.so.6
%attr(755,root,root) %{_libdir}/libKF6DocTools.so.*.*
%{_docdir}/HTML/*/kdoctools6-common
%dir %{_datadir}/kf6/kdoctools
%{_datadir}/kf6/kdoctools/customization
%{_mandir}/man1/checkXML6.1*
%{_mandir}/man1/meinproc6.1*
%{_mandir}/man7/kf6options.7*
%{_mandir}/man7/qt6options.7*
%{_mandir}/ca/man1/checkXML6.1*
%{_mandir}/ca/man1/meinproc6.1*
%{_mandir}/ca/man7/kf6options.7*
%{_mandir}/ca/man7/qt6options.7*
%{_mandir}/es/man1/checkXML6.1*
%{_mandir}/es/man1/meinproc6.1*
%{_mandir}/es/man7/qt6options.7*
%{_mandir}/it/man1/checkXML6.1*
%{_mandir}/it/man1/meinproc6.1*
%{_mandir}/it/man7/kf6options.7*
%{_mandir}/it/man7/qt6options.7*
%{_mandir}/nl/man1/checkXML6.1*
%{_mandir}/nl/man1/meinproc6.1*
%{_mandir}/nl/man7/kf6options.7*
%{_mandir}/nl/man7/qt6options.7*
%{_mandir}/tr/man1/checkXML6.1*
%{_mandir}/tr/man1/meinproc6.1*
%{_mandir}/tr/man7/kf6options.7*
%{_mandir}/tr/man7/qt6options.7*
%{_mandir}/uk/man1/checkXML6.1*
%{_mandir}/uk/man1/meinproc6.1*
%{_mandir}/uk/man7/kf6options.7*
%{_mandir}/uk/man7/qt6options.7*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KDocTools
%{_libdir}/cmake/KF6DocTools
%{_libdir}/libKF6DocTools.so
