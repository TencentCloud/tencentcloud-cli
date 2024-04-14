**Example 1: 更新质量规则接口**

更新质量规则接口

Input: 

```
tccli wedata ModifyRule --cli-unfold-argument  \
    --ProjectId 1234 \
    --RuleId 1 \
    --RuleGroupId 1 \
    --Name 规则1 \
    --TableId 867ujhn8i3240eif \
    --RuleTemplateId 1 \
    --Type 1 \
    --QualityDim 1 \
    --SourceObjectDataTypeName int \
    --SourceObjectValue name \
    --ConditionType 1 \
    --ConditionExpression >0 \
    --CustomSql abc \
    --CompareRule.Items.0.CompareType 1 \
    --CompareRule.Items.0.Operator < \
    --CompareRule.Items.0.ValueComputeType 1 \
    --CompareRule.Items.0.ValueList.0.ValueType 1 \
    --CompareRule.Items.0.ValueList.0.Value 10 \
    --CompareRule.CycleStep 1 \
    --AlarmLevel 1 \
    --Description 规则1 \
    --TargetDatabaseId 97yghbj9ik \
    --TargetTableId 56yujhr57ftuvgjb 78u \
    --TargetConditionExpr ct='${yyyy-mm-dd-1}' \
    --RelConditionExpr sourceTable.id=targetTable.id \
    --FieldConfig.WhereConfig.0.FieldKey param_1 \
    --FieldConfig.WhereConfig.0.FieldValue 10 \
    --FieldConfig.WhereConfig.0.FieldDataType id \
    --FieldConfig.TableConfig.0.DatabaseId 78ughibj8t6ygihb \
    --FieldConfig.TableConfig.0.DatabaseName dbName \
    --FieldConfig.TableConfig.0.TableId 8iuyhbf2we9fu \
    --FieldConfig.TableConfig.0.TableName test \
    --FieldConfig.TableConfig.0.TableKey table_1 \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldKey table_1.column_1 \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldValue id \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldDataType int \
    --TargetObjectValue 表 \
    --SourceEngineTypes 1
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

