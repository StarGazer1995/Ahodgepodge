
function(add_and_run_test name srcs deps)
    add_executable(${name} ${srcs})
    if (deps)
        target_link_libraries(${name} PRIVATE ${deps})
    endif()
    target_link_libraries(${name} PRIVATE gtest gtest_main)
    add_test(NAME test_${name}, COMMAND ${name}) 
endfunction()