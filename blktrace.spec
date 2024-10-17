Summary: Utilities for block layer IO tracing
Name: blktrace
Version:	1.3.0
Release:	1
Source0: http://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: https://git.kernel.org/?p=linux/kernel/git/axboe/blktrace.git;a=summary
BuildRequires: libaio-devel
BuildRequires: make

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space. This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

You should install the blktrace package if you need to gather detailed
information about IO patterns.

%prep
%autosetup -p1

%build
%make_build prefix=%{_prefix} mandir=%{_mandir}

%install
%make_install prefix=%{_prefix} mandir=%{_mandir}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
