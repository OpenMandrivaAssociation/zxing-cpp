%define major 1
%define libname %mklibname ZXing %{major}
%define devname %mklibname ZXing -d

Summary:	C++ port of the ZXing ("Zebra Crossing") barcode scanning library
Name:		zxing-cpp
Version:	1.2.0
Release:	1
Group:		System/Libraries
License:	LGPLv2.1+
Url:		https://github.com/nu-book/zxing-cpp
Source0:	https://github.com/nu-book/zxing-cpp/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Quick)

%description
This project is a C++ port of ZXing Library.

Same as ZXing, following barcode are supported:
* 1D product: UPC-A UPC-E EAN-8 EAN-13
* 1D industrial: Code 39, Code 93, Code 128, Codabar,
  ITF, RSS-14, RSS-Expanded
* 2D: QR Code, Data Matrix, Aztec (beta), PDF 417 (beta)

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This project is a C++ port of ZXing Library.

Same as ZXing, following barcode are supported:
* 1D product: UPC-A UPC-E EAN-8 EAN-13
* 1D industrial: Code 39, Code 93, Code 128, Codabar,
  ITF, RSS-14, RSS-Expanded
* 2D: QR Code, Data Matrix, Aztec (beta), PDF 417 (beta)

%files -n %{libname}
%{_libdir}/libZXing.so.%{major}*

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
%cmake -DENABLE_ENCODERS:BOOL=ON -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
