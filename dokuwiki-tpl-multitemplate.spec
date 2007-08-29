%define		_snap	01022007
%define		_ver	%(echo %{_snap} | sed -e 's,\\(..\\)\\(..\\)\\(....\\),\\3\\1\\2,')
Summary:	Multitemplate for DokuWiki
Name:		dokuwiki-tpl-multitemplate
Version:	%{_ver}
Release:	0.3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://tatewake.com/wiki/_media/projects:multitemplate-%{_snap}.zip
# Source0-md5:	b1d36f8b69439c8e0c67703fa0425238
URL:		http://tatewake.com/wiki/projects:multitemplate_for_dokuwiki
Requires:	dokuwiki
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_tpldir		%{_dokudir}/lib/tpl/%{_tpl}
%define		_tpl		multitemplate

%description
This template allows you to use any templates you wish for any
namespace (or page) you wish.

%prep
%setup -q -n %{_tpl}

cat > INSTALL <<'EOF'
To activate this template add something like this to your conf/local.php file: 

$multitemplate['playground'] = 'default';
$multitemplate[''] = 'monobook';

and
$conf['template'] = 'multitemplate';

EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_tpldir}
cp -a . $RPM_BUILD_ROOT%{_tpldir}
rm -f $RPM_BUILD_ROOT%{_tpldir}/INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL
%{_tpldir}
