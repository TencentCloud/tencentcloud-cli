**Example 1: 获取合规包列表**



Input: 

```
tccli config ListCompliancePacks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4348278a-b93d-434c-aabd-e8e923560203",
        "Items": [
            {
                "CompliancePackId": "cp-xzfz0vu007feuhwi8auv",
                "CompliancePackName": "合规1",
                "ComplianceResult": "NON_COMPLIANT",
                "CreateTime": "2022-11-16 14:11:48",
                "Description": null,
                "NoCompliantNames": [
                    "CAM访问管理子用户必须关联用户组"
                ],
                "RiskLevel": 1,
                "RuleCount": 1,
                "Status": "ACTIVE"
            }
        ],
        "Total": 1
    }
}
```

