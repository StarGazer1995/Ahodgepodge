function(getAllSubdirs dir dirs)
    # get subdirectories for dir
    get_property(subdirs DIRECTORY ${dir} PROPERTY SUBDIRECTORIES)
    # iterate any found subdirectories
    foreach(subdir ${subdirs})
        # append each sub directory
        list(APPEND ${dirs} ${subdir})
        getAllSubdirs(${subdir} ${dirs})
    endforeach()
    set(${dirs} ${${dirs}} PARENT_SCOPE)
endfunction()