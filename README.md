# InsightChallenge
## Author

Yuanxu Wu

## Prerequisite

Python

## How to run the application

method 1: `run.sh`

method 2: `python` `src/InsightChallange.py` `<actual value filename>` `<predicted value filename>` `<window size filename>` `<output filename>`

e.g. `python` `src/InsightChallange.py` `input/actual.txt` `input/predicted.txt` `input/window.txt` `output/comparison.txt`

## Challange Detail

You will read two different files, one provides the actual value of each stock every hour and the second lists the predicted value of various stocks at a certain hour during the same time period.

You will obtain the `average error` by calculating the average difference between the actual stock prices and predicted values over a specified sliding time window.

You are given the following input files

1. `actual.txt`: A time-ordered file listing the actual value of stocks at a given hour.
1. `predicted.txt`: A time-ordered file of the predicted value of certain stocks at a given hour. 
1. `window.txt`: Holds a single integer value denoting the window size (in hours) for which you must calculate the `average error`.

You may have multiple stocks for the same hour. While stock prices in the real world can change every second, for the purposes of this challenge, you can assume they only change every hour.

You are expected to produce the following output file

1. `comparison.txt`: A time-ordered file containing the average error of stock predictions for a certain time period

## Example

To make reading the below example easier, there is a new line between each hour of information in `actual.txt` and `predicted.txt`. There will **NOT** be that extra new line in the actual input files we'll test your code on.

##### window.txt
```
2
```

##### actual.txt
```
1|SLKWVA|94.51
1|CMWTQH|81.27
1|ATAYJP|25.74
1|HVIWZR|22.81

2|ATAYJP|29.62
2|SLKWVA|81.87
2|CMWTQH|116.11
2|HVIWZR|22.15

3|ATAYJP|21.93
3|HVIWZR|22.24
3|SLKWVA|78.01
3|CMWTQH|113.63

```


##### predicted.txt
```
1|ATAYJP|25.71
1|HVIWZR|22.80
1|SLKWVA|94.49
1|CMWTQH|81.22

2|ATAYJP|29.92
2|HVIWZR|22.06

3|ATAYJP|21.84
3|HVIWZR|22.36
3|SLKWVA|79.49

```


This example provides the value for stocks `SLKWVA`, `CMWTQH`, `ATAYJP` and `HVIWZR` for hours `1, 2 and 3`.

You have noticed that the predicted file is shorter than the actual file. This is because it only contains high confidence predictions. 

In this example, because `window.txt` contains the value `2`, we will compute the `average error` over two hour time windows. 

We compare every stock and time pair in `actual.txt` with its companion in `predicted.txt` and calculate the `error` between them. If we do not have a match for a stock at a particular time, we ignore the row and continue. 

Below is an example of that comparison:

#### Time window: `1 to 2`
```
actual              predicted           error
1|ATAYJP|25.74      1|ATAYJP|25.71      0.03
1|SLKWVA|94.51      1|SLKWVA|94.49      0.02
1|CMWTQH|81.27      1|CMWTQH|81.22      0.05
1|HVIWZR|22.81      1|HVIWZR|22.80      0.01
2|SLKWVA|81.87      no data present     ignore
2|ATAYJP|29.62      2|ATAYJP|29.92      0.30
2|HVIWZR|22.15      2|HVIWZR|22.06      0.09
2|CMWTQH|116.11     no data present     ignore
```

#### Time window: `2 to 3`
```
actual              predicted           error
2|SLKWVA|81.87      no data present     ignore
2|ATAYJP|29.62      2|ATAYJP|29.92      0.30
2|HVIWZR|22.15      2|HVIWZR|22.06      0.09
2|CMWTQH|116.11     no data present     ignore
3|ATAYJP|21.93      3|ATAYJP|21.84      0.09
3|HVIWZR|22.24      3|HVIWZR|22.36      0.12
3|SLKWVA|78.01      3|SLKWVA|79.49      1.48
3|CMWTQH|113.63     no data present     ignore
```

### Calculating average error

We take the average of the error for each time window ignoring those entries that have no data present in `predicted.txt`. 

For the first time window, the `average error` is `0.08` or `(0.03 + 0.02 + 0.05 + 0.01 + 0.30 + 0.09)/6` 

And for the second time window, the `average error` is `0.42` or `(0.30 + 0.09 + 0.09 + 0.12 + 1.48)/5`

The results would be written to the output file as seen below. 

##### comparison.txt
```
1|2|0.08
2|3|0.42
```
