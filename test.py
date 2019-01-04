OUT_LOG=$(ci/scripts/test_python_module.sh)

if [[ "$OUT_LOG" == "*traceback error*" ]]; then echo "traceback error detected" ; fi