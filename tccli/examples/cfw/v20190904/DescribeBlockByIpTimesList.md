**Example 1: DescribeBlockByIpTimesList 告警中心阻断IP折线图**

DescribeBlockByIpTimesList 告警中心阻断IP折线图

Input: 

```
tccli cfw DescribeBlockByIpTimesList --cli-unfold-argument  \
    --Direction 0 \
    --EdgeId vpc \
    --EndTime 2024-11-01 11:43:13 \
    --Ip 80.75.212.46 \
    --LogSource move \
    --Source 3 \
    --StartTime 2024-10-25 11:43:13 \
    --Zone ap-beijing
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Num": 1,
                "StatTime": "10-25 00:00"
            },
            {
                "Num": 3,
                "StatTime": "10-26 00:00"
            },
            {
                "Num": 0,
                "StatTime": "10-27 00:00"
            },
            {
                "Num": 0,
                "StatTime": "10-28 00:00"
            },
            {
                "Num": 0,
                "StatTime": "10-29 00:00"
            },
            {
                "Num": 0,
                "StatTime": "10-30 00:00"
            },
            {
                "Num": 0,
                "StatTime": "10-31 00:00"
            },
            {
                "Num": 0,
                "StatTime": "11-01 00:00"
            }
        ],
        "RequestId": "269ab1ff-475a-4d65-93b1-623a16870f22"
    }
}
```

