%define __noautoprov '(.*)\\.so(.*)'
%define efl_ver 1.21.1

Summary:	EFL bindings for Python
Name:		python-efl
Version:	1.21.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/bindings/python/%{name}-%{version}.tar.xz
#Patch0:		python-efl-1.13.0-linkage.patch
BuildRequires:	python-dbus-devel
BuildRequires:	pkgconfig(ecore) >= %{efl_ver}
BuildRequires:	pkgconfig(ecore-file) >= efl_ver
BuildRequires:	pkgconfig(edje) >= efl_ver
BuildRequires:	pkgconfig(eina) >= efl_ver
BuildRequires:	pkgconfig(elementary) >= efl_ver
BuildRequires:	pkgconfig(emotion) >= efl_ver
BuildRequires:	pkgconfig(eo) >= efl_ver
BuildRequires:	pkgconfig(evas) >= efl_ver
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-cython
Obsoletes:	python-e_dbus < 1.8.0
Obsoletes:	python-e_dbus < 1.8.0
Obsoletes:	python-ecore < 1.8.0
Obsoletes:	python-ecore-devel < 1.8.0
Obsoletes:	python-edje < 1.8.0
Obsoletes:	python-edje-devel < 1.8.0
Obsoletes:	python-elementary < 1.8.0
Obsoletes:	python-elementary-devel < 1.8.0
Obsoletes:	python-emotion < 1.8.0
Obsoletes:	python-emotion-devel < 1.8.0
Obsoletes:	python-ethumb < 1.8.0
Obsoletes:	python-ethumb-devel < 1.8.0
Obsoletes:	python-evas < 1.8.0
Obsoletes:	python-evas-devel < 1.8.0

%description
Python support files for EFL.

%files
%doc README
%{py_platsitedir}/efl/*
%{py_platsitedir}/python_efl-%{version}-py%{py_ver}.egg-info

#----------------------------------------------------------------------------

%prep
%setup -q
#%%patch0 -p1

%build
export CC=gcc CXX=g++
python setup.py build

%install
python setup.py install --root=%{buildroot}

