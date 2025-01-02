**Example 1: 查询触发器**



Input: 

```
tccli tcr DescribeWebhookTrigger --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --Limit 10 \
    --Offset 1 \
    --Namespace ns1
```

Output: 
```
{
    "Response": {
        "RequestId": "ca34c717-aba2-4307-a897-193343d10f39",
        "TotalCount": 1,
        "Triggers": [
            {
                "Condition": "golang",
                "Description": "",
                "Enabled": true,
                "EventTypes": [
                    "pushImage"
                ],
                "Id": 2,
                "Name": "tirgger",
                "NamespaceId": 1,
                "Targets": [
                    {
                        "Address": "http://www.baidu.com",
                        "Headers": [
                            {
                                "Key": "",
                                "Values": [
                                    "undefined"
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

