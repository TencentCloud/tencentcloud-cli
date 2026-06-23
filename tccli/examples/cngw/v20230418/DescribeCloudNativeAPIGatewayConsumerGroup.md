**Example 1: 查询分组详情**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayConsumerGroup --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --ConsumerGroupId cg-2cd91a00
```

Output: 
```
{
    "Response": {
        "RequestId": "0379d5e4-6a1e-4baf-bb92-6cd11cbe197a",
        "Result": {
            "ConsumerGroupId": "cg-2cd91a00",
            "CreateTime": "2025-11-11 11:11:11",
            "Description": "分组描述",
            "ModifyTime": "2025-11-11 11:11:11",
            "Name": "分组1",
            "Status": "Enable"
        }
    }
}
```

