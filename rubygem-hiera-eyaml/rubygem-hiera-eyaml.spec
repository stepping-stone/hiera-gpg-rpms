%global gem_name hiera-eyaml

Name:           rubygem-%{gem_name}
Version:        4.3.0
Release:        1%{?dist}
Summary:        Hiera backend for decrypting encrypted yaml properties

License:        MIT
URL:            https://rubygems.org/gems/optimist
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel
Requires: rubygem-optimist

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
%gemspec_remove_dep -g highline
%gemspec_add_dep -g highline

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

rm -vr %{buildroot}%{gem_instdir}/.github \
     %{buildroot}%{gem_instdir}/.rubocop.yml \
     %{buildroot}%{gem_instdir}/.rubocop_todo.yml \
     %{buildroot}%{gem_instdir}/.gitignore \
     %{buildroot}%{gem_instdir}/sublime_text
rm -v %{buildroot}%{gem_cache}

%files
%license %{gem_instdir}/LICENSE.txt
%{_bindir}/eyaml
%dir %{gem_instdir}
%{gem_instdir}/bin

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/{README,CHANGELOG,HISTORY,PLUGINS}.md
%{gem_instdir}/{Gemfile,Rakefile,%{gem_name}.gemspec}

%changelog
* Tue Jul 21 2026 Luca Albrecht <luca@albright.one> - 3.2.0-1
- Initial package
