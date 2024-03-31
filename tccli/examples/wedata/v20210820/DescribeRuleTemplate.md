**Example 1: 查询模板详情**

查询模板详情

Input: 

```
tccli wedata DescribeRuleTemplate --cli-unfold-argument  \
    --ProjectId 567890 \
    --TemplateId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleTemplateId": 1,
            "Name": "abc",
            "Description": "描述",
            "Type": 1,
            "SourceObjectType": 1,
            "SourceObjectDataType": 1,
            "SourceContent": "abc",
            "SourceEngineTypes": [
                1
            ],
            "QualityDim": 1,
            "CompareType": 1,
            "CitationCount": 1,
            "UserId": 1,
            "UserName": "zahgnsan",
            "UpdateTime": "2023-10-01",
            "WhereFlag": true,
            "MultiSourceFlag": true,
            "SqlExpression": "sql",
            "SubQualityDim": 1,
            "ResolvedSqlExpression": {
                "TableExpressions": [
                    {
                        "TableExpression": "expr",
                        "ColumnExpression": [
                            "expr"
                        ]
                    }
                ],
                "ParamExpressions": [
                    "exp"
                ]
            },
            "DatasourceTypes": [
                0
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

