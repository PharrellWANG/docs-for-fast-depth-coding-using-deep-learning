About Compilation
=================

Debug and Release
-----------------

- Typically *Release* mode is used to run multiple binaries simultaneously for collecting the data. Speed matters.
- *Debug* mode is used for inspecting/debugging the codebase. You can stop at breakpoint and check values of vars.

Few points to notice:

1. In `TypeDef.h`, the ``MAC_DEBUG_PATH`` need to be toggled for configuring the path when you switch from debug mode and release mode.

2. Remember to toggle the *Release/Debug* Config in **AppCode**.
