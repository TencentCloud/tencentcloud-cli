**Example 1: 查询事件详情**

查询事件详情

Input: 

```
tccli wedata DescribeDsEventDetail --cli-unfold-argument  \
    --ProjectId abc \
    --EventName abc \
    --DisplayTask True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Name": "abc",
            "EventType": "abc",
            "EventSubType": "abc",
            "EventBroadcastType": "abc",
            "DimensionFormat": "abc",
            "TimeToLive": "abc",
            "TimeUnit": "abc",
            "CreationTs": "abc",
            "Owner": "abc",
            "Properties": "abc",
            "Description": "abc",
            "Listeners": [
                {
                    "Key": "abc",
                    "Type": "abc",
                    "CreationTs": "abc",
                    "PropertiesList": [
                        {
                            "ParamKey": "abc",
                            "ParamValue": "abc"
                        }
                    ],
                    "EventName": "abc",
                    "TaskInfo": {
                        "TaskId": "abc",
                        "TaskName": "abc",
                        "WorkflowId": "abc",
                        "WorkflowName": "abc",
                        "TaskTypeId": "abc",
                        "TaskType": "abc",
                        "ProjectId": "abc"
                    }
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

