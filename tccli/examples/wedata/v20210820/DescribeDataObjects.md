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
                "SourceObjectValue": "xx",
                "SourceObjectDataTypeName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

