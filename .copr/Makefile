repo_dir := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/..)

.PHONY: srpm
srpm:
	test -n "$(outdir)"
	dnf install -y cargo cargo-rpm-macros rpm-build curl tar gzip
	set -eu; workdir=$$(mktemp -d); \
		sh "$(repo_dir)/packaging/fedora/make-srpm.sh" "$$workdir"; \
		cp "$$workdir"/SRPMS/*.src.rpm "$(outdir)/"
