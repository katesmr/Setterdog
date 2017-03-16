# [\<ACDC/\>] setterdog
## Basic requirements

  - **must** be a console application
  - **must** be configurable using config file in JSON format
  - **must** have default configuration file
  - **must** have ability to launch external lint\build tool
    - build\lint tool to be launched - always CLI application
  - **must** return the error code (not 0) if any pattern was triggered during launch
  - **must** return 0 if no pattern was triggered during launch
  - **must** have Command Line Interface to override base configuration

## Configuration
    
  - **must** have ability to set the command to launch build\lint tool (including command line arguments for it) in configuration file
  - **must** support at leaast two types of report input: catch STDOUT of the build\lint tool or set the path to the file of report
  - **must** have an ability to specify the set of regular expressions (criterias) - line patterns to be found in reports.
    
## Criteria

  - criteria **must** be a regular expression
  - **must** support the set of criterias (more then one)
  - each criteria **may** have own error code

## Artifacts
    
  - **may** store the lint\build report
  - **may** return the statistic information about how much patterns of specific types occured in 


