#!/bin/bash
set -o errexit

 # Get project path.
PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd ${PROJECT_PATH}

 # Run tests.
for TEST_FILE in $(find tests -name "*_test.py"); do
    echo "Running tests in ${TEST_FILE}"
    python ${TEST_FILE}
done
echo "All tests passed!"

popd
