# Performance-Measuring
Scripts used for measuring the performance of a Google Cloud Application, using ApacheBench. 

We measured the performance of a simple REST API at various concurency levels in order to gauge how many REST servers were needed so that we could meet the expectations of our users.

The bash script will run tests for all concurency levels, and outputs the results to files. These files are then loaded into the graphing script, and graphs are generated using Plotly.
