**Example 1: 编辑合规包**



Input: 

```
tccli config UpdateCompliancePack --cli-unfold-argument  \
    --CompliancePackId cp-xzfz0vu007feuhwi8auv \
    --CompliancePackName 合规1 \
    --RiskLevel 1 \
    --Description 安全合规 \
    --ConfigRules.0.Identifier cam-user-group-bound \
    --ConfigRules.0.RuleName CAM访问管理子用户必须关联用户组 \
    --ConfigRules.0.Description 帐号访问管理中用户至少关联一个用户组，则符合规则。 \
    --ConfigRules.0.RiskLevel 3 \
    --ConfigRules.0.ConfigRuleId cr-13vkg9c31dixgabkepxe
```

Output: 
```
{
    "Response": {
        "RequestId": "da85d5e2-4432-4f02-9863-0ab07adeff33"
    }
}
```

