#!/usr/bin/env bash

set -ue

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

SRC_DIR="$SCRIPT_DIR/../src"

STAGING_DIR=$(mktemp -d)
BUILD_DIR="$SCRIPT_DIR/../build"

# recreate the build dir to make sure it's clean
rm -rf "$BUILD_DIR"
mkdir "$BUILD_DIR"

for app_dir in "$SRC_DIR"/* ; do
    if [[ ! -d "$app_dir" ]]; then
        continue
    fi

    requirements_file="$app_dir/requirements.txt"
    lambda_func_file="$app_dir/lambda_function.py"

    if [[ ! -f "$requirements_file" || ! -f "$lambda_func_file" ]]; then
        continue
    fi

    app_name=$(basename "$app_dir")

    echo 2>&1 "Building $app_name"

    # clear out the staging directory
    rm -rf "$STAGING_DIR/*"

    # copy the needed bits of the staging directory
    cp "$app_dir/requirements.txt" "$app_dir/lambda_function.py" "$STAGING_DIR"

    app_dependencies_archive="$STAGING_DIR/${app_name}-dependencies.zip"
    app_archive="$STAGING_DIR/$app_name.zip"

    # subshell as we're going to cd into the staging directory
    (
        cd "$STAGING_DIR"
        python3.10 -m venv env
        source env/bin/activate
        pip install -r requirements.txt
        mkdir python
        cp -R env/. python/.
        zip -r "$app_dependencies_archive" python
        zip "$app_archive" lambda_function.py
    )

    # copy the resultant archive to the build dir
    cp "$app_archive" "$app_dependencies_archive" build/
done
