**Example 1: 获取消费者列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayConsumerList --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1064a23d-68f6-4e0b-8205-33d341f0026b",
        "Result": {
            "Consumers": [
                {
                    "ConsumerId": "c31f5dd7-eab5-4e77-ac18-31add3c94a9d",
                    "CreateTime": "2025-11-19 16:58:43",
                    "Description": "消费者1",
                    "ModifyTime": "2025-11-19 16:58:43",
                    "Name": "消费者1"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

