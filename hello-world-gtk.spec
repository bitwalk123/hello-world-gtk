Name:           hello-world-gtk
Version:        1.0
Release:        1%{?dist}
Summary:        Hello World program with GTK4

License:        Public Domain
URL:            https://github.com/bitwalk123/hello-world-gtk
Source:         %{name}-%{version}.zip

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk4-devel

%description
Hello World program with GTK4.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%license LICENSE
%{_datadir}/applications/hello.desktop
%{_datadir}/icons/hicolor/scalable/apps/hello.svg
%{_bindir}/hello

%changelog
* Wed Dec 23 2020 Fuhito Suguri <bitwalk@users.sourceforge.net> - 1.0-1
- Initial package
