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
                "SourceContent": "abc",
                "SourceEngineTypes": [
                    1
                ],
                "QualityDim": 1,
                "CompareType": 1,
                "CitationCount": 1,
                "UserId": 1,
                "UserName": "abc",
                "UpdateTime": "abc",
                "WhereFlag": true,
                "MultiSourceFlag": true,
                "SqlExpression": "abc",
                "SubQualityDim": 1,
                "ResolvedSqlExpression": {
                    "TableExpressions": [
                        {
                            "TableExpression": "abc",
                            "ColumnExpression": [
                                "abc"
                            ]
                        }
                    ],
                    "ParamExpressions": [
                        "abc"
                    ]
                },
                "DatasourceTypes": [
                    0
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

