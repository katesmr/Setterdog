@echo OFF

python main.py -f test\test_success_ping_mozila.json -d ERROR

set code=%ERRORLEVEL%

if '%code%' == '22' (
    @echo Success with exit-code %code%
) else (
    @echo Failed test. Program does not have errors.
    @echo Emergency exit with exit-code %code%
)

PAUSE
