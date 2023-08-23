**Example 1: 批量查看资源关联的标签（计费）**

批量查看资源关联的标签（计费）

Input: 

```
tccli tag DescribeResourceTagsByResourceIdsForBill --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourcePrefix instance \
    --ResourceIds test-1234
```

Output: 
```
{
    "Response": {
        "Limit": 15,
        "Offset": 0,
        "RequestId": "b4fb34f9-83ea-4948-850e-480e47cf9a11",
        "Tags": [
            {
                "Region": "ap-guangzhou",
                "ResourceId": "vpc-1234",
                "TagKey": "testKey",
                "TagKeyMd5": "c0751bd838918952b086812599b4f2e2",
                "TagValue": "testValue",
                "TagValueMd5": "123fa27d4bf6a6787faebd41f199aa2a",
                "UpdateTime": "2023-08-01 11:50:00"
            }
        ],
        "TotalCount": 1
    }
}
```

