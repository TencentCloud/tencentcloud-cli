**Example 1: 注册事件监听者**

注册事件监听者

Input: 

```
tccli wedata RegisterDsEventListener --cli-unfold-argument  \
    --ProjectId abc \
    --Key abc \
    --Type abc \
    --EventName abc \
    --EventProjectId 23 \
    --Properties.0.ParamKey abc \
    --Properties.0.ParamValue abc
```

Output: 
```
{
    "Response": {
        "Data": {
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
                "ProjectId": "abc",
                "CycleType": "abc"
            },
            "EventProjectId": "abc"
        },
        "RequestId": "abc"
    }
}
```

