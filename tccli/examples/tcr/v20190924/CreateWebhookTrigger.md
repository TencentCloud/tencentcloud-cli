**Example 1: 创建触发器**



Input: 

```
tccli tcr CreateWebhookTrigger --cli-unfold-argument  \
    --RegistryId tcr-7s2d14fn\
    --Namespace someNs\
    --Trigger.Name someTrigger\
    --Trigger.Description 触发器描述\
    --Trigger.Targets.0.Address http://httpbin.org/post\
    --Trigger.Targets.0.Headers.0.Key X-Custom-Header\
    --Trigger.Targets.0.Headers.0.Values abc\
    --Trigger.EventTypes pullImage\
    --Trigger.Condition .*\
    --Trigger.Enabled true
```

Output: 
```
{
    "Response": {
        "RequestId": "db4441cd-1027-4f95-9fe1-df4b85470925"
    }
}
```

