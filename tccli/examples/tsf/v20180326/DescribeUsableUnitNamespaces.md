**Example 1: 查询可用于被导入的命名空间列表**



Input: 

```
tccli tsf DescribeUsableUnitNamespaces --cli-unfold-argument  \
    --SearchWord container \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "8d5c97b6-73fb-4fa5-8648-4ebf8b3b9551",
        "Result": {
            "Content": [
                {
                    "CreatedTime": "2025",
                    "GatewayInstanceId": "instance-id",
                    "Id": "id",
                    "NamespaceId": "namespace-ygo3djma",
                    "NamespaceName": "cluster-container-jolyonzheng_default",
                    "UpdatedTime": "2025"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

