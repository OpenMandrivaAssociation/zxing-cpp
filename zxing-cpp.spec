%define major 0
%define libname %mklibname ZXingCore %{major}
%define devname %mklibname ZXingCore -d

Summary:	C++ port of the ZXing ("Zebra Crossing") barcode scanning library
Name:		zxing-cpp
Version:	1.0.7
Release:	1
Group:		System/Libraries
License:	LGPLv2.1+
Url:		https://github.com/nu-book/zxing-cpp
Source0:	https://github.com/nu-book/zxing-cpp/archive/master.tar.gz
Patch0:		zxing-cpp-20181126-linuxify.patch
BuildRequires:	cmake ninja

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
%{_libdir}/libZXingCore.so.%{major}*

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

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-master

%build
cd core
%cmake -DENABLE_ENCODERS:BOOL=ON -G Ninja
%ninja_build

%install
cd core
%ninja_install -C build
