%global gem_name hiera-eyaml-gpg

Name:           rubygem-%{gem_name}
Version:        0.7.4
Release:        1%{?dist}
Summary:        Encryption plugin for hiera-eyaml backend for Hiera

License:        MIT
URL:            https://rubygems.org/gems/optimist
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel
Requires: rubygem-hiera-eyaml
Requires: rubygem-gpgme

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

# Patch gemspec directly due to broken gemspec_add_dep macro on Fedora 43
ruby -e "
  spec = Gem::Specification.load('../%{gem_name}-%{version}.gemspec')
  spec.dependencies.reject! { |d| d.name == 'highline' }
  unless spec.dependencies.any? { |d| d.name == 'hiera-eyaml' }
    spec.add_runtime_dependency 'hiera-eyaml'
  end
  File.write('../%{gem_name}-%{version}.gemspec', spec.to_ruby)
"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

rm -vr %{buildroot}%{gem_instdir}/.gitignore \
       %{buildroot}%{gem_instdir}/.rubocop.yml \
       %{buildroot}%{gem_instdir}/.travis.yml \
       %{buildroot}%{gem_instdir}/Gemfile \
       %{buildroot}%{gem_instdir}/Rakefile \
       %{buildroot}%{gem_instdir}/tools
rm -v %{buildroot}%{gem_cache}

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/{README,CHANGELOG,HISTORY,PLUGINS}.md
%{gem_instdir}/{Gemfile,Rakefile,%{gem_name}.gemspec}

%changelog
* Tue Jul 21 2026 Luca Albrecht <luca@albright.one> - 0.7.4-1
- Initial package
