# Fedora Copr packaging

The spec builds a tagged Jay release with vendored, locked Cargo dependencies.
Copr can generate the source RPM from this repository using the SCM source
type and the `make srpm` method. Set the spec path to
`packaging/fedora/jay.spec` and leave the subdirectory empty. Source generation
needs network access; the RPM builds use the vendored dependencies offline.

To generate a source RPM locally on Fedora:

```sh
sudo dnf install cargo cargo-rpm-macros rpm-build curl
sh packaging/fedora/make-srpm.sh /tmp/jay-copr-srpm
```

The work directory must be empty. The resulting source RPM is in `SRPMS/`.

For each new release, update `Version` and `%changelog` in `jay.spec`, then
regenerate the source RPM. Check the build's `cargo_license_summary` output
and update the `License` field if the linked dependencies' licenses change.
The spec runs a CLI smoke test, not the full test suite, which requires
facilities unavailable in some build sandboxes.
