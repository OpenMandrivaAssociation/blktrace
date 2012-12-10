%define name blktrace
%define version 0.99.2
%define git 20070730
%define release %mkrel 1.%{git}
%define distname %{name}-%{version}-%{git}

Summary: Utilities for block layer IO tracing
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://git.kernel.org/?p=linux/kernel/git/axboe/blktrace.git;a=summary
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space. This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

You should install the blktrace package if you need to gather detailed
information about IO patterns.

%prep
%setup -q -n %{distname}

%build
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/blkparse
%{_bindir}/blkrawverify
%{_bindir}/blktrace
%{_bindir}/btrace
%{_bindir}/btt
%{_bindir}/verify_blkparse
%{_mandir}/man1/blkparse.1*
%{_mandir}/man1/blkrawverify.1*
%{_mandir}/man1/btt.1*
%{_mandir}/man1/verify_blkparse.1*
%{_mandir}/man8/blktrace.8*
%{_mandir}/man8/btrace.8*


%changelog
* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.99.2-1.20070730mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 12 2007 Olivier Blin <oblin@mandriva.com> 0.99.2-1.20070730mdv2008.0
+ Revision: 62377
- initial package
- Create blktrace

