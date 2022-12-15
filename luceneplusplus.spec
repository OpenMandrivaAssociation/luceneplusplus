%ifarch %{ix86} %{arm}
%define _disable_ld_no_undefined 1
%define _disable_lto 1
%endif

%define oname LucenePlusPlus

%define major 0
%define libname %mklibname %{name} %{major}
%define libcontrib %mklibname %{name}-contrib %{major}
%define devname %mklibname %{name} -d

Summary:	C++ port of the popular Java Lucene library
Name:		lucene++
Version:	3.0.8
Release:	3
License:	LGPLv3+ and ASL2.0
Group:		Development/C++
Url:		https://github.com/luceneplusplus/LucenePlusPlus
Source0:	https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}/LucenePlusPlus-rel_%{version}.tar.gz
#Patch1:		LucenePlusPlus-20140729-pkgconfig.patch
Patch0:         lucene++-3.0.8-fix-contrib-soname.patch
Patch1:         lucene++-3.0.8-fix-pc-libdir.patch
Patch2:         lucene++-3.0.8-fix-cmake-issues.patch
Patch3:         lucene++-3.0.8-fix-missing-headers.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(bzip2)

%description
Lucene++ is an up to date C++ port of the popular Java Lucene library,
a high-performance, full-featured text search engine.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	C++ port of the popular Java Lucene library
Group:		System/Libraries

%description -n %{libname}
Lucene++ is an up to date C++ port of the popular Java Lucene library,
a high-performance, full-featured text search engine.

%files -n %{libname}
%doc *.license README* AUTHORS
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{version}

#----------------------------------------------------------------------------

%package -n %{libcontrib}
Summary:	C++ port of the popular Java Lucene library
Group:		System/Libraries

%description -n %{libcontrib}
Lucene++ is an up to date C++ port of the popular Java Lucene library,
a high-performance, full-featured text search engine.

%files -n %{libcontrib}
%doc *.license README* AUTHORS
%{_libdir}/lib%{name}-contrib.so.%{major}
%{_libdir}/lib%{name}-contrib.so.%{version}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files and headers for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{libcontrib} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the development ifles and headers for %{name}.

%files -n %{devname}
%doc *.license README* AUTHORS REQUESTS
%{_includedir}/%{name}/
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/liblucene++.pc
%{_libdir}/pkgconfig/liblucene++-contrib.pc
%{_libdir}/cmake/liblucene++/
%{_libdir}/cmake/liblucene++-contrib/

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-rel_%{version}
%autopatch -p1

%build
#ifarch %ix86
#export CC=gcc
#export CXX=g++
#endif

%cmake  \
        -DINSTALL_GTEST=OFF \
        -DENABLE_TEST=OFF
%make_build lucene++ lucene++-contrib

%install
%make_install -C build

