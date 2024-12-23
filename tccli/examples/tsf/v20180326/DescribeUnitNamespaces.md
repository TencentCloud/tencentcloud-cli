**Example 1: 查询单元化命名空间列表**



Input: 

```
tccli tsf DescribeUnitNamespaces --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-szesmg28 \
    --SearchWord global \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "cc6f37b7-9847-4c25-a438-b85289e2f977",
        "Result": {
            "Content": [
                {
                    "CreatedTime": "2023-01-10 17:27:55",
                    "GatewayInstanceId": "gw-ins-szesmg28",
                    "Id": "unit-ns-n7n178c3",
                    "NamespaceId": "namespace-vk5blxnv",
                    "NamespaceName": "global_default",
                    "UpdatedTime": "2023-01-10 17:27:55"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

