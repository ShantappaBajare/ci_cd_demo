@echo off

echo Starting Test Execution...

pytest tests -v --html=reports\report.html --self-contained-html

echo Test Execution Completed

pause