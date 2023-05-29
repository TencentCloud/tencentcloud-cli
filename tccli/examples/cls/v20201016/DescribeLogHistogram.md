**Example 1: 获取日志分布直方图**

根据指定的检索条件，获取符合检索条件的日志分布直方图

Input: 

```
tccli cls DescribeLogHistogram --cli-unfold-argument  \
    --From 1685086740862 \
    --To 1685087640862 \
    --Interval 30000 \
    --TopicId 2e7b5c4d-1be3-484a-xxxx-8705adb56dcd \
    --Query  \
    --SyntaxRule 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 14,
        "Interval": 30000,
        "HistogramInfos": [
            {
                "Count": 0,
                "BTime": 1685086740000
            },
            {
                "Count": 0,
                "BTime": 1685086770000
            },
            {
                "Count": 0,
                "BTime": 1685086800000
            },
            {
                "Count": 0,
                "BTime": 1685086830000
            },
            {
                "Count": 0,
                "BTime": 1685086860000
            },
            {
                "Count": 0,
                "BTime": 1685086890000
            },
            {
                "Count": 0,
                "BTime": 1685086920000
            },
            {
                "Count": 0,
                "BTime": 1685086950000
            },
            {
                "Count": 0,
                "BTime": 1685086980000
            },
            {
                "Count": 0,
                "BTime": 1685087010000
            },
            {
                "Count": 0,
                "BTime": 1685087040000
            },
            {
                "Count": 0,
                "BTime": 1685087070000
            },
            {
                "Count": 0,
                "BTime": 1685087100000
            },
            {
                "Count": 0,
                "BTime": 1685087130000
            },
            {
                "Count": 0,
                "BTime": 1685087160000
            },
            {
                "Count": 0,
                "BTime": 1685087190000
            },
            {
                "Count": 0,
                "BTime": 1685087220000
            },
            {
                "Count": 0,
                "BTime": 1685087250000
            },
            {
                "Count": 0,
                "BTime": 1685087280000
            },
            {
                "Count": 0,
                "BTime": 1685087310000
            },
            {
                "Count": 0,
                "BTime": 1685087340000
            },
            {
                "Count": 0,
                "BTime": 1685087370000
            },
            {
                "Count": 0,
                "BTime": 1685087400000
            },
            {
                "Count": 0,
                "BTime": 1685087430000
            },
            {
                "Count": 0,
                "BTime": 1685087460000
            },
            {
                "Count": 0,
                "BTime": 1685087490000
            },
            {
                "Count": 0,
                "BTime": 1685087520000
            },
            {
                "Count": 0,
                "BTime": 1685087550000
            },
            {
                "Count": 0,
                "BTime": 1685087580000
            },
            {
                "Count": 14,
                "BTime": 1685087610000
            },
            {
                "Count": 0,
                "BTime": 1685087640000
            }
        ],
        "RequestId": "4279ae1f-cbd6-438b-xxxx-6df5a8152afd"
    }
}
```

