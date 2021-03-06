# Created by pyp2rpm-3.3.3
%global pypi_name requre

Name:           python-%{pypi_name}
Version:        0.2.4
Release:        1%{?dist}
Summary:        Python library what allows re/store output of various objects for testing

License:        MIT
URL:            https://github.com/packit-service/requre
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python3dist(sphinx)

%description
REQUest REcordingRequre [rekure] - Is Library for storing output of various
function and methods to persistent storage and be able to replay the stored
output to functions.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
REQUest REcordingRequre [rekure] - Is Library for storing output of various
function and methods to persistent storage and be able to replay the stored
output to functions.

%package -n python-%{pypi_name}-doc
Summary:        requre documentation
%description -n python-%{pypi_name}-doc
Documentation for requre

%check
make check

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/requre-patch
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jan 15 2020 Jan Ščotka <jscotka@redhat.com> - 0.2.0-1
- Initial package.
