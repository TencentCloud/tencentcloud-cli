**Example 1: 资产视角下风险列表示例**



Input: 

```
tccli csip DescribeAssetRiskList --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AssetRiskList": [
            {
                "AppId": 9000448058,
                "AssetType": "存储桶",
                "CheckType": "auth_control",
                "Classify": "emergency",
                "CloudAccountId": "30001616646",
                "CloudAccountName": "天空之蓝",
                "CreateTime": "2025-07-14 16:24:01",
                "InstanceId": "rdpexport-9000448058",
                "InstanceName": "rdpexport-9000448058",
                "Provider": "tencent",
                "ProviderName": "腾讯云",
                "RiskRuleId": "tc_072",
                "RiskStatus": 0,
                "RiskTitle": "COS存储桶访问权限配置不当",
                "Severity": "high",
                "StandardTerms": [
                    {
                        "Tag": "网络安全等级保护基本要求（三级）",
                        "Terms": [
                            "1.4.1 身份鉴别"
                        ]
                    },
                    {
                        "Tag": "网络安全等级保护基本要求（二级）",
                        "Terms": [
                            "1.4.1 身份鉴别"
                        ]
                    },
                    {
                        "Tag": "CIS腾讯云基础基准v1.0.0",
                        "Terms": [
                            "4.1 确保 COS 存储桶不可匿名或公开访问。"
                        ]
                    }
                ],
                "UpdateTime": "2025-07-22 17:53:05"
            }
        ],
        "RequestId": "1c358530-d17a-4871-bd8c-a1cebde94c9a",
        "StandardNameList": [
            {
                "ID": 1,
                "Name": "CIS阿里云基础基准v2.0.0"
            },
            {
                "ID": 2,
                "Name": "CIS AWS计算服务基准 v1.1.0"
            },
            {
                "ID": 3,
                "Name": "网络安全等级保护基本要求（二级）"
            },
            {
                "ID": 4,
                "Name": "网络安全等级保护基本要求（三级）"
            },
            {
                "ID": 5,
                "Name": "CIS AWS基础基线v5.0.0"
            },
            {
                "ID": 6,
                "Name": "CIS腾讯云基础基准v1.0.0"
            }
        ],
        "TotalCount": 2877
    }
}
```

