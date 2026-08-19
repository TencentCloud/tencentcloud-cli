**Example 1: 自定义风险规则配置列表**



Input: 

```
tccli csip DescribeCustomRiskRules --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AssetTypeList": [
            {
                "Text": "腾讯云-API 网关",
                "Value": "tencent-apigateway_api"
            }
        ],
        "CheckTypeList": [
            {
                "Count": "33/33",
                "Text": "账号安全",
                "Value": "account_security"
            }
        ],
        "ClassifyList": [
            {
                "Count": "28/28",
                "Text": "云资产加固",
                "Value": "asset_weakness"
            }
        ],
        "ProviderList": [
            {
                "Text": "腾讯云",
                "Value": "tencent"
            }
        ],
        "RiskRuleList": [
            {
                "AssetType": "API 网关",
                "CheckType": "permission_control",
                "Classify": "emergency",
                "IsFree": 0,
                "PolicyEnableCount": 1,
                "Provider": "tencent",
                "RelatedUinCount": 1,
                "RiskTitle": "API 网关未授权访问且存储桶未禁用匿名用户列桶权限",
                "RuleID": "tc_142",
                "Severity": "low",
                "StandardTerms": [],
                "Status": "disable"
            }
        ],
        "RuleSeverityList": [
            {
                "Count": "1/1",
                "Text": "严重",
                "Value": "critical"
            }
        ],
        "StandardList": [
            {
                "Count": "101/101",
                "Text": "网络安全等级保护基本要求（二级）",
                "Value": "3"
            }
        ],
        "StandardNameList": [],
        "TotalCount": 167,
        "RequestId": "63375643-8a57-4ad1-bf2d-db67a9335880"
    }
}
```

