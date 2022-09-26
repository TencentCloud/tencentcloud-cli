**Example 1: 查询触发器**



Input: 

```
tccli tcr DescribeWebhookTrigger --cli-unfold-argument  \
    --Limit 1 \
    --Namespace someNs \
    --RegistryId tcr-7s2d14fn
```

Output: 
```
{
    "Response": {
        "RequestId": "d7549286-ffb6-486c-98b6-30a4001da260",
        "TotalCount": 130,
        "Triggers": [
            {
                "Id": 152,
                "Name": "someTrigger",
                "Description": "触发器描述",
                "Targets": [
                    {
                        "Address": "http://httpbin.org/post",
                        "Headers": [
                            {
                                "Key": "X-Header1",
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
        ]
    }
}
```

