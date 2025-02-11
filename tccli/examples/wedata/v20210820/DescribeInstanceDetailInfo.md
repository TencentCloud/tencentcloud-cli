**Example 1: 样例**



Input: 

```
tccli wedata DescribeInstanceDetailInfo --cli-unfold-argument  \
    --TaskId 231232313 \
    --CurRunDate 2024-10-01 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "231232313",
                "CurRunDate": "2024-10-01 00:00:00",
                "LifeRound": 0,
                "RunType": "REDO",
                "Tries": 0,
                "InstanceLifeDetailDtoList": [
                    {
                        "State": "RUNNING",
                        "StartTime": "231232313"
                    }
                ],
                "RunnerState": "RUNNING",
                "ErrorDesc": "",
                "ErrorCodeLevel": "",
                "InstanceLogListOpsDto": {
                    "TaskId": "231232313",
                    "CurRunDate": "2024-10-01 00:00:00",
                    "Tries": "1",
                    "LastUpdate": "2024-10-01 00:00:00",
                    "BrokerIp": "10.0.0.1",
                    "FileSize": "1000",
                    "OriginFileName": "test.log",
                    "CreateTime": "2024-10-01 00:00:00",
                    "InstanceLogType": "2",
                    "TaskName": "测试任务",
                    "CostTime": "10",
                    "InstanceStatus": "RUNNING",
                    "CodeFileName": "info.log",
                    "ExtensionInfo": [
                        {
                            "Key": "",
                            "Value": "",
                            "Description": ""
                        }
                    ]
                }
            }
        ],
        "RequestId": "12312434"
    }
}
```

