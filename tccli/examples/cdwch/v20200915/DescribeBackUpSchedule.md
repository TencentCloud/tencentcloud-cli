**Example 1: 示例**

查询备份策略信息

Input: 

```
tccli cdwch DescribeBackUpSchedule --cli-unfold-argument  \
    --InstanceId cdwch-1a1xfbc
```

Output: 
```
{
    "Response": {
        "BackUpOpened": true,
        "MetaStrategy": {
            "CosBucketName": "pa-cold-test-1258142303",
            "RetainDays": 1,
            "WeekDays": "2",
            "ExecuteHour": 5,
            "ScheduleId": 1
        },
        "DataStrategy": {
            "CosBucketName": "pa-cold-test-1268142801",
            "RetainDays": 2,
            "WeekDays": "1",
            "ExecuteHour": 8,
            "ScheduleId": 13
        },
        "BackUpContents": [
            {
                "VCluster": "default_cluster",
                "Database": "default",
                "Table": "stemp",
                "TotalBytes": 1231270,
                "Ips": "10.0.1.23"
            }
        ],
        "BackUpStatus": 0,
        "ErrorMsg": "",
        "RequestId": "asdfaes-xad12x-123axafg"
    }
}
```

