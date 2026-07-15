**Example 1: TriggerStrategy 调用示例**



Input: 

```
tccli ccc CreateAutoCalloutTask --cli-unfold-argument  \
    --SdkAppId 1500098925 \
    --NotBefore 1777641412 \
    --Callees 008613675881491 \
    --Callers 0086075533614747 \
    --Name dinoggagagag \
    --TimeZone Asia/Shanghai \
    --AIAgentId 973 \
    --TriggerStrategy.0.InterfaceConfig.Url https://webhook.site/8f9aa946-3190-4107-b175-38914e8aa6f6 \
    --TriggerStrategy.0.InterfaceConfig.HeaderParams.0.Key taskid \
    --TriggerStrategy.0.InterfaceConfig.HeaderParams.0.Value {taskId} \
    --TriggerStrategy.0.InterfaceConfig.Params.0.Key callStatus \
    --TriggerStrategy.0.InterfaceConfig.Params.0.Value {callStatus} \
    --TriggerStrategy.0.InterfaceConfig.Async False \
    --TriggerStrategy.0.HangupTypes 202 203 206 \
    --TriggerStrategy.0.CallTags.0.TagName test123 \
    --TriggerStrategy.0.CallTags.0.TagValue 345 \
    --TriggerStrategy.0.TriggerMode ALWAYS_ON_MATCH
```

Output: 
```
{
    "Response": {
        "RequestId": "ec683719-4460-4686-b976-a6dd64e4accb",
        "TaskId": 17110
    }
}
```

