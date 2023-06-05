**Example 1: 获取离线任务实例运行日志列表**

获取离线任务实例运行日志列表

Input: 

```
tccli wedata DescribeInstanceLogList --cli-unfold-argument  \
    --TaskId abc \
    --CurRunDate abc
```

Output: 
```
{
    "Response": {
        "Data": "abc",
        "InstanceLogList": [
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
                "CostTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

