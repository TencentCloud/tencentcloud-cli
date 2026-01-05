**Example 1: 分页查询规则模版**

分页查询规则模版

Input: 

```
tccli wedata ListQualityRuleTemplates --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CitationCount": 0,
                    "CompareType": 1,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "A common metric in machine learning used to monitor the shift in the distribution of a feature or model score over time.",
                    "MultiSourceFlag": false,
                    "Name": "Population Stability Index (PSI)",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "BASELINE_TABLE",
                            "FEATURE_COLUMN",
                            "BASELINE_DB"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6514,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 1,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "measures the minimum \"work\" required to transform one distribution into another. less sensitive to sharp changes in distribution shapes.",
                    "MultiSourceFlag": false,
                    "Name": "wasserstein distance",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "BASELINE_TABLE",
                            "FEATURE_COLUMN",
                            "BASELINE_DB"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6513,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 1,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "a symmetric and bounded measure of the similarity between two probability distributions, based on kl divergence. range is [0, 1].",
                    "MultiSourceFlag": false,
                    "Name": "jensen-shannon divergence",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "BASELINE_TABLE",
                            "FEATURE_COLUMN",
                            "BASELINE_DB"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6512,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 1,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "measures the maximum absolute difference between the two probability distributions at any point.",
                    "MultiSourceFlag": false,
                    "Name": "l-infinity distance",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "BASELINE_TABLE",
                            "FEATURE_COLUMN",
                            "BASELINE_DB"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6511,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 1,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "measures the largest possible difference between the probabilities that two distributions can assign to the same event.",
                    "MultiSourceFlag": false,
                    "Name": "total variation distance",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "BASELINE_TABLE",
                            "FEATURE_COLUMN",
                            "BASELINE_DB"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6510,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 1,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "used to test if two one-dimensional continuous probability distributions differ significantly.",
                    "MultiSourceFlag": false,
                    "Name": "kolmogorov-smirnov test (ks test)",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "BASELINE_TABLE",
                            "FEATURE_COLUMN",
                            "BASELINE_DB"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6509,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 1,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "used to test if there is a significant difference between two categorical distributions.",
                    "MultiSourceFlag": false,
                    "Name": "chi-squared test",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "BASELINE_TABLE",
                            "FEATURE_COLUMN",
                            "BASELINE_DB"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6508,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 7,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "requires that the probability of receiving a positive outcome is equal across different groups.",
                    "MultiSourceFlag": false,
                    "Name": "statistical parity",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "PROTECTION_VALUE",
                            "COMPARISON_COLUMN",
                            "PREDICTION_COLUMN",
                            "POSITIVE_VALUE"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6507,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 7,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "requires that the true positive rate (recall) is equal across different groups.",
                    "MultiSourceFlag": false,
                    "Name": "equal opportunity",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "PROTECTION_VALUE",
                            "COMPARISON_COLUMN",
                            "PREDICTION_COLUMN",
                            "LABEL_COLUMN",
                            "POSITIVE_VALUE"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6506,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": 0,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                },
                {
                    "CitationCount": 0,
                    "CompareType": 7,
                    "DatasourceTypes": [
                        2,
                        3
                    ],
                    "Description": "requires that the false positive rate (fpr) is equal across different groups.",
                    "MultiSourceFlag": false,
                    "Name": "predictive equality",
                    "QualityDim": 1,
                    "ResolvedSqlExpression": {
                        "ParamExpressions": null,
                        "SystemTemplateExpressions": [
                            "PROTECTION_VALUE",
                            "COMPARISON_COLUMN",
                            "PREDICTION_COLUMN",
                            "LABEL_COLUMN",
                            "POSITIVE_VALUE"
                        ],
                        "TableExpressions": null
                    },
                    "RuleTemplateId": 6505,
                    "SourceContent": null,
                    "SourceEngineTypes": [
                        2,
                        4,
                        16
                    ],
                    "SourceObjectDataType": 3,
                    "SourceObjectType": 2,
                    "SqlExpression": null,
                    "SubQualityDim": null,
                    "Type": 1,
                    "UpdateTime": null,
                    "UserId": 1,
                    "UserIdStr": null,
                    "UserName": null,
                    "WhereFlag": false
                }
            ],
            "TotalCount": 180
        },
        "RequestId": "40900661-28b4-4126-8023-0d4247a5194d"
    }
}
```

