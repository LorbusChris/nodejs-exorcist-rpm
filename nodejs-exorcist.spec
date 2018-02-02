%global modulename exorcist
# npm(browserify) and npm(nave) are missing deps for tests
%global enable_tests 0

Name:           nodejs-%{modulename}
Version:        0.4.0
Release:        1
Summary:        Externalizes the source map found inside a stream to an external .js.map file
License:        MIT
URL:            https://github.com/thlorenz/exorcist
Source0:  			https://registry.npmjs.org/%{modulename}/-/%{modulename}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  npm(is-stream) npm(minimist) npm(mkdirp) npm(mold-source-map)
%if 0%{?enable_tests}
BuildRequires:	npm(browserify) npm(nave) npm(proxyquire) npm(tap) npm(through2)
%endif

%description
%{summary}.

%prep
%setup -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modulename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{modulename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/tap test/*.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md example/
%license LICENSE
%{nodejs_sitelib}/%{modulename}

%changelog
* Thu Feb 1 2018 Christian Glombek <christian.glombek@rwth-aachen.de> - 0.4.0-1
- Initial RPM Spec
