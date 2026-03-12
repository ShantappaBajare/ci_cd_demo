import pytest

if __name__ == "__main__":
    pytest.main([
        "tests/",
        "--html=reports/report.html",
        "--self-contained-html",
        "-v"
    ])