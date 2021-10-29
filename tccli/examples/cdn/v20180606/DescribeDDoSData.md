**Example 1: DDoS统计数据查询**



Input: 

```
tccli cdn DescribeDDoSData --cli-unfold-argument  \
    --StartTime '2020-09-22 00:00:00' \
    --EndTime '2020-09-22 01:00:00' \
    --Interval min
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "AttackBandwidthData": [
            {
                "Time": "2020-01-01 00:00:00",
                "Value": 0.0,
                "AttackType": "all"
            }
        ],
        "Data": [
            {
                "Time": "2020-01-01 00:00:00",
                "Value": 1
            },
            {
                "Time": "2020-01-01 00:01:00",
                "Value": 1
            }
        ],
        "Interval": "min"
    }
}
```

