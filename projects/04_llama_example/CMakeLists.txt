set(src test_llama.cpp)
set(deps ${LLAMA_LIB})
add_and_run_code(04_llama_example "${src}" "${LLAMA_LIB}")