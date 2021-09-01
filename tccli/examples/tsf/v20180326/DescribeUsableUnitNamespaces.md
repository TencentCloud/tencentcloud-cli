**Example 1: 查询可用于被导入的命名空间列表**



Input: 

```
tccli tsf DescribeUsableUnitNamespaces --cli-unfold-argument ```

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

