# 4051-multiplexer
python version of a 4051 multiplexer chip

I'm working on a lunetta style synthesizer, basically simple audio circuits based off common logic chips.
This script emulates the behavior of a 4051 multiplexer chip - http://www.ti.com/product/CD4051B

the output is based off of whatever combination is fed into the three inputs. this script counts up from 0 to 8,
but you can get unusual patterns by setting any of the inputs to 0 or 1, or randomly chosing 0 or 1.

truth table:

|a | b | c | pin | step #|
|--|--|--|--|--|
|0 | 0 | 0 | A0  | 1|
|0 | 0 | 1 | A1  | 2|
|0 | 1 | 0 | A2  | 3|
|0 | 1 | 1 | A3  | 4|
|1 | 0 | 0 | A4  | 5|
|1 | 0 | 1 | A5  | 6|
|1 | 1 | 0 | A6  | 7|
|1 | 1 | 1 | A7  | 8|


more information on lunettas / boolean synths at https://milkcrate.com.au/_other/sea-moss/

quick 8 step example outputs:

0 0 0

A0

0 0 1

A1

0 1 0

A2

0 1 1

A3

1 0 0

A4

1 0 1

A5

1 1 0

A6

1 1 1

A7



randomized:

0 0 1

A1

1 1 1

A7

0 0 0

A0

1 0 0

A4

1 1 0

A6

1 1 1

A7

0 1 0

A2

1 1 1

using another oscillator and switches to control each bit would lead to interesting patterns. 
