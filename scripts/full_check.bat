@echo off
SET SUBMISSION_PATH=submissions
IF NOT "%1"=="" SET SUBMISSION_PATH=%1
call all_py2rtf.bat %SUBMISSION_PATH%
call execute_all_tests.bat %SUBMISSION_PATH%
echo %~n0 Done.