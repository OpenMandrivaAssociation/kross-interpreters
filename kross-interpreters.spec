%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%bcond_with python
%bcond_without java
%bcond_without ruby

Name:		kross-interpreters
Summary:	KDE bindings to non-C++ languages
Version:	23.08.4
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		https://projects.kde.org/projects/kde/kdebindings/kross-interpreters
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kross-23.08.0-ecm.patch
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(ECM)
BuildRequires:	java-devel
%if %with ruby
BuildRequires:	ruby-devel
%endif
%if %with python
BuildRequires:	python2-devel
%endif

%description
Language interpreters to enable in-process scripting with Kross.

#----------------------------------------------------------------

%package java
Summary:	Java kross interpreter

%description java
Java kross interpreter

# For the moment, Java isn't supported
#files java
#{_libdir}/kde4/kross/kross.jar
#{_libdir}/kde4/krossjava.so

#---------------------------------------------------------------

%if %with python
%package python
Summary:	Python kross-interpreter
Conflicts:	python-kde4 < 1:4.7.0

%description python
Python kross interpreter

%files python
%{_libdir}/qt5/plugins/krosspython.so
%endif

#--------------------------------------------------------------
%if %with ruby
%package ruby
Summary:	Ruby kross interpreter
Conflicts:	ruby-kde4 < 1:4.7.0

%description ruby
Ruby kross interpreter

%files ruby
%{_libdir}/qt5/plugins/krossruby.so
%endif

#------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DPYTHON_EXECUTABLE=%{__python}

%build
%ninja -C build

%install
%ninja_install -C build
