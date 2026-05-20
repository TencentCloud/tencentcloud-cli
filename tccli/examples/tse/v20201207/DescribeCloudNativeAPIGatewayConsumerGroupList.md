**Example 1: 根据分组id模糊查询**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayConsumerGroupList --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "2478e2b2-e9a4-44cd-b958-419e0a809158",
        "Result": {
            "ConsumerGroups": [
                {
                    "ConsumerGroupId": "cg-2cd91a00",
                    "CreateTime": "2025-11-20 09:13:16",
                    "Description": "分组描述",
                    "ModifyTime": "2025-11-20 09:13:16",
                    "Name": "分组1",
                    "Status": "Enable",
                    "BindCount": 0
                }
            ],
            "TotalCount": 1
        }
    }
}
```

