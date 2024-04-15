**Example 1: 获取实例日志列表**

实例运维-获取实例日志列表

Input: 

```
tccli wedata DescribeOpsInstanceLogList --cli-unfold-argument  \
    --TaskId 201234567889999 \
    --CurRunDate 2024-04-06 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "1234567889999",
                "CurRunDate": "2024-04-09 00:00:00",
                "Tries": "1",
                "LastUpdate": "2024-04-09 00:00:00",
                "BrokerIp": "ins-841jqgbx",
                "FileSize": "10",
                "OriginFileName": "201234567889999-9-all-log-0.20240410203512.log",
                "CreateTime": "2024-02-09 00:00:00",
                "InstanceLogType": "run",
                "TaskName": "test_task_0",
                "CostTime": "00:05",
                "InstanceStatus": "RUNNING"
            }
        ],
        "RequestId": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    }
}
```

