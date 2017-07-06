Name:           jupyterhub
Version:        0.7.2
Release:        1%{?dist}
Summary:        A multi-user server for Jupyter notebooks

License:        BSD
URL:            https://github.cop/jupyter/%{name}
Source0:        https://github.com/jupyter/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python34-devel
BuildRequires:    nodejs
BuildRequires:    git
# For tests
#BuildRequires:  python34-pytest
#BuildRequires:  python34-jinja2
#BuildRequires:  python34-requests
#BuildRequires:  python34-sqlalchemy
#BuildRequires:  python34-tornado >= 4
#BuildRequires:  python34-traitlets
Requires:       nodejs
Requires:       python34-pip
Requires:       python34-jinja2
Requires:       python34-requests
Requires:       python34-pamela
Requires:       python34-sqlalchemy >= 1.0
Requires:       python34-tornado >= 4.1
Requires:       python34-traitlets >= 4.3.2

%description
JupyterHub is a multi-user server that manages and proxies multiple instances
of the single-user Jupyter notebook server.

Three actors:

 *  multi-user Hub (tornado process)
 *  configurable http proxy (node-http-proxy)
 *  multiple single-user IPython notebook servers (Python/IPython/tornado)

Basic principles:

 *  Hub spawns proxy
 *  Proxy forwards ~all requests to hub by default
 *  Hub handles login, and spawns single-user servers on demand
 *  Hub configures proxy to forward url prefixes to single-user servers


%prep
%setup -q


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}
npm install
./node_modules/bower/bin/bower install


%post
pip3 install alembic
npm install -g configurable-http-proxy
bower install
gulp js
gulp css

#%check
#py.test-%{python3_version} -v %{name}


%files
%doc README.md
# %license COPYING.md
%{_bindir}/jupyterhub
%{_bindir}/jupyterhub-singleuser
/usr/share/jupyter/hub/
%{python3_sitelib}/*


%changelog
* Thu Jul 6 2017 Steve Jones <stephen.jones@equalexpets.com> - 0.1
- Initial package
