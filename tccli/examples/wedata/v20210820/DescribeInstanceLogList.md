**Example 1: 获取离线任务实例运行日志列表**

获取离线任务实例运行日志列表

Input: 

```
tccli wedata DescribeInstanceLogList --cli-unfold-argument  \
    --TaskId 20220408130054538 \
    --CurRunDate 2022-04-10 19:38:37
```

Output: 
```
{
    "Response": {
        "Data": "true",
        "InstanceLogList": [
            {
                "TaskId": "20220408130054538",
                "CurRunDate": "2022-04-10 19:38:37",
                "Tries": "null",
                "LastUpdate": "2022-04-10 19:38:37",
                "BrokerIp": "172.1.1.1",
                "FileSize": "10mb",
                "OriginFileName": "ins-1",
                "CreateTime": "2022-04-10 19:38:37",
                "InstanceLogType": "info",
                "TaskName": "1",
                "CostTime": "123000"
            }
        ],
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

