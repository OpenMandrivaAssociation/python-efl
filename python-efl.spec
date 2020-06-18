%define __noautoprov '(.*)\\.so(.*)'
%define efl_ver 1.24.3

Summary:	EFL bindings for Python
Name:		python-efl
Version:	1.24.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/bindings/python/%{name}-%{version}.tar.xz
Patch0:         remove-clang-unkown-no-var-tracking-assignments-option.patch
Patch1:         setup-py-linkage.patch
BuildRequires:	python-dbus-devel
BuildRequires:	pkgconfig(ecore) >= %{efl_ver}
BuildRequires:	pkgconfig(ecore-file) >= efl_ver
BuildRequires:	pkgconfig(edje) >= efl_ver
BuildRequires:	pkgconfig(eina) >= efl_ver
BuildRequires:	pkgconfig(elementary) >= efl_ver
BuildRequires:	pkgconfig(emotion) >= efl_ver
BuildRequires:	pkgconfig(eo) >= efl_ver
BuildRequires:	pkgconfig(evas) >= efl_ver
BuildRequires:	pkgconfig(python)
BuildRequires:	python-cython


%description
Python support files for EFL.

%files
%doc README
%{py_platsitedir}/efl/*
%{py_platsitedir}/python_efl-%{version}-py%{py_ver}.egg-info

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 
%patch1 -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

