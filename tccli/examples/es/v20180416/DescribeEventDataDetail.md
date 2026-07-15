**Example 1: DescribeEventDataDetail示例**



Input: 

```
tccli es DescribeEventDataDetail --cli-unfold-argument  \
    --EventTaskId 3 \
    --EventType 1 \
    --InstanceId es-8f6p8dsa
```

Output: 
```
{
    "Response": {
        "EventDataDetail": {
            "EventName": "集群节点底层机器存在隐患",
            "EventImportance": 1,
            "EventContent": "集群节点底层机器存在隐患，需检查集群状态，可根据实际影响情况，对节点进行关机或蓝绿重启操作",
            "InstanceId": "es-******",
            "InstanceName": "*********",
            "NodeId": "17543933********932",
            "NodeRole": "hotData",
            "EventStatus": 0,
            "EventType": 1,
            "EventTaskId": 3,
            "SubEventType": 101,
            "CvmRepairId": "rep-*******",
            "EventIsolationStatus": 0,
            "StartTime": "2025-08-06 20:16:42",
            "EndTime": ""
        },
        "RequestId": "a24a3089-********-********-bf89-*******"
    }
}
```

