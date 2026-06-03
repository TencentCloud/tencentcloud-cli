**Example 1: 查询消费者分组列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayConsumerGroupList --cli-unfold-argument  \
    --GatewayId gateway-c67671ec \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ConsumerGroups": [
                {
                    "BindCount": 1,
                    "ConsumerGroupId": "cg-200bac0a61cd4c",
                    "CreateTime": "2026-04-16 19:08:18",
                    "Description": "Default consumer group created by the system",
                    "ModifyTime": "2026-04-16 19:08:18",
                    "Name": "default-consumer-group",
                    "Status": "Enable"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "3dfde9ac-42a6-4982-9a58-d5b4f5b1b0d4"
    }
}
```

