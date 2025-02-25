@echo OFF
REM="""
setlocal
set PythonExe=
set PythonExeFlags=

for %%i in (cmd bat exe) do (
    for %%j in (python.%%i) do (
        call :SetPythonExe "%%~$PATH:j"
    )
)
for /f "tokens=2 delims==" %%i in ('assoc .py') do (
    for /f "tokens=2 delims==" %%j in ('ftype %%i') do (
        for /f "tokens=1" %%k in ("%%j") do (
            call :SetPythonExe %%k
        )
    )
)
"%PythonExe%" -x %PythonExeFlags% "%~f0" %*
goto :EOF

:SetPythonExe
if not [%1]==[""] (
    if ["%PythonExe%"]==[""] (
        set PythonExe=%~1
    )
)
goto :EOF
"""

# ===================================================
# Python script starts here
# ===================================================

#!/usr/bin/env python

import sys
import petaexpress.cli.driver

def main():
    return petaexpress.cli.driver.main()

if __name__ == '__main__':
    sys.exit(main())
