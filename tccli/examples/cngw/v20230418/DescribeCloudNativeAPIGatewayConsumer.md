**Example 1: 查看详情**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayConsumer --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --ConsumerId c31f5dd7-eab5-4e77-ac18-31add3c94a9d
```

Output: 
```
{
    "Response": {
        "RequestId": "e6bfe546-a077-4935-905b-b97ba97fef2f",
        "Result": {
            "ConsumerGroups": [
                {
                    "ConsumerGroupId": "cg-5070cb47",
                    "CreateTime": "2025-11-20 09:53:12",
                    "Description": "分组描述",
                    "ModifyTime": "2025-11-20 09:53:12",
                    "Name": "分组3",
                    "Status": "Enable"
                },
                {
                    "ConsumerGroupId": "cg-6021c8b0",
                    "CreateTime": "2025-11-19 16:55:08",
                    "Description": "消费者分组描述",
                    "ModifyTime": "2025-11-20 10:26:35",
                    "Name": "消费者组",
                    "Status": "Disable"
                }
            ],
            "ConsumerId": "c31f5dd7-eab5-4e77-ac18-31add3c94a9d",
            "CreateTime": "2025-11-19 16:58:43",
            "Description": "消费者1",
            "ModifyTime": "2025-11-19 16:58:43",
            "Name": "消费者1"
        }
    }
}
```

