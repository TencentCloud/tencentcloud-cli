**Example 1: 查询用户所有规则的策略问题**



Input: 

```
tccli fwm DescribeRiskList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Product enterprise_sg \
    --MemberId mem-1300846651-100011616646
```

Output: 
```
{
    "Response": {
        "PolicyRiskLst": [
            {
                "Direction": "Egress",
                "DisposalTime": "",
                "FoundTime": "2026-03-04 17:36:12",
                "Id": "06c15d97ec325e8e5fe6f10883478360",
                "Product": "enterprise_sg",
                "RiskCategory": "deviate_baseline",
                "RiskFeature": "inbound_accept_any",
                "RiskLevel": 2,
                "RiskReason": "108275允许入站任意访问，范围过大",
                "RiskSubCategory": "inbound_accept_any",
                "RuleCount": 1,
                "RuleType": "ACCEPT",
                "SgId": [
                    ""
                ],
                "SgRuleId": [
                    "108275"
                ],
                "Status": 0,
                "Suggestion": "检测到入向全放行规则，范围过大。建议根据业务实际需求调整规则，缩小覆盖范围以提升规则精准度。"
            },
            {
                "Direction": "Egress",
                "DisposalTime": "",
                "FoundTime": "2026-03-02 22:22:33",
                "Id": "a10b189d0974f4f1b4f04fc98187fc4d",
                "Product": "enterprise_sg",
                "RiskCategory": "invalid_rule",
                "RiskFeature": "loss_of_effect_rules",
                "RiskLevel": 2,
                "RiskReason": "",
                "RiskSubCategory": "loss_of_effect_rules",
                "RuleCount": 1,
                "RuleType": "ACCEPT",
                "SgId": [
                    ""
                ],
                "SgRuleId": [
                    "164108"
                ],
                "Status": 0,
                "Suggestion": "检测到规则关联的资产实例、地址模板、或资源标签模板已被部分删除。建议直接删除该无效规则。"
            },
            {
                "Direction": "Egress",
                "DisposalTime": "",
                "FoundTime": "2026-03-04 17:58:46",
                "Id": "c987cf88c6c0de2702f06530a0070564",
                "Product": "enterprise_sg",
                "RiskCategory": "invalid_rule",
                "RiskFeature": "overridden_rules_by:108275",
                "RiskLevel": 0,
                "RiskReason": "规则（允许 ::/0 -> 2400:ee00:101c:5701:0:9d35:c8f9:d41f:ANY(ANY)）覆盖了1条低优先级规则",
                "RiskSubCategory": "overridden_rules",
                "RuleCount": 2,
                "RuleType": "ACCEPT",
                "SgId": [
                    ""
                ],
                "SgRuleId": [
                    "108275",
                    "108276"
                ],
                "Status": 0,
                "Suggestion": "检测到规则已被优先级更高的规则覆盖。建议删除被覆盖的无效规则。"
            }
        ],
        "RequestId": "ba338963-595a-4d8b-b630-2b646cb97be1",
        "Total": 3
    }
}
```

