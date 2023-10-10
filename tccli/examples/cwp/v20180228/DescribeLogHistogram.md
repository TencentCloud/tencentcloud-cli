**Example 1: 示例**



Input: 

```
tccli cwp DescribeLogHistogram --cli-unfold-argument  \
    --EndTime 1660533600000 \
    --Interval 500000 \
    --QueryString  \
    --StartTime 1660532400000
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 49,
                "TimeStamp": 1660532000000
            },
            {
                "Count": 158,
                "TimeStamp": 1660532500000
            },
            {
                "Count": 136,
                "TimeStamp": 1660533000000
            },
            {
                "Count": 0,
                "TimeStamp": 1660533500000
            }
        ],
        "Period": 500000,
        "RequestId": "b8748ca2-de8e-4ccb-b369-99d7f65907cf",
        "TotalCount": 343
    }
}
```

