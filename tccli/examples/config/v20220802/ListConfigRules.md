**Example 1: 获取规则列表**

获取规则列表

Input: 

```
tccli config ListConfigRules --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderType desc \
    --RiskLevel 1 \
    --State ACTIVE \
    --ComplianceResult COMPLIANT \
    --RuleName CAM
```

Output: 
```
{
    "Response": {
        "RequestId": "107f8d51-7095-4a6f-b374-a8aa7743584b",
        "Items": [
            {
                "AccountGroupId": "ca-324234",
                "AccountGroupName": "账号组",
                "Annotation": null,
                "CompliancePackId": "",
                "CompliancePackName": null,
                "ComplianceResult": "NON_COMPLIANT",
                "ConfigRuleId": "cr-HQxxxxxxxhR0BxxxxGodh",
                "ConfigRuleInvokedTime": null,
                "CreateTime": "2024-11-15 14:21:47",
                "Description": "CAM用户下不存在已禁用的 AccessKey，则符合规则。",
                "ExcludeResourceIdsScope": [],
                "Identifier": "cam-user-invalid-ak-check",
                "IdentifierType": "SYSTEM",
                "InputParameter": [],
                "Labels": [
                    "用户",
                    "密钥"
                ],
                "ManageInputParameter": [],
                "ManageTriggerType": [
                    "ConfigurationItemChangeNotification"
                ],
                "RegionsScope": [],
                "ResourceType": [
                    "QCS::CAM::User"
                ],
                "RiskLevel": 3,
                "RuleName": "CAM用户下不存在已禁用的访问密钥AccessKey",
                "RuleOwnerId": 84935363164,
                "ServiceFunction": null,
                "SourceCondition": [],
                "Status": "ACTIVE",
                "TagsScope": [],
                "TriggerType": [
                    {
                        "MaximumExecutionFrequency": null,
                        "MessageType": "ConfigurationItemChangeNotification"
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```

