Name:		pciutils
Version:	2.1.8
Release: 8
Source:		ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Patch: 		pciutils-werror.patch
Patch2:		pciutils-bufsiz.patch
Patch3:		pciutils-ids.patch
Patch4:		pciutils-qlogic.patch
Patch5:		pciutils-pcix.patch
Patch6:		pciutils-ids-2.patch
Patch7:         pciutils-i815.patch
Patch8:         pciutils-ati.patch
Patch9:         pciutils-vortex.patch
License:	GPL
Buildroot: 	%{_tmppath}/%{name}-%{version}-root
ExclusiveOS: 	Linux
ExcludeArch:	armv4l
Requires:	kernel >= 2.2
Summary: Linux PCI utilities.
Group: Applications/System

%description
This package contains various utilities for inspecting and setting
devices connected to the PCI bus. The utilities provided require
kernel version 2.1.82 or newer (supporting the /proc/bus/pci
interface).

%package devel
Summary: Linux PCI development library.
Group: Development/Libraries

%description devel
This package contains a library for inspecting and setting
devices connected to the PCI bus.

%prep
%setup -q
%patch -p1 -b .werror
%patch2 -p1 -b .bufsiz
%patch3 -p1
%patch4 -p1 
%patch5 -p1 -b .pcix
%patch6 -p1
%patch7 -p1 
%patch8 -p1
%patch9 -p1 -b .vortex

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,%{_mandir}/man8,/usr/share,/usr/lib,/usr/include/pci}

install -s lspci setpci $RPM_BUILD_ROOT/sbin
install lspci.8 setpci.8 $RPM_BUILD_ROOT%{_mandir}/man8
install pci.ids $RPM_BUILD_ROOT/usr/share
install lib/libpci.a $RPM_BUILD_ROOT/usr/lib
install lib/pci.h $RPM_BUILD_ROOT/usr/include/pci
install lib/header.h $RPM_BUILD_ROOT/usr/include/pci
install lib/config.h $RPM_BUILD_ROOT/usr/include/pci

%files
%defattr(0644, root, root, 0755)
%attr(0644, root, man) %{_mandir}/man8/*
%attr(0755, root, root) /sbin/*
%config /usr/share/pci.ids
%doc README ChangeLog pciutils.lsm

%files devel
%defattr(0644, root, root)
/usr/lib/libpci.a
/usr/include/pci/*.h

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jul 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- clean up patches to not generate badly-formatted files

* Tue Jul 25 2000 Preston Brown <pbrown@redhat.com>
- Vortex fixes laroche originally applied on kudzu moved here.

* Fri Jul 14 2000 Preston Brown <pbrown@redhat.com>
- pci ids for i815, new ati hardware

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul 11 2000 Bill Nottingham <notting@redhat.com>
- yet more IDs
- PCI-X support from Matt Domsch

* Fri Jul  7 2000 Bill Nottingham <notting@redhat.com>
- some more QLogic ids

* Mon Jun 26 2000 Bill Nottingham <notting@redhat.com>
- more IDs from Dell

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.8

* Fri Apr 21 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.7

* Mon Apr 17 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.6

* Fri Mar  3 2000 Bill Nottingham <notting@redhat.com>
- add a couple of ids

* Mon Feb 14 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.5

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Mon Jan 24 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.4

* Thu Jan 20 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.3

* Fri Dec 24 1999 Bill Nottingham <notting@redhat.com>
- update to 2.1.2

* Tue Jun 29 1999 Bill Nottingham <notting@redhat.com>
- add -devel package

* Thu May 20 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0

* Mon Apr 19 1999 Jakub Jelinek  <jj@ultra.linux.cz>
- update to 1.99.5
- fix sparc64 operation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Feb  4 1999 Bill Nottingham <notting@redhat.com>
- initial build
