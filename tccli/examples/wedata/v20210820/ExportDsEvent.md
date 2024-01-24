**Example 1: 事件导出**

事件导出

Input: 

```
tccli wedata ExportDsEvent --cli-unfold-argument  \
    --ProjectId abc \
    --OriginDomain abc \
    --Range abc \
    --EventNames abc \
    --Events.0.Name abc \
    --Events.0.EventType abc \
    --Events.0.EventSubType abc \
    --Events.0.EventBroadcastType abc \
    --Events.0.DimensionFormat abc \
    --Events.0.TimeToLive 1 \
    --Events.0.TimeUnit abc \
    --Events.0.CreationTs abc \
    --Events.0.Owner abc \
    --Events.0.Properties abc \
    --Events.0.Description abc \
    --Events.0.Listeners.0.Key abc \
    --Events.0.Listeners.0.Type abc \
    --Events.0.Listeners.0.CreationTs abc \
    --Events.0.Listeners.0.PropertiesList.0.ParamKey abc \
    --Events.0.Listeners.0.PropertiesList.0.ParamValue abc \
    --Events.0.Listeners.0.EventName abc \
    --Events.0.Listeners.0.TaskInfo.TaskId abc \
    --Events.0.Listeners.0.TaskInfo.TaskName abc \
    --Events.0.Listeners.0.TaskInfo.WorkflowId abc \
    --Events.0.Listeners.0.TaskInfo.WorkflowName abc \
    --Events.0.Listeners.0.TaskInfo.TaskTypeId 31 \
    --Events.0.Listeners.0.TaskInfo.TaskType abc \
    --Events.0.Listeners.0.TaskInfo.ProjectId abc \
    --PublishTime abc \
    --Title abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "CosPath": "abc",
            "CosBucketName": "abc",
            "Region": "abc",
            "Token": "abc",
            "SecretId": "abc",
            "SecretKey": "abc"
        },
        "RequestId": "abc"
    }
}
```

