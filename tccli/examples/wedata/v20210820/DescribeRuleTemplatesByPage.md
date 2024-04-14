**Example 1: 规则模板列表**



Input: 

```
tccli wedata DescribeRuleTemplatesByPage --cli-unfold-argument  \
    --OrderFields.0.Name id \
    --OrderFields.0.Direction asc \
    --Filters.0.Name tableId \
    --Filters.0.Values t678yuh987tgui \
    --PageNumber 1 \
    --PageSize 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "RuleTemplateId": 1,
                    "Name": "规则1",
                    "Description": "描述",
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
                                "TableExpression": "table1",
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
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

