**Example 1: 注册事件**

注册事件

Input: 

```
tccli wedata RegisterDsEvent --cli-unfold-argument  \
    --ProjectId abc \
    --Name abc \
    --EventType abc \
    --EventSubType abc \
    --EventBroadcastType abc \
    --DimensionFormat abc \
    --TimeToLive abc \
    --TimeUnit abc \
    --Owner abc \
    --Description abc
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
            "TimeToLive": 0,
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
                        "TaskTypeId": 0,
                        "TaskType": "abc",
                        "ProjectId": "abc"
                    },
                    "EventProjectId": "abc"
                }
            ],
            "ProjectId": "abc",
            "ProjectName": "abc"
        },
        "RequestId": "abc"
    }
}
```

