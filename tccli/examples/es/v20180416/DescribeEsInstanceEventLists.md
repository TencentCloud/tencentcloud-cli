**Example 1: DescribeEsInstanceEventLists接口请求示例**



Input: 

```
tccli es DescribeEsInstanceEventLists --cli-unfold-argument  \
    --EndTime 2025-08-06 20:56:38 \
    --Limit 10 \
    --Offset 0 \
    --StartTime 2025-07-30 20:56:38
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EventDataInfoList": [
            {
                "EventType": 2,
                "EventTaskId": 16676,
                "EventName": "ModifyInstance",
                "EventContent": "{\"OldInfo\":[{\"Key\":\"MasterNodeType\",\"Value\":\"ES.S1.MEDIUM8\"}],\"NewInfo\":[{\"Key\":\"MasterNodeType\",\"Value\":\"ES.S1.MEDIUM4\"}]}",
                "InstanceId": "es-*****",
                "InstanceName": "************",
                "NodeId": "",
                "NodeRole": "",
                "EventStatus": 2,
                "StartTime": "2025-08-06 20:54:01",
                "EndTime": "2025-08-07 20:54:01"
            }
        ],
        "RequestId": "*******************************"
    }
}
```

