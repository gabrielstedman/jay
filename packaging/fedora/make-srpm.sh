#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
    echo "Usage: sh $0 EMPTY_WORK_DIRECTORY" >&2
    exit 2
fi

spec_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
spec="$spec_dir/jay.spec"
mkdir -p "$1"
workdir=$(CDPATH= cd -- "$1" && pwd)
if [ -n "$(ls -A "$workdir")" ]; then
    echo "Work directory must be empty: $workdir" >&2
    exit 1
fi

version=$(rpmspec -q --srpm --qf '%{VERSION}' "$spec")
mkdir -p "$workdir/SOURCES" "$workdir/SRPMS"
archive="jay-$version.tar.gz"
curl -fL "https://github.com/mahkoh/jay/archive/refs/tags/v$version/$archive" \
    -o "$workdir/SOURCES/$archive"
tar -xzf "$workdir/SOURCES/$archive" -C "$workdir"
cargo vendor --locked --manifest-path "$workdir/jay-$version/Cargo.toml" "$workdir/vendor" > /dev/null
tar -czf "$workdir/SOURCES/jay-$version-vendor.tar.gz" -C "$workdir" vendor
rpmbuild -bs --define "_topdir $workdir" "$spec"
