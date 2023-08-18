%define libname %mklibname KF6GlobalAccel
%define devname %mklibname KF6GlobalAccel -d
%define git 20230818

Name: kf6-kglobalaccel
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kglobalaccel/-/archive/master/kglobalaccel-master.tar.bz2#/kglobalaccel-%{git}.tar.bz2
Summary: Global desktop keyboard shortcuts
URL: https://invent.kde.org/frameworks/kglobalaccel
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
# Don't pull in plasma5
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Global desktop keyboard shortcuts

%package -n %{libname}
Summary: Global desktop keyboard shortcuts
Group: System/Libraries
Requires: %{name} = %{EVRD}
Requires: kglobalaccel-dbus-interfaces = %{EVRD}

%description -n %{libname}
Global desktop keyboard shortcuts

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Global desktop keyboard shortcuts

# This is split out so it can be shared with KF5.
# Once we drop KF5, this can be merged back into the
# main package.
%package -n kglobalaccel-dbus-interfaces
Summary: D-Bus interface files for kglobalaccel
Group: System/Libraries

%description -n kglobalaccel-dbus-interfaces
D-Bus interface files for kglobalaccel

%prep
%autosetup -p1 -n kglobalaccel-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kglobalaccel.*

%files -n kglobalaccel-dbus-interfaces
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KGlobalAccel.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.kglobalaccel.Component.xml

%files -n %{devname}
%{_includedir}/KF6/KGlobalAccel
%{_libdir}/cmake/KF6GlobalAccel
%{_qtdir}/mkspecs/modules/qt_KGlobalAccel.pri
%{_qtdir}/doc/KF6GlobalAccel.*

%files -n %{libname}
%{_libdir}/libKF6GlobalAccel.so*
