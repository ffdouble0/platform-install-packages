%define prefix /opt/kaltura
%define widget_name kupload
Name:	kaltura-%{widget_name}
Version: v1.2.16 
Release: 2
Epoch:1
Summary: Kaltura kupload widget
License: AGPLv3+	
URL: http://kaltura.org
Source0: %{name}-%{version}.zip
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

Requires: kaltura-base, httpd	

%description
Kaltura is the world's first Open Source Online Video Platform, transforming the way people work, 
learn, and entertain using online video. 
The Kaltura platform empowers media applications with advanced video management, publishing, 
and monetization tools that increase their reach and monetization and simplify their video operations. 
Kaltura improves productivity and interaction among millions of employees by providing enterprises 
powerful online video tools for boosting internal knowledge sharing, training, and collaboration, 
and for more effective marketing. Kaltura offers next generation learning for millions of students and 
teachers by providing educational institutions disruptive online video solutions for improved teaching,
learning, and increased engagement across campuses and beyond. 
For more information visit: http://corp.kaltura.com, http://www.kaltura.org and http://www.html5video.org.

This package installs the Kaltura kupload.

%prep
%setup -qn %{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/web/flash/%{widget_name}
mkdir -p $RPM_BUILD_ROOT%{prefix}/web/content
cp -r %{_builddir}/%{version} $RPM_BUILD_ROOT/%{prefix}/web/flash/%{widget_name}
find $RPM_BUILD_ROOT/%{prefix}/web/flash/%{widget_name} -name ".project" -exec rm {} \;

%post
if [ "$1" = 2 ];then
	if [ -r /etc/kaltura.d/system.ini ];then
		. /etc/kaltura.d/system.ini
		echo 'update ui_conf set swf_url = "/flash/kupload/%{version}/KUpload.swf" where swf_url like "/flash/kupload/v%/KUpload.swf"'|mysql -h$DB1_HOST -u $SUPER_USER -p$SUPER_USER_PASSWD -P$DB1_PORT $DB1_NAME
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{prefix}/web/flash/%{widget_name}

%changelog
* Thu Oct 20 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v1.2.16-2
- Auto upgrade ui_conf.swf_url during %post

* Mon Nov 17 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v1.2.16-1
- Bounce ver and also moved to GitHub.

* Tue Feb 11 2014 Jess Portnoy <jess.portnoy@kaltura.com> - 1.0.0-1
- initial package.
