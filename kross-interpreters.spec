%bcond_with java 0
%bcond_with falcon 0

Name:kross-interpreters
Summary: KDE bindings to non-C++ languages
Version: 4.8.2
Release: 1
Epoch: 1
Group: Graphical desktop/KDE
License: LGPLv2
URL: https://projects.kde.org/projects/kde/kdebindings/kross-interpreters
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%version
BuildRequires: java-devel
BuildRequires: ruby-devel
BuildRequires: python-devel
BuildRequires: qscintilla-qt4-devel
%if %with falcon
BuildRequires: falcon-devel
%endif

%description
Language interpreters to enable in-process scripting with Kross.

#----------------------------------------------------------------

%package java
Summary: Java kross interpreter

%description java
Java kross interpreter

%files java
%_kde_libdir/kde4/kross/kross.jar
%_kde_libdir/kde4/krossjava.so

#---------------------------------------------------------------

%package python
Summary: Python kross-interpreter
Conflicts: python-kde4 < 1:4.7.0
%description python
Python kross interpreter

%files python
%_kde_libdir/kde4/krosspython.so

#--------------------------------------------------------------

%package ruby
Summary: Ruby kross interpreter
Conflicts: ruby-kde4 < 1:4.7.0
%description ruby
Ruby kross interpreter

%files ruby
%_kde_libdir/kde4/krossruby.so

#------------------------------------------------------------

%if %with falcon

%package -n falcon-kde4
Summary: Falcon KDE 4 bindings
Group: Development/KDE and Qt
Requires: falcon

%description -n falcon-kde4
Falcon KDE 4 bindings.

%files -n falcon-kde4
%_kde_libdir/kde4/krossfalcon.so

%endif

#------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

