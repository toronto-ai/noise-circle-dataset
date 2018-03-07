
# Benchmark results - 999 steps

* conv, 3x3, 16 filters -> avg pooling
* conv, 3x3, 32 filters -> avg pooling
* conv, 3x3, 64 filters -> avg pooling
* dense 32
*step: 999, EMA radius error: 34px. EMA center error: 14px*

* conv, 5x5, 16 filters -> avg pooling
* conv, 5x5, 32 filters -> avg pooling
* conv, 5x5, 64 filters -> avg pooling
* dense 32
*step: 999, EMA radius error: 19px. EMA center error: 9px*

* conv, 5x5, 16 filters -> avg pooling
* conv, 5x5, 32 filters -> avg pooling
* conv, 5x5, 64 filters -> avg pooling 
* dense 32
* dense 32
* dense 32
*step: 999, EMA radius error: 13px. EMA center error: 8px*


## Awesome!
* conv, 5x5, 16 filters -> avg pooling
* conv, 5x5, 32 filters -> avg pooling
* conv, 5x5, 64 filters -> avg pooling
* conv, 5x5,128 filters -> avg pooling
* dense 32
* dense 32
* dense 32
*step: 999, EMA radius error: 2px. EMA center error: 4px*
