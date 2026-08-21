**Example 1: 获取基线配置检测项ID**

获取基线配置检测项ID

Input: 

```
tccli csip DescribeBaselinePolicyItemList --cli-unfold-argument  \
    --PolicyID 2 \
    --MemberId mem-**************752f66e429 \
    --ParentCategoryID 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ItemList": [
            {
                "AffectedVersionList": [],
                "Category": {
                    "CheckAssetType": "HOST",
                    "Description": "等保三级-Ubuntu  24.04 安全基线检查",
                    "ID": 176,
                    "Name": "等保三级-Ubuntu  24.04 安全基线检查"
                },
                "CheckObject": [
                    "HOST"
                ],
                "CustomItemID": 0,
                "DefaultValueList": [],
                "Description": "PASS_MIN_DAYS <N> - 允许更改密码的最短间隔天数。任何早于此天数的密码更改都将被拒绝。如果未指定，则假定为 0（禁用限制）。",
                "FixSuggestion": "编辑 /etc/login.defs，将 PASS_MIN_DAYS 设置为大于 0 的值，并遵循本地站点策略：\nPASS_MIN_DAYS 1",
                "ID": 4605,
                "IsCustomConf": false,
                "Name": "确保配置了最短密码天数",
                "ReferenceLink": "",
                "RiskLevel": "HIGH",
                "RuleID": 13400,
                "SupportCustomValue": false,
                "SupportFix": false,
                "SystemCategory": {
                    "CheckAssetType": "HOST",
                    "Description": "等保合规",
                    "ID": 1,
                    "Name": "等保合规"
                },
                "WebEditParam": ""
            }
        ],
        "TotalCount": 2,
        "RequestId": "c27c3d68-9200-47ca-b5a7-738a976e6c55"
    }
}
```

