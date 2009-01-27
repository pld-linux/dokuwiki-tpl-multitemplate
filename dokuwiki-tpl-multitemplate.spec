%define		snap	01022007
%define		ver	%(echo %{snap} | sed -e 's,\\(..\\)\\(..\\)\\(....\\),\\3\\1\\2,')
%define		tpl	multitemplate
Summary:	Multitemplate for DokuWiki
Summary(pl.UTF-8):	Wielokrotne szablony dla DokuWiki
Name:		dokuwiki-tpl-multitemplate
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://tatewake.com/wiki/_media/projects:multitemplate-%{snap}.zip
# Source0-md5:	b1d36f8b69439c8e0c67703fa0425238
URL:		http://tatewake.com/wiki/projects:multitemplate_for_dokuwiki
Requires:	dokuwiki
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		tpldir		%{dokudir}/lib/tpl/%{tpl}

%description
This template allows you to use any templates you wish for any
namespace (or page) you wish.

%description -l pl.UTF-8
Ten szablon pozwala na używanie dowolnie wybranych szablonów dla
dowolnej przestrzeni nazw (lub strony).

%prep
%setup -q -n %{tpl}

cat > INSTALL <<'EOF'
To activate this template add something like this to your conf/local.php file:

$conf['template'] = '%{tpl}';

and configure defaults:
$multitemplate['playground'] = 'default';
$multitemplate[''] = 'monobook';

EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tpldir}
cp -a . $RPM_BUILD_ROOT%{tpldir}
rm -f $RPM_BUILD_ROOT%{tpldir}/INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc INSTALL
%{tpldir}
