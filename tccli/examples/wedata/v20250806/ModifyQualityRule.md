**Example 1: 修改规则示例**

修改规则示例

Input: 

```
tccli wedata ModifyQualityRule --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --RuleId 1069 \
    --RuleGroupId 731 \
    --Name autotest_s3mCmodify \
    --TableId E-UEBWQB-XRjERluUg \
    --RuleTemplateId 54 \
    --Type 1 \
    --QualityDim 1 \
    --SourceObjectDataTypeName int \
    --SourceObjectValue age \
    --ConditionType 1 \
    --ConditionExpression pt=substring('${yyyyMMddHHmmss-1H}',1,10) \
    --CompareRule.Items.0.CompareType 1 \
    --CompareRule.Items.0.Operator > \
    --CompareRule.Items.0.ValueComputeType 1 \
    --CompareRule.Items.0.ValueList.0.ValueType 3 \
    --CompareRule.Items.0.ValueList.0.Value 0 \
    --CompareRule.CycleStep 1 \
    --CompareRule.ComputeExpression 0 \
    --AlarmLevel 1 \
    --Description 规则 \
    --TargetDatabaseId 97yuhijbkh08y97uhi \
    --TargetTableId E-UEBWQB-XRjERluUg \
    --TargetConditionExpr ct='${yyyy-mm-dd-1}' \
    --RelConditionExpr sourceTable.id=targetTable.id \
    --FieldConfig.WhereConfig.0.FieldKey param_1 \
    --FieldConfig.WhereConfig.0.FieldValue id \
    --FieldConfig.WhereConfig.0.FieldDataType int \
    --FieldConfig.TableConfig.0.DatabaseId NW0VL_YYPESvi8w \
    --FieldConfig.TableConfig.0.DatabaseName default \
    --FieldConfig.TableConfig.0.TableId EHdPET2IKQ2KBhGw \
    --FieldConfig.TableConfig.0.TableName dq_student \
    --FieldConfig.TableConfig.0.TableKey table_1 \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldKey table_1.column_1 \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldValue id \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldDataType int \
    --TargetObjectValue value \
    --SourceEngineTypes 2 4
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "9fd96539-4745-4e36-bf6d-f4b7a6d722a4"
    }
}
```

