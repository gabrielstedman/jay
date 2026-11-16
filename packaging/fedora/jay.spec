Name:           jay
Version:        1.15.1
Release:        1%{?dist}
Summary:        Wayland compositor written in Rust
License:        GPL-3.0-only AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT) AND (Zlib OR MIT OR Apache-2.0)
URL:            https://github.com/mahkoh/jay
Source0:        https://github.com/mahkoh/jay/archive/refs/tags/v%{version}/jay-%{version}.tar.gz
Source1:        jay-%{version}-vendor.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pangocairo)

Requires:       mesa-libEGL
Requires:       mesa-libGLES
Requires:       sqlite-libs
Requires:       vulkan-loader
Requires:       xkeyboard-config

Recommends:     mesa-vulkan-drivers
Recommends:     pipewire
Recommends:     xorg-x11-server-Xwayland

%description
Jay is a Wayland compositor with tiling and floating window management.

%prep
%autosetup -n jay-%{version} -a 1
%cargo_prep -v vendor

%build
%cargo_build -- --locked
%cargo_license_summary
%cargo_vendor_manifest

%install
install -Dm755 target/release/jay %{buildroot}%{_bindir}/jay
install -Dm644 etc/jay.desktop %{buildroot}%{_datadir}/wayland-sessions/jay.desktop
install -Dm644 etc/jay.portal %{buildroot}%{_datadir}/xdg-desktop-portal/portals/jay.portal
install -Dm644 etc/jay-portals.conf %{buildroot}%{_datadir}/xdg-desktop-portal/jay-portals.conf
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
target/release/jay generate-completion bash > %{buildroot}%{_datadir}/bash-completion/completions/jay
target/release/jay generate-completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_jay
target/release/jay generate-completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/jay.fish

%check
target/release/jay --help > /dev/null

%files
%license LICENSE cargo-vendor.txt
%doc README.md
%{_bindir}/jay
%{_datadir}/wayland-sessions/jay.desktop
%{_datadir}/xdg-desktop-portal/portals/jay.portal
%{_datadir}/xdg-desktop-portal/jay-portals.conf
%{_datadir}/bash-completion/completions/jay
%{_datadir}/zsh/site-functions/_jay
%{_datadir}/fish/vendor_completions.d/jay.fish

%changelog
* Mon Nov 16 2026 Jay Copr maintainers - 1.15.1-1
- Initial Copr package
