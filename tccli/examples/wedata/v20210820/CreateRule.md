**Example 1: 创建质量规则接口**

创建质量规则组中单个规则

Input: 

```
tccli wedata CreateRule --cli-unfold-argument  \
    --ProjectId abc \
    --RuleGroupId 1 \
    --Name abc \
    --TableId abc \
    --RuleTemplateId 1 \
    --Type 1 \
    --QualityDim 1 \
    --SourceObjectDataTypeName abc \
    --SourceObjectValue abc \
    --ConditionType 1 \
    --ConditionExpression abc \
    --CustomSql abc \
    --CompareRule.Items.0.CompareType 1 \
    --CompareRule.Items.0.Operator abc \
    --CompareRule.Items.0.ValueComputeType 1 \
    --CompareRule.Items.0.ValueList.0.ValueType 1 \
    --CompareRule.Items.0.ValueList.0.Value abc \
    --CompareRule.CycleStep 1 \
    --AlarmLevel 1 \
    --Description abc \
    --DatasourceId abc \
    --DatabaseId abc \
    --TargetDatabaseId abc \
    --TargetTableId abc \
    --TargetConditionExpr abc \
    --RelConditionExpr abc \
    --FieldConfig.WhereConfig.0.FieldKey abc \
    --FieldConfig.WhereConfig.0.FieldValue abc \
    --FieldConfig.WhereConfig.0.FieldDataType abc \
    --FieldConfig.TableConfig.0.DatabaseId abc \
    --FieldConfig.TableConfig.0.DatabaseName abc \
    --FieldConfig.TableConfig.0.TableId abc \
    --FieldConfig.TableConfig.0.TableName abc \
    --FieldConfig.TableConfig.0.TableKey abc \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldKey abc \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldValue abc \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldDataType abc \
    --TargetObjectValue abc \
    --SourceEngineTypes 1
```

Output: 
```
{
    "Response": {
        "Data": {
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
        },
        "RequestId": "abc"
    }
}
```

