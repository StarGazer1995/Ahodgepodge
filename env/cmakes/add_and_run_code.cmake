function(add_and_run_code name srcs deps)
    add_executable(${name} ${srcs})
    if (deps)
        target_link_libraries(${name} PRIVATE ${deps})
    endif()
    add_custom_target(run_${name}
        COMMAND ${name}
        DEPENDS ${name}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    )
endfunction()
