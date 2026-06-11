**Example 1: 查询策略**



Input: 

```
tccli cynosdb DescribeClusterPeriodScalePolicy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xdbsbsgg
```

Output: 
```
{
    "Response": {
        "PolicyList": [
            {
                "PolicyId": "cynosdbmysql-spd-rye0gd5b",
                "MaxCpu": 4,
                "MinCpu": 1,
                "ScaleStartTime": "10:00",
                "ScaleEndTime": "12:00",
                "PolicyStartTime": "2025-12-01 00:12:00",
                "PolicyEndTime": "2025-12-30 00:20:00",
                "PeriodType": "day",
                "PeriodConfig": [],
                "Status": "normal",
                "CreateTime": "2025-11-01 00:12:00",
                "UpdateTime": "2025-11-21 00:12:00"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

