:: unit-test file should be in the current folder
:: script expects there will be "submissions" folder, and in it - different folder for every student

@echo off
IF NOT EXIST results mkdir results
FOR /D %%X in (%1\*) DO (
  SET PYTHONPATH=%CD%\%%X
  echo Testing %%~nxX...
  ::python -m unittest -v -b 2> results\test_results.%%~nxX.txt > nul
  ::nosetests --with-xunit --xunit-file=results\test_results.%%~nxX.xml 2> nul > nul
  nosetests -v --with-xunit --xunit-file="results\test_results.%%~nxX.xml" 2> "results\test_results.%%~nxX.txt" > nul
)
python collect_results.py
echo Done.
