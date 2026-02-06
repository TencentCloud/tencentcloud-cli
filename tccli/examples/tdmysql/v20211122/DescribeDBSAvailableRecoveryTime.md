**Example 1: 可恢复时间查询**

可恢复时间查询

Input: 

```
tccli tdmysql DescribeDBSAvailableRecoveryTime --cli-unfold-argument  \
    --InstanceId tdpg-qw8te1qw
```

Output: 
```
{
    "Response": {
        "StartTime": "2024-10-16 12:00:00",
        "EndTime": "2024-10-21 12:00:00",
        "Intervals": [
            {
                "StartTime": "2024-10-16 12:00:00",
                "EndTime": "2024-10-21 12:00:00",
                "MajorVersion": "18.3",
                "MinorVersion": "18.3.0"
            }
        ],
        "RequestId": "ea784d7e-cdcc-41e0-bc6b-4532815d6bf2"
    }
}
```

