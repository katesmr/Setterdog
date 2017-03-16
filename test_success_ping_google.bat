@echo OFF

python main.py -c "ping google.com" -f test\test_success_ping_google.json

set code=%ERRORLEVEL%

if '%code%' == '45' (
    @echo Success with exit-code %code%
) else (
    @echo Failed test. Program does not have errors.
    @echo Emergency exit with exit-code %code%
)

PAUSE
