**Example 1: 创建合规包**

创建合规包

Input: 

```
tccli config AddCompliancePack --cli-unfold-argument  \
    --ConfigRules.0.Identifier sfc-function-settings-check \
    --ConfigRules.0.RuleName 函数计算中函数设置满足参数指定要求 \
    --ConfigRules.0.Description 函数计算中的函数设置满足参数指定的要求，视为“合规”。 \
    --ConfigRules.0.RiskLevel 3 \
    --ConfigRules.0.ManagedRuleIdentifier sfc-function-settings-check \
    --ConfigRules.0.InputParameter.0.ParameterKey maxMemorySize \
    --ConfigRules.0.InputParameter.0.Type Require \
    --ConfigRules.0.InputParameter.0.Value 512 \
    --RiskLevel 1 \
    --CompliancePackName 合规包12 \
    --Description 
```

Output: 
```
{
    "Response": {
        "CompliancePackId": "cp-33mA27YUlOJWG4sJ53Sx",
        "RequestId": "9de42909-38ef-4e54-99de-8f17f5bbf018"
    }
}
```

