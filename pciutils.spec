Name:		pciutils
Version:	2.1.8
Release: 23
Source:		ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Patch0:		pciutils-werror.patch
Patch1:		pciutils-pci.ids-update.patch
Patch2:		pciutils-bufsiz.patch
Patch4:		pciutils-qlogic.patch
Patch5:		pciutils-pcix.patch
Patch6:		pciutils-ids-2.patch
Patch7:         pciutils-i815.patch
Patch8:         pciutils-ati.patch
Patch9:         pciutils-vortex.patch
Patch10:	pciutils-megaraid.patch
Patch11:	pciutils-2.4.0.diffs
Patch12:	pciutils-broadcom.patch
Patch13:	pciutils-various.ids.patch
Patch14:        pciutils-i860.patch
Patch15:        pciutils-serveraid.patch
Patch16:	pciutils-lsi.patch
Patch17:	pciutils-2.1.8-moremega.patch
Patch18:	pciutils-2.1.8-e1000.patch
Patch19:	pciutils-2.1.8-2.4.6.patch
Patch20:	pciutils-i845.patch
Patch21:	pciutils-2.1.8-2.4.7.patch
License:	GPL
Buildroot: 	%{_tmppath}/%{name}-%{version}-root
ExclusiveOS: 	Linux
ExcludeArch:	armv4l
Requires:	kernel >= 2.2
Summary: PCI bus related utilities.
Group: Applications/System

%description
The pciutils package contains various utilities for inspecting and
setting devices connected to the PCI bus. The utilities provided
require kernel version 2.1.82 or newer (which support the
/proc/bus/pci interface).

%package devel
Summary: Linux PCI development library.
Group: Development/Libraries

%description devel
This package contains a library for inspecting and setting
devices connected to the PCI bus.

%prep
%setup -q
%patch0 -p1 -b .werror
%patch1 -p1 -b .update
%patch2 -p1 -b .bufsiz
%patch4 -p1 -b .qlogicids
%patch5 -p1 -b .pcix
%patch6 -p1 -b .yetmoreids
%patch7 -p1 -b .i815-ids
%patch8 -p1 -b .ati-ids
%patch9 -p1 -b .vortex
%patch10 -p1 -b .megaraid
%patch11 -p0 -b 2.4
%patch12 -p1 -b .broadcom
%patch13 -p1 -b .various
%patch14 -p1 -b .i860
%patch15 -p1 -b .serveraid
%patch16 -p1 -b .lsi
%patch17 -p1 -b .moremega
%patch18 -p1 -b .e1000
%patch19 -p1 -b .2.4.6
%patch20 -p1 -b .i845
%patch21 -p0 -b .2.4.7

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
* Fri Aug 10 2001 Bill Nottingham <notting@redhat.com>
- more ids

* Tue Jul 17 2001 Bill Nottingham <notting@redhat.com>
- add newline in printf in PCI-X patch (#49277)

* Mon Jul  9 2001 Bill Nottingham <notting@redhat.com>
- update broadcom patch
- add new ids from 2.4.6

* Mon May 28 2001 Bill Nottingham <notting@redhat.com>
- add a couple of e1000 ids

* Thu Mar 22 2001 Bill Nottingham <notting@redhat.com>
- another megaraid id

* Wed Mar 21 2001 Bill Nottingham <notting@redhat.com>
- another megaraid id

* Wed Mar 14 2001 Preston Brown <pbrown@redhat.com>
- LSI SCSI PCI id

* Wed Feb 21 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix formatting problems

* Wed Feb 21 2001 Preston Brown <pbrown@redhat.com>
- add IBM ServeRAID entries

* Tue Feb 20 2001 Preston Brown <pbrown@redhat.com>
- i860 entries.

* Mon Feb 19 2001 Helge Deller <hdeller@redhat.de>
- added various pci ids 

* Fri Feb  2 2001 Bill Nottingham <notting@redhat.com>
- fix mishap in fixing mishap

* Thu Feb  1 2001 Bill Nottingham <notting@redhat.com>
- fix apparent mishap in pci.ids update from kernel (#25520)

* Tue Jan 23 2001 Bill Nottingham <notting@redhat.com>
- pci.ids updates

* Tue Dec 12 2000 Bill Nottingham <notting@redhat.com>
- big pile of pci.ids updates

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
