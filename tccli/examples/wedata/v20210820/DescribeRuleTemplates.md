**Example 1: 查询规则模板列表**



Input: 

```
tccli wedata DescribeRuleTemplates --cli-unfold-argument  \
    --Type 1 \
    --SourceObjectType 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RuleTemplateId": 1,
                "Name": "abc",
                "Description": "abc",
                "Type": 1,
                "SourceObjectType": 1,
                "SourceObjectDataType": 1,
                "SourceContent": "content",
                "SourceEngineTypes": [
                    1
                ],
                "QualityDim": 1,
                "CompareType": 1,
                "CitationCount": 1,
                "UserId": 1,
                "UserName": "zhangsan",
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
                        "expr"
                    ]
                },
                "DatasourceTypes": [
                    0
                ]
            }
        ],
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

