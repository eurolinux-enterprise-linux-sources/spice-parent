Name:           spice-parent
Version:        15
Release:        11%{?dist}
Summary:        Sonatype Spice Components

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://svn.sonatype.org/spice/tags/spice-parent-15
#svn export http://svn.sonatype.org/spice/tags/spice-parent-15 spice-parent-15
#tar zcf spice-parent-15.tar.gz spice-parent-15/
Source0:        %{name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt
Patch0:         pom.patch

BuildArch: noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  forge-parent

%description
Spice components and libraries are common components
used throughout the Sonatype Forge.

%prep
%setup -q -n %{name}-%{version}

#Remove plexus-javadoc
%patch0

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 15-11
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 15-10
- Migrate away from mvn-rpmbuild (Resolves: #997502)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 15-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec  6 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 15-7
- Fix build requires and requires (#884632)
- Cleanup specfile for latest guidelines 
- Add ASL license text

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 09 2010 Hui Wang <huwang@redhat.com> - 15-3
- Add pom.patch

* Fri May 14 2010 Hui Wang <huwang@redhat.com> - 15-2
- Add instruction which create Source0 as a commont
- Use macros in Source0

* Tue May 11 2010 Hui Wang <huwang@redhat.com> - 15-1
- Initial version of the package
