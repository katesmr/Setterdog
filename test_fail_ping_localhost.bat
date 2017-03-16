@echo OFF

python main.py -f test\test_fail_ping_localhost.json

set code=%ERRORLEVEL%

if '%code%' == '-1' (
    @echo Success test. Program have errors and it emergency finished with error-code %code%
) else (
    @echo Failed test. Program have errors.
    @echo Exit-code %code%
)

PAUSE
