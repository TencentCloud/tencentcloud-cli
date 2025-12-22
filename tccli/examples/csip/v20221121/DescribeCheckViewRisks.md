**Example 1: 检查视角下云资源配置风险列表**



Input: 

```
tccli csip DescribeCheckViewRisks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CheckViewRiskList": [
            {
                "AssetCount": 2,
                "AssetType": "存储桶",
                "CheckType": "auth_control",
                "Classify": "emergency",
                "CreateTime": "2025-11-04 12:09:42",
                "EventType": "COS存储桶访问权限配置不当",
                "Provider": "腾讯云",
                "RiskCount": 8,
                "RiskDesc": "发现*个COS存储桶访问权限配置不当",
                "RiskRuleId": "tc_072",
                "RiskStatus": 0,
                "RiskTitle": "COS存储桶访问权限配置不当",
                "Severity": "high",
                "StandardTerms": [
                    {
                        "Tag": "网络安全等级保护基本要求（三级）",
                        "Terms": [
                            "2.3.1 访问控制",
                            "1.3.2 访问控制"
                        ]
                    },
                    {
                        "Tag": "网络安全等级保护基本要求（二级）",
                        "Terms": [
                            "1.3.2 访问控制",
                            "2.3.1 访问控制"
                        ]
                    }
                ],
                "UpdateTime": "2025-12-02 08:13:08"
            }
        ],
        "RequestId": "d68d6d2e-28f5-4db3-9f52-902ca2bc0937",
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
            }
        ],
        "TotalCount": 33
    }
}
```

