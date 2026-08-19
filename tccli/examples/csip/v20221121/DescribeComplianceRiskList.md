**Example 1: 合规标准下聚合云资源配置检测风险列表**



Input: 

```
tccli csip DescribeComplianceRiskList --cli-unfold-argument  \
    --StandardID 3 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AssetTypeList": [
            {
                "Text": "腾讯云-CAM 账号设置",
                "Value": "tencent-cam_account_setting"
            }
        ],
        "CheckViewRiskList": [
            {
                "AssetCount": 0,
                "AssetType": "ES 采集器",
                "AssetTypeIconURL": "https://cloud-xspm-we*-1258344699.cos.ap-gu*n*z*ou.myqcloud.com/asset-icon/analysisIcon_2d.svg",
                "CheckType": "permission_control",
                "Classify": "emergency",
                "CreateTime": "",
                "EventType": "Elasticsearch Service采集器未禁用管理员权限",
                "Provider": "腾讯云",
                "RiskCount": 0,
                "RiskDesc": "发现*个Elasticsearch Service采集器未禁用管理员权限",
                "RiskRuleId": "tc_066",
                "RiskStatus": 4,
                "RiskTitle": "Elasticsearch Service采集器未禁用管理员权限",
                "Severity": "critical",
                "StandardTerms": [
                    {
                        "Tag": "网络安全等级保护基本要求（二级）",
                        "Terms": [
                            "1.4.2 访问控制"
                        ]
                    }
                ],
                "UpdateTime": ""
            }
        ],
        "TotalCount": 106,
        "RequestId": "a3117c56-23f5-45d9-bacb-3b02d5cc465c"
    }
}
```

