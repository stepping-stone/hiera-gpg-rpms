%global gem_name ruby_gpg

Name:           rubygem-%{gem_name}
Version:        0.3.2
Release:        1%{?dist}
Summary:        Ruby wrapper for the gpg binary
License:        MIT
URL:            https://rubygems.org/gems/%{gem_name}
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel

BuildArch:      noarch

%description
%{summary}.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

rm -vrf %{buildroot}%{gem_instdir}/features \
    %{buildroot}%{gem_instdir}/spec \
    %{buildroot}%{gem_instdir}/test_keys \
    %{buildroot}%{gem_instdir}/.autotest \
    %{buildroot}%{gem_instdir}/cucumber.yml \
    %{buildroot}%{gem_instdir}/VERSION \
    %{buildroot}%{gem_instdir}/.gitignore
rm -v %{buildroot}%{gem_cache}

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%doc %{gem_instdir}/CHANGELOG.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Aug 17 2026 Luca Albrecht <luca@albright.one> - 0.3.2-1
- Initial package
