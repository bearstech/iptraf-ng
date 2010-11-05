Summary:        A console-based network monitoring utility
Name:           iptraf-ng
Version:        1.0.4
Release:        1%{?dist}
Source0:        https://fedorahosted.org/releases/i/p/iptraf-ng/%{name}-%{version}.tar.gz
Source1:        iptraf-ng-logrotate.conf
URL:            https://fedorahosted.org/iptraf-ng/
License:        GPLv2+
Group:          Applications/System
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ncurses-devel
Obsoletes:	iptraf
Provides:	iptraf-ng

%description
IPTraf-ng is a console-based network monitoring utility.  IPTraf gathers
data like TCP connection packet and byte counts, interface statistics
and activity indicators, TCP/UDP traffic breakdowns, and LAN station
packet and byte counts.  IPTraf-ng features include an IP traffic monitor
which shows TCP flag information, packet and byte counts, ICMP
details, OSPF packet types, and oversized IP packet warnings;
interface statistics showing IP, TCP, UDP, ICMP, non-IP and other IP
packet counts, IP checksum errors, interface activity and packet size
counts; a TCP and UDP service monitor showing counts of incoming and
outgoing packets for common TCP and UDP application ports, a LAN
statistics module that discovers active hosts and displays statistics
about their activity; TCP, UDP and other protocol display filters so
you can view just the traffic you want; logging; support for Ethernet,
FDDI, ISDN, SLIP, PPP, and loopback interfaces; and utilization of the
built-in raw socket interface of the Linux kernel, so it can be used
on a wide variety of supported network cards.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# remove everything besides the html and pictures in Documentation
find Documentation -type f | grep -v '\.html$\|\.png$\|/stylesheet' | \
	xargs rm -f

install -D -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/iptraf

install -d -m 0755 $RPM_BUILD_ROOT%{_localstatedir}/{lock,log,lib}/iptraf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES FAQ LICENSE INSTALL README* RELEASE-NOTES
%doc Documentation
%{_bindir}/iptraf
%{_bindir}/rawtime
%{_bindir}/rvnamed
%{_mandir}/man8/iptraf.8*
%{_mandir}/man8/rvnamed.8*
%{_localstatedir}/lock/iptraf
%{_localstatedir}/log/iptraf
%{_localstatedir}/lib/iptraf
%config(noreplace) %{_sysconfdir}/logrotate.d/iptraf

%changelog
* Thu Apr 8 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 1.0.2-3
- Still Package Review fixing rhbz#576591

* Mon Apr 3 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 1.0.2-2
- Fix many issues according to rhbz#576591

* Mon Jan 4 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 1.0.2-1
- Initialization build
