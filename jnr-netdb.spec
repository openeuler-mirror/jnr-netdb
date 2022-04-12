Name:                jnr-netdb
Version:             1.1.6
Release:             2
Summary:             Network services database access for java
License:             ASL 2.0
URL:                 https://github.com/jnr/%{name}/
Source0:             https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:           noarch
BuildRequires:       maven-local mvn(com.github.jnr:jnr-ffi) mvn(junit:junit)
BuildRequires:       mvn(org.sonatype.oss:oss-parent:pom:)
%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3)

%package        javadoc
Summary:             Javadoc for %{name}
%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find ./ -name '*.jar' -exec rm -f '{}' \;
find ./ -name '*.class' -exec rm -f '{}' \;

%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:2.22.0 . "
<configuration>
    <skipTests>true</skipTests>
</configuration>"

%build
%mvn_build

%install
%mvn_install

%files  -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon Mar 28 2022 wujie <wujie@nj.iscas.ac.cn> - 1.1.6-2
- Fix build error

* Fri Jul 31 2020 Jeffery.Gao <gaojianxing@huawei.com> - 1.1.6-1
- Package init
