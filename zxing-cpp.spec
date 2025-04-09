%define major 2
%define oldlibname %mklibname ZXing 1
%define libname %mklibname ZXing
%define devname %mklibname ZXing -d

Summary:	C++ port of the ZXing ("Zebra Crossing") barcode scanning library
Name:		zxing-cpp
Version:	2.3.0
Release:	2
Group:		System/Libraries
License:	LGPLv2.1+
Url:		https://github.com/nu-book/zxing-cpp
Source0:	https://github.com/nu-book/zxing-cpp/archive/v%{version}/%{name}-%{version}.tar.gz
# https://bugs.kde.org/show_bug.cgi?id=498240
Patch0:		fix-improper-use-of-ndebug.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  qmake5
#BuildRequires:  git
BuildRequires:	pkgconfig(opencv4)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(stb)
Requires:	%{libname} = %{EVRD}

%description
This project is a C++ port of ZXing Library.

Same as ZXing, following barcode are supported:
* 1D product: UPC-A UPC-E EAN-8 EAN-13
* 1D industrial: Code 39, Code 93, Code 128, Codabar,
  ITF, RSS-14, RSS-Expanded
* 2D: QR Code, Data Matrix, Aztec (beta), PDF 417 (beta)

%files
%{_bindir}/ZXing{Reader,Writer}

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
This project is a C++ port of ZXing Library.

Same as ZXing, following barcode are supported:
* 1D product: UPC-A UPC-E EAN-8 EAN-13
* 1D industrial: Code 39, Code 93, Code 128, Codabar,
  ITF, RSS-14, RSS-Expanded
* 2D: QR Code, Data Matrix, Aztec (beta), PDF 417 (beta)

%files -n %{libname}
%{_libdir}/libZXing.so.%{major}*
%{_libdir}/libZXing.so.3

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains the development files for %{name}.

%files -n %{devname}
%{_includedir}/ZXing
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake -Wno-dev \
	-DENABLE_ENCODERS:BOOL=ON \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
