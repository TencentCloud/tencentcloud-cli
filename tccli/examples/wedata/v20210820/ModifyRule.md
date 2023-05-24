**Example 1: 更新质量规则接口**

更新质量规则接口

Input: 

```
tccli wedata ModifyRule --cli-unfold-argument  \
    --ProjectId abc \
    --RuleId 1 \
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
        "Data": true,
        "RequestId": "abc"
    }
}
```

