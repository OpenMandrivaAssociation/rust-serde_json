# * compiletest_rs and automod are not packaged
%bcond_with check
%global debug_package %{nil}

%global crate serde_json

Name:           rust-%{crate}
Version:        1.0.64
Release:        1
Summary:        JSON serialization file format

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_json
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
JSON serialization file format.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+arbitrary_precision-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary_precision-devel %{_description}

This package contains library source intended for building other packages
which use "arbitrary_precision" feature of "%{crate}" crate.

%files       -n %{name}+arbitrary_precision-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages
which use "indexmap" feature of "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+preserve_order-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+preserve_order-devel %{_description}

This package contains library source intended for building other packages
which use "preserve_order" feature of "%{crate}" crate.

%files       -n %{name}+preserve_order-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+raw_value-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+raw_value-devel %{_description}

This package contains library source intended for building other packages
which use "raw_value" feature of "%{crate}" crate.

%files       -n %{name}+raw_value-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unbounded_depth-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unbounded_depth-devel %{_description}

This package contains library source intended for building other packages
which use "unbounded_depth" feature of "%{crate}" crate.

%files       -n %{name}+unbounded_depth-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
