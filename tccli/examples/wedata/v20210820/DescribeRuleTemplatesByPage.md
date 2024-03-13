**Example 1: 规则模板列表**



Input: 

```
tccli wedata DescribeRuleTemplatesByPage --cli-unfold-argument  \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --PageNumber 1 \
    --PageSize 1 \
    --ProjectId abc
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
            ]
        },
        "RequestId": "abc"
    }
}
```

