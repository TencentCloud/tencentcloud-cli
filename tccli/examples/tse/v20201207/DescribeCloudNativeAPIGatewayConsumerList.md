**Example 1: 查询消费者列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayConsumerList --cli-unfold-argument  \
    --GatewayId gateway-c67671ec \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "Consumers": [
                {
                    "ConsumerId": "50240110-fe3e-4cab-bd99-b9f37d330c2f",
                    "CreateTime": "2026-04-30 11:49:52",
                    "Description": "",
                    "ModifyTime": "2026-04-30 11:49:52",
                    "Name": "**********"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "bdd74c6e-bd30-4583-a979-0f23477c825f"
    }
}
```

