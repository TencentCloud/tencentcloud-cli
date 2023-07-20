**Example 1: 获取实例日志列表**

实例运维-获取实例日志列表

Input: 

```
tccli wedata DescribeOpsInstanceLogList --cli-unfold-argument  \
    --TaskId abc \
    --CurRunDate abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "abc",
                "CurRunDate": "abc",
                "Tries": "abc",
                "LastUpdate": "abc",
                "BrokerIp": "abc",
                "FileSize": "abc",
                "OriginFileName": "abc",
                "CreateTime": "abc",
                "InstanceLogType": "abc",
                "TaskName": "abc",
                "CostTime": "abc",
                "InstanceStatus": "RUNNING"
            }
        ],
        "RequestId": "abc"
    }
}
```

