**Example 1: 示例**



Input: 

```
tccli cdwch DescribeBackUpSchedule --cli-unfold-argument  \
    --InstanceId 0
```

Output: 
```
{
    "Response": {
        "DataStrategy": [
            {
                "ExecuteHour": 0,
                "CosBucketName": "xx",
                "RetainDays": 0,
                "WeekDays": "xx"
            }
        ],
        "BackUpOpened": true,
        "BackUpStatus": 0,
        "MetaStrategy": {
            "ExecuteHour": 0,
            "CosBucketName": "xx",
            "RetainDays": 0,
            "WeekDays": "xx"
        },
        "BackUpContents": {
            "Table": "xx",
            "Ips": "xx",
            "VCluster": "xx",
            "TotalBytes": 0,
            "Database": "xx"
        },
        "RequestId": "xx"
    }
}
```

