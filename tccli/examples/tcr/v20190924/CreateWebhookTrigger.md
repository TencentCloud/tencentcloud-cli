**Example 1: 创建触发器**

创建触发器

Input: 

```
tccli tcr CreateWebhookTrigger --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --Trigger.Id 5 \
    --Trigger.Name trigger5 \
    --Trigger.Description desc \
    --Trigger.Targets.0.Address http://www.baidu.com \
    --Trigger.Targets.0.Headers.0.Key k1 \
    --Trigger.Targets.0.Headers.0.Values v1 \
    --Trigger.Targets.0.Headers.1.Key k2 \
    --Trigger.Targets.0.Headers.1.Values v2 \
    --Trigger.EventTypes pushImage uploadChart \
    --Trigger.Condition golang \
    --Trigger.Enabled True \
    --Trigger.NamespaceId 5 \
    --Trigger.NamespaceName ns \
    --Namespace ns
```

Output: 
```
{
    "Response": {
        "RequestId": "ee7ae0ad-4a6f-4b71-8566-7f3e6a624fce",
        "Trigger": {
            "Condition": "golang",
            "Description": "desc",
            "Enabled": true,
            "EventTypes": [
                "pushImage",
                "uploadChart"
            ],
            "Id": 6,
            "Name": "trigger5",
            "NamespaceId": 5,
            "Targets": [
                {
                    "Address": "http://www.baidu.com",
                    "Headers": [
                        {
                            "Key": "k1",
                            "Values": [
                                "v1"
                            ]
                        },
                        {
                            "Key": "k2",
                            "Values": [
                                "v2"
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
```

