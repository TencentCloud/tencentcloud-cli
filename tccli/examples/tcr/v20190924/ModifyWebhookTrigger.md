**Example 1: 更新触发器**



Input: 

```
tccli tcr ModifyWebhookTrigger --cli-unfold-argument  \
    --RegistryId tcr-7s2d14fn \
    --Namespace someNs \
    --Trigger.Id 9 \
    --Trigger.Enabled false \
    --Trigger.Targets.0.Address abc.local \
    --Trigger.EventTypes pullImage
```

Output: 
```
{
    "Response": {
        "RequestId": "3c33da0e-5a85-4fdc-841c-5ca47454a117"
    }
}
```

