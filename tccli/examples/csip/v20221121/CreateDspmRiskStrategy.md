**Example 1: 创建Dspm自定义风险策略**



Input: 

```
tccli csip CreateDspmRiskStrategy --cli-unfold-argument  \
    --Name 自定义SQL注入审计规则 \
    --Rule {"RuleType":1,"Fields":[{"Key":"SqlText","Operator":"contains","Value":"sleep("}],"RuleIdentifier":"CustomSqlInjection","SaveToDb":true} \
    --RiskLevel High \
    --IsEnabled 1 \
    --RiskType alarm \
    --StrategyCategory SQLOperationAnomaly
```

Output: 
```
{
    "Response": {
        "StrategyId": "190001",
        "StrategyType": "CustomAudit_8f6b5b0c2c1b4bb7a1e4bcb828c97a6a",
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

