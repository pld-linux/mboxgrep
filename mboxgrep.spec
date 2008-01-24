Summary:	Grep for mailboxes
Summary(pl.UTF-8):	grep dla skrzynek pocztowych
Name:		mboxgrep
Version:	0.7.9
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/mboxgrep/%{name}-%{version}.tar.gz
# Source0-md5:	4b256de164b8f094db9ccf0e6386d246
URL:		http://www.mboxgrep.org/
BuildRequires:	bzip2-devel
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mboxgrep is a small utility that scans a mailbox for messages matching
a basic, extended, or Perl-compatible regular expression. Found
messages can be either displayed on standard output, counted or
written to another mailbox. It supports mbox, MH, nnmh, nnml and
Maildir folders.

%description -l pl.UTF-8
mboxgrep to niewielkie narzędzie szukające w skrzynce pocztowej
wiadomości pasujących do podstawowego, rozszerzonego lub perlowego
wyrażenia regularnego. Znalezione wiadomości mogą być wyświetlane na
standardowym wyjściu, liczone lub zapisywane do innej skrzynki.
mboxgrep obsługuje skrzynki mbox, MH, nnmh, nnml oraz foldery Maildir.

%prep
%setup -q

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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/*/*
