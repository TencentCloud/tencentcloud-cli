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
                "Name": "表行数",
                "Description": "描述",
                "Type": 1,
                "SourceObjectType": 1,
                "SourceObjectDataType": 1,
                "SourceContent": "",
                "SourceEngineTypes": [
                    2
                ],
                "QualityDim": 1,
                "CompareType": 1,
                "CitationCount": 1,
                "UserId": 1,
                "UserName": "zahgnsan",
                "UpdateTime": "2023-10-01",
                "WhereFlag": true,
                "MultiSourceFlag": true,
                "SqlExpression": "select count(*) from table",
                "SubQualityDim": 1,
                "ResolvedSqlExpression": {
                    "TableExpressions": [
                        {
                            "TableExpression": "table_2.column_2",
                            "ColumnExpression": [
                                "column_1"
                            ]
                        }
                    ],
                    "ParamExpressions": [
                        "param_1"
                    ]
                },
                "DatasourceTypes": [
                    2
                ]
            }
        ],
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

