**Example 1: Waf统计数据查询**



Input: 

```
tccli cdn DescribeWafData --cli-unfold-argument  \
    --Domain www.test.com \
    --StartTime '2019-06-11 00:00:00' \
    --EndTime '2019-06-11 23:59:59' \
    --Interval hour
```

Output: 
```
{
    "Response": {
        "RequestId": "d9b58c40-562c-4ac1-8aea-755547beefa3",
        "Data": [
            {
                "Time": "2019-06-26 00:00:00",
                "Value": 0
            },
            {
                "Time": "2019-06-26 01:00:00",
                "Value": 1
            },
            {
                "Time": "2019-06-26 02:00:00",
                "Value": 2
            },
            {
                "Time": "2019-06-26 03:00:00",
                "Value": 9
            },
            {
                "Time": "2019-06-26 04:00:00",
                "Value": 0
            }
        ],
        "Interval": "hour"
    }
}
```

