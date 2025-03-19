Name:		swww
Version:	0.9.5
Release:	1
URL:		https://github.com/LGFae/swww
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	A Solution to your Wayland Wallpaper Woes
License:	GPL-3.0
Group:		Wayland/Util

BuildRequires: cargo
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(scdoc)
BuildRequires: cargo-rpm-macros

%description
%summary

%prep
%autosetup -p1
cargo vendor
%cargo_prep -v vendor

%build
cargo build --release
./doc/gen.sh

%install
install -Dpm755 target/release/swww %{buildroot}%{_bindir}/swww
install -Dpm755 target/release/swww-daemon %{buildroot}%{_bindir}/swww-daemon
install -Dpm644 ./doc/generated/*.1 -t %{buildroot}%{_mandir}/man1

%files
%license	LICENSE
%doc README.md
%{_bindir}/swww
%{_bindir}/swww-daemon
%{_mandir}/man1/swww*.1.*

