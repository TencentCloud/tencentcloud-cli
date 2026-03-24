**Example 1: 获取合规包详情**



Input: 

```
tccli config DescribeAggregateCompliancePack --cli-unfold-argument  \
    --CompliancePackId cp-1g118yvw28p142zr17kz \
    --AccountGroupId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "f9c86059-d081-4034-b566-05535406c231",
        "CompliancePackId": "cp-xzfz0vu007feuhwi8auv",
        "CompliancePackName": "合规1",
        "ConfigRules": [
            {
                "ComplianceResult": "NON_COMPLIANT",
                "ConfigRuleId": "cr-13vkg9c31dixgabkepxe",
                "CreateByType": "user",
                "Description": "帐号访问管理中用户至少关联一个用户组，则符合规则。",
                "Identifier": "cam-user-group-bound",
                "InputParameter": [],
                "Labels": [
                    "用户",
                    "用户组"
                ],
                "ManageInputParameter": [],
                "RiskLevel": 3,
                "RuleName": "CAM访问管理子用户必须关联用户组",
                "SourceCondition": [
                    {
                        "DesiredValue": "1",
                        "EmptyAs": "COMPLIANT",
                        "Operator": "GreaterOrEquals",
                        "Required": false,
                        "SelectPath": "$User.GroupBindNum"
                    }
                ],
                "Status": "ACTIVE"
            }
        ],
        "CreateTime": "2022-11-16 14:11:48",
        "Description": "安全合规",
        "RiskLevel": 1,
        "Status": "ACTIVE"
    }
}
```

