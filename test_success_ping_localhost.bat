@echo OFF

python main.py -f test\test_success_ping_localhost.json

set code=%ERRORLEVEL%

if '%code%' == '11' (
    @echo Success with exit-code %code%
) else (
    @echo Failed test. Program does not have errors.
    @echo Emergency exit with exit-code %code%
)

PAUSE
