**Example 1: 更新触发器**



Input: 

```
tccli tcr ModifyWebhookTrigger --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --Trigger.Name tirgger \
    --Trigger.Targets.0.Address http://www.baidu.com \
    --Trigger.Targets.0.Headers.0.Key k1 \
    --Trigger.Targets.0.Headers.0.Values v1 \
    --Trigger.Targets.0.Headers.1.Key k2 \
    --Trigger.Targets.0.Headers.1.Values v2 \
    --Trigger.EventTypes pushImage \
    --Trigger.Condition release* \
    --Trigger.Enabled True \
    --Trigger.Id 2 \
    --Trigger.Description desc22 \
    --Trigger.NamespaceId 1 \
    --Trigger.NamespaceName ns1 \
    --Namespace ns1
```

Output: 
```
{
    "Response": {
        "RequestId": "cadb3e9c-6f00-4d20-9688-23e0fa792624"
    }
}
```

