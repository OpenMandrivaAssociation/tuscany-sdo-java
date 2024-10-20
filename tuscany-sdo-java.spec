%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global api_version 2.1
%global api_name tuscany-sdo-api-r%{api_version}

Name:          tuscany-sdo-java
Version:       1.1.1
Release:       8.0%{?dist}
Summary:       Service Data Objects 2.1 Java API spec
License:       ASL 2.0
Url:           https://tuscany.apache.org/sdo-java.html
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/tuscany/java/sdo/%{version}/apache-tuscany-sdo-%{version}-src.tar.gz

BuildRequires: java-devel

BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-assembly-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-provider-junit4

# required by plugin-bundle
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

BuildArch:     noarch

%description
SDO is a framework for data application development, which
includes an architecture and API. SDO does the following:

- Simplifies the J2EE data programming model
- Abstracts data in a service oriented architecture (SOA)
- Unifies data application development
- Supports and integrates XML
- Incorporates J2EE patterns and best practices

With SDO, you do not need to be familiar with a
technology-specific API in order to access and utilize data.
You need to know only one API, the SDO API, which lets you
work with data from multiple data sources, including
relational databases, entity EJB components, XML pages, Web
services, the Java Connector Architecture, JavaServer Pages
pages, and more.

This package contains only a Java API of SDO 2.1 spec.
EclipseLink is a implementation of this spec.

%package javadoc
Summary:       Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n tuscany-sdo-%{version}-src

%pom_disable_module lib
%pom_disable_module impl
%pom_disable_module tools
%pom_disable_module plugin
%pom_disable_module sample
%pom_disable_module distribution
%pom_disable_module java5tools

sed -i 's|<artifactId>tuscany-sdo-api-r${specVersion}</artifactId>|<artifactId>%{api_name}</artifactId>|' $( find . -iname "pom.xml")

sed -i 's|pom.name|project.name|' sdo-api/pom.xml
sed -i 's|pom.description|project.description|' sdo-api/pom.xml
sed -i 's|pom.organization.name|project.organization.name|' sdo-api/pom.xml
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId='tuscany-sdo-api-r2.1']/pom:version" '
${project.version}'

sed -i 's/\r//' LICENSE NOTICE README RELEASE_NOTES

# RHBZ #842622
sed -i 's#<source>1.4</source>#<source>1.5</source>#' pom.xml sdo-api/pom.xml
sed -i 's#<target>1.4</target>#<target>1.5</target>#' pom.xml sdo-api/pom.xml

%build

%mvn_file :%{api_name} %{name}
%mvn_file :%{api_name} tuscany-sdo-api
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README RELEASE_NOTES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Jul 30 2013 gil cattaneo <puntogil@libero.it> 1.1.1-8
- added synlink for backward compatibility

* Mon Jul 01 2013 gil cattaneo <puntogil@libero.it> 1.1.1-7
- switch to XMvn and pom macros, minor changes to adapt to current guideline

* Tue Feb 19 2013 gil cattaneo <puntogil@libero.it> 1.1.1-6
- added maven-shared-components as BR

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jul 24 2012 gil cattaneo <puntogil@libero.it> 1.1.1-3
- Rebuilt RHBZ #842622 (compile with -target 1.5 or greater)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 gil cattaneo <puntogil@libero.it> 1.1.1-1
- initial rpm
