**Example 1: 更新质量规则接口**



Input: 

```
tccli wedata ModifyRule --cli-unfold-argument  \
    --FieldConfig.TableConfig xx \
    --ConditionExpression xx \
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
    --SourceObjectDataTypeName xx \
    --RuleGroupId 1 \
    --RuleId 1 \
    --SourceObjectValue xx \
    --AlarmLevel 1
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```

