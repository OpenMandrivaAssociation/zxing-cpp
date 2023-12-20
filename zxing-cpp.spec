%define major 2
%define oldlibname %mklibname ZXing 1
%define libname %mklibname ZXing
%define devname %mklibname ZXing -d

Summary:	ZXing-C++ is a multi-format linear/matrix barcode image processing library implemented in C++.
Name:		zxing-cpp
Version:	2.2.1
Release:	1
Group:		System/Libraries
License:	Apache-2.0
Url:		https://github.com/zxing-cpp/zxing-cpp
Source0:	https://github.com/zxing-cpp/zxing-cpp/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  git
Requires:	%{libname} = %{EVRD}

%description
ZXing-C++ ("zebra crossing") is an open-source, multi-format linear/matrix
barcode image processing library implemented in C++.

It was originally ported from the Java ZXing Library but has been developed
further and now includes many improvements in terms of runtime and detection
performance. It can both read and write barcodes in a number of formats.

%files
%{_bindir}/ZXing{Reader,Writer}

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
ZXing-C++ ("zebra crossing") is an open-source, multi-format linear/matrix
barcode image processing library implemented in C++.

It was originally ported from the Java ZXing Library but has been developed
further and now includes many improvements in terms of runtime and detection
performance. It can both read and write barcodes in a number of formats.


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
%cmake -DCMAKE_CXX_STANDARD=20 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
