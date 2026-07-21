%global gem_name optimist

Name:           rubygem-%{gem_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Optimist is a commandline option parser for Ruby that just gets out of your way.
License:        MIT
URL:            https://rubygems.org/gems/optimist
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

rm -vr %{buildroot}%{gem_instdir}/.github \
     %{buildroot}%{gem_instdir}/.rubocop.yml \
     %{buildroot}%{gem_instdir}/.gitignore \
     %{buildroot}%{gem_instdir}/.codeclimate.yml \
     %{buildroot}%{gem_instdir}/.rubocop_cc.yml \
     %{buildroot}%{gem_instdir}/.rubocop_local.yml \
     %{buildroot}%{gem_instdir}/.whitesource
rm -v %{buildroot}%{gem_cache}

%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/{README,CHANGELOG,HISTORY,PLUGINS}.md
%doc %{gem_instdir}/FAQ.txt
%doc %{gem_instdir}/History.txt
%{gem_instdir}/test
%{gem_instdir}/{Gemfile,Rakefile,%{gem_name}.gemspec}

%changelog
* Tue Jul 21 2026 Luca Albrecht <luca@albright.one> - 3.1.0-1
- Initial package
