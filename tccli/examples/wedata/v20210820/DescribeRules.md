**Example 1: 查询质量规则列表**

{
  "ProjectId": "abc",
  "RuleGroupId": 1,
  "EngineType":"HIVE"
}

Input: 

```
tccli wedata DescribeRules --cli-unfold-argument  \
    --ProjectId abc \
    --RuleGroupId 1 \
    --EngineType HIVE
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RuleId": 1,
                "RuleGroupId": 1,
                "TableId": "abc",
                "Name": "abc",
                "Type": 1,
                "RuleTemplateId": 1,
                "RuleTemplateContent": "abc",
                "QualityDim": 1,
                "SourceObjectType": 1,
                "SourceObjectDataType": 1,
                "SourceObjectDataTypeName": "abc",
                "SourceObjectValue": "abc",
                "ConditionType": 1,
                "ConditionExpression": "abc",
                "CustomSql": "abc",
                "CompareRule": {
                    "Items": [
                        {
                            "CompareType": 1,
                            "Operator": "abc",
                            "ValueComputeType": 1,
                            "ValueList": [
                                {
                                    "ValueType": 1,
                                    "Value": "abc"
                                }
                            ]
                        }
                    ],
                    "CycleStep": 1
                },
                "AlarmLevel": 1,
                "Description": "abc",
                "Operator": "abc",
                "TargetDatabaseId": "abc",
                "TargetDatabaseName": "abc",
                "TargetTableId": "abc",
                "TargetTableName": "abc",
                "TargetConditionExpr": "abc",
                "RelConditionExpr": "abc",
                "FieldConfig": {
                    "WhereConfig": [
                        {
                            "FieldKey": "abc",
                            "FieldValue": "abc",
                            "FieldDataType": "abc"
                        }
                    ],
                    "TableConfig": [
                        {
                            "DatabaseId": "abc",
                            "DatabaseName": "abc",
                            "TableId": "abc",
                            "TableName": "abc",
                            "TableKey": "abc",
                            "FieldConfig": [
                                {
                                    "FieldKey": "abc",
                                    "FieldValue": "abc",
                                    "FieldDataType": "abc"
                                }
                            ]
                        }
                    ]
                },
                "MultiSourceFlag": true,
                "WhereFlag": true,
                "TemplateSql": "abc",
                "SubQualityDim": 1,
                "TargetObjectType": 1,
                "TargetObjectDataType": 1,
                "TargetObjectDataTypeName": "abc",
                "TargetObjectValue": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

