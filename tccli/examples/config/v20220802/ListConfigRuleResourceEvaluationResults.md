**Example 1: 查询配置规则资源评估结果**

查询配置规则资源评估结果

Input: 

```
tccli config ListConfigRuleResourceEvaluationResults --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Annotation": {
                    "Configuration": "false",
                    "DesiredValue": "false[123, 123, 123]",
                    "Operator": "",
                    "Property": "AttachedPolicy[resource, effect, action]"
                },
                "ResourceId": "4611686018427872551",
                "ResourceName": "Orgnization_QCSLinkedRoleInCIC",
                "ResourceRegion": "global",
                "ResourceTags": [],
                "ResourceType": "QCS::CAM::Role",
                "RuleDescription": "CAMu89d2u8272u7ed1u5b9au4e86u6307u5b9au7684u7b56u7565",
                "RuleId": "cr-9JY91Ayx1LamXSoa3geQ",
                "RuleIdentifier": "cam-role-attached-specified-policy",
                "RuleName": "CAMu89d2u8272u7ed1u5b9au4e86u6307u5b9au7684u7b56u7565",
                "RuleOwnerId": 700000145543,
                "RuleRiskLevel": 1
            }
        ],
        "RequestId": "40e6fc5f-6b54-461d-8a5e-c0b7c276cebe"
    }
}
```

