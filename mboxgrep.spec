Summary:	Grep for mailboxes
Summary(pl):	grep dla skrzynek pocztowych
Name:		mboxgrep
Version:	0.7.8
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/mboxgrep/%{name}-%{version}.tar.gz
# Source0-md5:	efb1137bd408558f00a8641e268af6b0
URL:   		http://www.mboxgrep.org/
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mboxgrep is a small utility that scans a mailbox for messages matching
a basic, extended, or Perl-compatible regular expression. Found
messages can be either displayed on standard output, counted or
written to another mailbox. It supports mbox, MH, nnmh, nnml and
Maildir folders.

%description -l pl
mboxgrep to niewielkie narzêdzie szukaj±ce w skrzynce pocztowej
wiadomo¶ci pasuj±cych do podstawowego, rozszerzonego lub perlowego
wyra¿enia regularnego. Znalezione wiadomo¶ci mog± byæ wy¶wietlane na
standardowym wyj¶ciu, liczone lub zapisywane do innej skrzynki.
mboxgrep obs³uguje skrzynki mbox, MH, nnmh, nnml oraz foldery Maildir.

%prep
%setup -q -n %{name}

%build
%configure
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}

install	src/mboxgrep $RPM_BUILD_ROOT%{_bindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*
%{_mandir}/*/*
