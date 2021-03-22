**Example 1: 查询单元化命名空间列表**



Input: 

```
tccli tsf DescribeUnitNamespaces --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-afsfas
```

Output: 
```
{
    "Response": {
        "RequestId": "efa09114-e0c3-43ec-8347-5f4454696c61",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "Id": "gw-xxxxxxx",
                    "NamespaceId": "test",
                    "NamespaceName": "”DASD“"
                }
            ]
        }
    }
}
```

