%global gem_name gpgme

Name:           rubygem-%{gem_name}
Version:        2.0.26
Release:        1%{?dist}
Summary:        Ruby binding of GPGME.
License:        MIT
URL:            https://rubygems.org/gems/gpgme
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires: gcc
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: gpgme-devel
BuildRequires: libassuan-devel
BuildRequires: libgpg-error-devel
Requires: rubygem-mini_portile2

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

ruby -e "
  spec = Gem::Specification.load('../gpgme-%{version}.gemspec')
  spec.require_paths << '/usr/lib64/gems/ruby/gpgme-%{version}'
  File.write('../gpgme-%{version}.gemspec', spec.to_ruby)
"

%build
gem build ../%{gem_name}-%{version}.gemspec
mkdir -p ./usr/share/gems
CONFIGURE_ARGS="--use-system-libraries" \
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_libdir}/gems/ruby/%{gem_name}-%{version}
cp -a .//usr/lib64/gems/ruby/%{gem_name}-%{version}/gpgme_n.so \
    %{buildroot}%{_libdir}/gems/ruby/%{gem_name}-%{version}/

mkdir -p %{buildroot}%{_datadir}/gems/build_info
touch %{buildroot}%{_datadir}/gems/build_info/gpgme-%{version}.info

touch %{buildroot}%{_libdir}/gems/ruby/%{gem_name}-%{version}/gem.build_complete

rm -vr %{buildroot}%{gem_instdir}/examples \
     %{buildroot}%{gem_instdir}/ext \
     %{buildroot}%{gem_instdir}/test
rm -v %{buildroot}%{gem_cache}

%files
%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}
%{gem_extdir_mri}
%{_datadir}/gems/build_info/gpgme-%{version}.info

%files doc
%doc %{gem_docdir}

%changelog
* Tue Jul 21 2026 Luca Albrecht <luca@albright.one> - 2.0.24-1
- Initial package
