function(add_and_run_bench name srcs deps)
    add_executable(${name} ${srcs})
    if (deps)
        target_link_libraries(${name} PRIVATE ${deps})
    endif()
    target_link_libraries(${name} PRIVATE benchmark::benchmark)
    add_custom_target(bench_${name}
        COMMAND ${name}
        DEPENDS ${name}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    )
endfunction()