**Example 1: 创建质量检测规则**



Input: 

```
tccli wedata CreateQualityRule --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --CreateRuleScene 1 \
    --RuleBOList.0.Name new_rule_5 \
    --RuleBOList.0.Type 1 \
    --RuleBOList.0.RuleGroupId 727 \
    --RuleBOList.0.RuleTemplateId 6142 \
    --RuleBOList.0.SourceObjectDataTypeName table \
    --RuleBOList.0.SourceObjectValue 表 \
    --RuleBOList.0.ConditionType 1 \
    --RuleBOList.0.CompareRule.Items.0.CompareType 1 \
    --RuleBOList.0.CompareRule.Items.0.Operator <= \
    --RuleBOList.0.CompareRule.Items.0.ValueList.0.ValueType 3 \
    --RuleBOList.0.CompareRule.Items.0.ValueList.0.Value 10 \
    --RuleBOList.0.CompareRule.ComputeExpression 0 \
    --RuleBOList.0.AlarmLevel 2 \
    --RuleBOList.0.Description row count \
    --RuleBOList.0.DatasourceId 8860 \
    --RuleBOList.0.SourceEngineTypes 16 \
    --RuleBOList.0.Index 50464ee-6775-7037-4e0a-c02ae7baf8d \
    --RuleBOList.0.DatabaseName at_dlc_cloud_gz_prod_mc \
    --RuleBOList.0.TableName gee01 \
    --RuleBOList.0.CatalogName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailedCount": 0,
            "Msg": "共配置1条规则，其中1条生成成功，0条生成失败",
            "Results": [
                {
                    "Msg": null,
                    "Name": "new_rule_5",
                    "RuleGroupId": 727,
                    "RuleGroupTableId": 328,
                    "RuleId": 1079,
                    "Success": true
                }
            ],
            "SuccessCount": 1,
            "SuccessRuleIds": [
                1079
            ],
            "SumCount": 1
        },
        "RequestId": "e8cda1dc-d78f-419a-8653-8295a5e1eb0d"
    }
}
```

