**Example 1: 可恢复时间查询**

可恢复时间查询

Input: 

```
tccli tdmysql DescribeDBSAvailableRecoveryTime --cli-unfold-argument  \
    --InstanceId tdsql3-3f17e49d
```

Output: 
```
{
    "Response": {
        "EndTime": "2026-03-26 20:12:29",
        "Intervals": [
            {
                "EndTime": "2026-03-26 20:12:29",
                "MajorVersion": "",
                "MinorVersion": "",
                "StartTime": "2026-03-23 22:14:09"
            }
        ],
        "StartTime": "2026-03-23 22:14:09",
        "RequestId": "2c15b222-d578-4173-a2fb-fb4843a9983e"
    }
}
```

