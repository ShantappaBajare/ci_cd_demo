#!/bin/bash

echo "Starting Test Execution..."

# Activate virtual environment
source .venv/bin/activate

pytest tests -v --html=reports/report.html --self-contained-html

echo "Test Execution Completed"

#!/bin/bash

#echo "Starting Test Execution..."

#source .venv/bin/activate

#pytest tests -v -m "$1" --html=reports/report.html --self-contained-html

#echo "Test Execution Completed"

#cmd: ./run.sh smoke/sanity/regression