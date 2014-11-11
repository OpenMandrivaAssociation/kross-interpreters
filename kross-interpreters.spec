%bcond_with java 0
%bcond_with falcon 0
%bcond_with ruby 0

Name:		kross-interpreters
Summary:	KDE bindings to non-C++ languages
Version:	4.14.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		https://projects.kde.org/projects/kde/kdebindings/kross-interpreters
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	java-devel
%if %with ruby
BuildRequires:	ruby-devel
%endif
BuildRequires:	python-devel
BuildRequires:	qscintilla-qt4-devel
%if %with falcon
BuildRequires:	falcon-devel
%endif

%description
Language interpreters to enable in-process scripting with Kross.

#----------------------------------------------------------------

%package java
Summary:	Java kross interpreter

%description java
Java kross interpreter

%files java
%{_kde_libdir}/kde4/kross/kross.jar
%{_kde_libdir}/kde4/krossjava.so

#---------------------------------------------------------------

%package python
Summary:	Python kross-interpreter
Conflicts:	python-kde4 < 1:4.7.0

%description python
Python kross interpreter

%files python
%{_kde_libdir}/kde4/krosspython.so

#--------------------------------------------------------------
%if %with ruby
%package ruby
Summary:	Ruby kross interpreter
Conflicts:	ruby-kde4 < 1:4.7.0

%description ruby
Ruby kross interpreter

%files ruby
%{_kde_libdir}/kde4/krossruby.so
%endif

#------------------------------------------------------------

%if %with falcon
%package -n falcon-kde4
Summary:	Falcon KDE 4 bindings
Group:		Development/KDE and Qt
Requires:	falcon

%description -n falcon-kde4
Falcon KDE 4 bindings.

%files -n falcon-kde4
%{_kde_libdir}/kde4/krossfalcon.so
%endif

#------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Mon Jul 09 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Sat Jun 09 2012 Crispin Boylan <crisb@mandriva.org> 1:4.8.4-1
+ Revision: 803700
- New release

* Fri May 04 2012 Crispin Boylan <crisb@mandriva.org> 1:4.8.3-1
+ Revision: 796231
- New release

* Fri Apr 20 2012 Crispin Boylan <crisb@mandriva.org> 1:4.8.2-1
+ Revision: 792409
- Disable ruby for now as it fails to build on ruby 1.9
- New release

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762480
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758067
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 744547
- New upstream tarball
- New upstream tarball $NEW_VERSION
- Import kross-interpreters
- Create folder

