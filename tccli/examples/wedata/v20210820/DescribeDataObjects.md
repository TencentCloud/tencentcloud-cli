**Example 1: 查询规则组数据对象列表**



Input: 

```
tccli wedata DescribeDataObjects --cli-unfold-argument  \
    --ProjectId 1 \
    --TableId 1 \
    --DatasourceId 1 \
    --RuleGroupId 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "SourceObjectDataTypeName": "int",
                "SourceObjectValue": "1",
                "ObjectDataTypeName": "abc",
                "ObjectValue": "1",
                "ObjectType": 1
            }
        ],
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

