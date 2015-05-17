%define __noautoprov '(.*)\\.so(.*)'

Summary:	EFL bindings for Python
Name:		python-efl
Version:	1.14.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/bindings/python/%{name}-%{version}.tar.bz2
Patch0:		python-efl-1.13.0-linkage.patch
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(eo)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(python)
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
%patch0 -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

