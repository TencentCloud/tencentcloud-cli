**Example 1: 创建质量规则接口**



Input: 

```
tccli wedata CreateRule --cli-unfold-argument  \
    --FieldConfig.WhereConfig.0.FieldKey xx \
    --FieldConfig.WhereConfig.0.FieldValue xx \
    --FieldConfig.TableConfig.0.DatabaseId xx \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldKey xx \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldValue xx \
    --FieldConfig.TableConfig.0.TableName xx \
    --FieldConfig.TableConfig.0.TableId xx \
    --FieldConfig.TableConfig.0.DatabaseName xx \
    --FieldConfig.TableConfig.0.TableKey xx \
    --ConditionExpression xx \
    --DatabaseId xx \
    --QualityDim 1 \
    --TableId xx \
    --TargetTableId xx \
    --Type 1 \
    --CustomSql xx \
    --Name xx \
    --Description xx \
    --TargetDatabaseId xx \
    --TargetObjectValue xx \
    --ConditionType 1 \
    --RelConditionExpr xx \
    --ProjectId xx \
    --TargetConditionExpr xx \
    --CompareRule.Items.0.Operator xx \
    --CompareRule.Items.0.ValueComputeType 1 \
    --CompareRule.Items.0.ValueList.0.ValueType 1 \
    --CompareRule.Items.0.ValueList.0.Value xx \
    --CompareRule.Items.0.CompareType 1 \
    --RuleTemplateId 1 \
    --DatasourceId xx \
    --SourceObjectDataTypeName xx \
    --RuleGroupId 1 \
    --SourceObjectValue xx \
    --AlarmLevel 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CompareRule": {
                "Items": [
                    {
                        "Operator": "xx",
                        "ValueComputeType": 1,
                        "ValueList": [
                            {
                                "ValueType": 1,
                                "Value": "xx"
                            }
                        ],
                        "CompareType": 1
                    }
                ]
            },
            "ConditionType": 1,
            "RuleTemplateContent": "xx",
            "Name": "xx",
            "RuleGroupId": 1,
            "SourceObjectDataType": 1,
            "RuleId": 1,
            "AlarmLevel": 1,
            "SourceObjectValue": "xx",
            "RuleTemplateId": 1,
            "SourceObjectDataTypeName": "xx",
            "TableId": "xx",
            "CustomSql": "xx",
            "Operator": "xx",
            "Description": "xx",
            "Type": 1,
            "ConditionExpression": "xx",
            "SourceObjectType": 1,
            "QualityDim": 1
        },
        "RequestId": "xx"
    }
}
```

