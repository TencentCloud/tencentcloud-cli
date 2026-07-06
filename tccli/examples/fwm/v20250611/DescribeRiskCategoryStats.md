**Example 1: 查询策略体检风险分类统计数据**



Input: 

```
tccli fwm DescribeRiskCategoryStats --cli-unfold-argument  \
    --Product enterprise_sg \
    --MemberId mem-1300846651-100011616646
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CategoryId": "deviate_baseline",
                "CategoryName": "安全基线偏离规则",
                "Description": "检测到入向全放行规则，范围过大",
                "DisposalRate": 0,
                "HasRisk": 1,
                "IgnoredCount": 0,
                "RemediationStatus": "Incomplete",
                "RiskLevel": 2,
                "RiskLevelName": "高危",
                "RuleCount": 1,
                "SubcategoryId": "inbound_accept_any",
                "SubcategoryName": "入向全放行规则",
                "Suggestion": "检测到入向全放行规则，范围过大。建议根据业务实际需求调整规则，缩小覆盖范围以提升规则精准度。",
                "TreatedCount": 0,
                "UntreatedCount": 1
            },
            {
                "CategoryId": "invalid_rule",
                "CategoryName": "无效规则",
                "Description": "规则关联的资产实例、地址模板、资源标签等模板已被部分或全部删除",
                "DisposalRate": 0,
                "HasRisk": 1,
                "IgnoredCount": 0,
                "RemediationStatus": "Incomplete",
                "RiskLevel": 2,
                "RiskLevelName": "高危",
                "RuleCount": 1,
                "SubcategoryId": "loss_of_effect_rules",
                "SubcategoryName": "失效规则",
                "Suggestion": "检测到规则关联的资产实例、地址模板、或资源标签等模板已被部分删除。建议直接删除该无效规则。",
                "TreatedCount": 0,
                "UntreatedCount": 1
            },
            {
                "CategoryId": "invalid_rule",
                "CategoryName": "无效规则",
                "Description": "规则已被优先级更高的规则覆盖",
                "DisposalRate": 0,
                "HasRisk": 1,
                "IgnoredCount": 0,
                "RemediationStatus": "Incomplete",
                "RiskLevel": 0,
                "RiskLevelName": "低危",
                "RuleCount": 2,
                "SubcategoryId": "overridden_rules",
                "SubcategoryName": "被高优覆盖规则",
                "Suggestion": "检测到规则已被优先级更高的规则覆盖。建议删除被覆盖的无效规则。",
                "TreatedCount": 0,
                "UntreatedCount": 2
            }
        ],
        "RequestId": "11a97c77-9c0e-468f-b6a2-02b38c121322",
        "Total": 2
    }
}
```

