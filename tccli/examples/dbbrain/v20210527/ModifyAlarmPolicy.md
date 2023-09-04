**Example 1: 增加实例**

修改策略

Input: 

```
tccli dbbrain ModifyAlarmPolicy --cli-unfold-argument  \
    --ApplyType instance \
    --Enable 1 \
    --InstanceIds.0.InstanceId cdb-k9p7oscf \
    --InstanceIds.1.InstanceId cdb-5jqzedc \
    --NewProfileLevel Instance \
    --NewProfileName test \
    --ProfileName test \
    --ProfileType alarm_policy \
    --Remark test \
    --RuleType 0 \
    --QuickRule fatal \
    --TemplateInfo.0.TemplateId 23002 \
    --TemplateInfo.0.TemplateName ada测试
```

Output: 
```
{
    "Response": {
        "RequestId": "08baa278-1104-4d3a-8585-027cc511d300"
    }
}
```

