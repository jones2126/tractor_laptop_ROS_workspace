# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/tractor/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/tractor/catkin_ws/build

# Include any dependencies generated for this target.
include BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/depend.make

# Include the progress variables for this target.
include BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/progress.make

# Include the compile flags for this target's objects.
include BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/flags.make

BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.o: BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/flags.make
BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.o: /home/tractor/catkin_ws/src/BehaviorTree.CPP/examples/t07_load_multiple_xml.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/tractor/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.o"
	cd /home/tractor/catkin_ws/build/BehaviorTree.CPP/examples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.o -c /home/tractor/catkin_ws/src/BehaviorTree.CPP/examples/t07_load_multiple_xml.cpp

BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.i"
	cd /home/tractor/catkin_ws/build/BehaviorTree.CPP/examples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tractor/catkin_ws/src/BehaviorTree.CPP/examples/t07_load_multiple_xml.cpp > CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.i

BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.s"
	cd /home/tractor/catkin_ws/build/BehaviorTree.CPP/examples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tractor/catkin_ws/src/BehaviorTree.CPP/examples/t07_load_multiple_xml.cpp -o CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.s

# Object files for target t07_load_multiple_xml
t07_load_multiple_xml_OBJECTS = \
"CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.o"

# External object files for target t07_load_multiple_xml
t07_load_multiple_xml_EXTERNAL_OBJECTS =

/home/tractor/catkin_ws/devel/lib/behaviortree_cpp/t07_load_multiple_xml: BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/t07_load_multiple_xml.cpp.o
/home/tractor/catkin_ws/devel/lib/behaviortree_cpp/t07_load_multiple_xml: BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/build.make
/home/tractor/catkin_ws/devel/lib/behaviortree_cpp/t07_load_multiple_xml: BehaviorTree.CPP/sample_nodes/lib/libbt_sample_nodes.a
/home/tractor/catkin_ws/devel/lib/behaviortree_cpp/t07_load_multiple_xml: /home/tractor/catkin_ws/devel/lib/libbehaviortree_cpp.so
/home/tractor/catkin_ws/devel/lib/behaviortree_cpp/t07_load_multiple_xml: BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/tractor/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/tractor/catkin_ws/devel/lib/behaviortree_cpp/t07_load_multiple_xml"
	cd /home/tractor/catkin_ws/build/BehaviorTree.CPP/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/t07_load_multiple_xml.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/build: /home/tractor/catkin_ws/devel/lib/behaviortree_cpp/t07_load_multiple_xml

.PHONY : BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/build

BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/clean:
	cd /home/tractor/catkin_ws/build/BehaviorTree.CPP/examples && $(CMAKE_COMMAND) -P CMakeFiles/t07_load_multiple_xml.dir/cmake_clean.cmake
.PHONY : BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/clean

BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/depend:
	cd /home/tractor/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/tractor/catkin_ws/src /home/tractor/catkin_ws/src/BehaviorTree.CPP/examples /home/tractor/catkin_ws/build /home/tractor/catkin_ws/build/BehaviorTree.CPP/examples /home/tractor/catkin_ws/build/BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : BehaviorTree.CPP/examples/CMakeFiles/t07_load_multiple_xml.dir/depend

