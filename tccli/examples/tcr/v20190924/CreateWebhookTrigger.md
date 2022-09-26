**Example 1: 创建触发器**

创建触发器

Input: 

```
tccli tcr CreateWebhookTrigger --cli-unfold-argument  \
    --Namespace someNs \
    --Trigger.Name sometrigger \
    --Trigger.Enabled true \
    --Trigger.EventTypes pullImage \
    --Trigger.Targets.0.Headers.0.Values abc \
    --Trigger.Targets.0.Headers.0.Key X-Custom-Header \
    --Trigger.Targets.0.Address http://httpbin.org/post \
    --Trigger.Condition .* \
    --Trigger.Description 触发器描述 \
    --RegistryId tcr-7s2d14fn
```

Output: 
```
{
    "Response": {
        "RequestId": "6942d117-55bb-4aad-9ed0-af8fd4664402",
        "Trigger": {
            "Id": 20,
            "Name": "sometrigger",
            "NamespaceId": 30,
            "Description": "触发器描述",
            "Targets": [
                {
                    "Address": "http://httpbin.org/post",
                    "Headers": [
                        {
                            "Key": "X-Custom-Header",
                            "Values": [
                                "abc"
                            ]
                        }
                    ]
                }
            ],
            "EventTypes": [
                "pullImage"
            ],
            "Enabled": true,
            "Condition": ".*"
        }
    }
}
```

