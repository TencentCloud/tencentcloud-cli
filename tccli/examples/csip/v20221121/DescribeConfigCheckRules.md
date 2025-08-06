**Example 1: 云资源配置风险规则列表示例**

云资源配置风险规则列表示例

Input: 

```
tccli csip DescribeConfigCheckRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CheckTypeList": [
            {
                "Text": "账号安全",
                "Value": "account_security"
            },
            {
                "Text": "基础安全",
                "Value": "basic_security"
            },
            {
                "Text": "安全审计",
                "Value": "security_audit"
            },
            {
                "Text": "配置安全",
                "Value": "config_security"
            },
            {
                "Text": "鉴权管控",
                "Value": "auth_control"
            },
            {
                "Text": "权限管控",
                "Value": "permission_control"
            },
            {
                "Text": "网络安全",
                "Value": "network_security"
            },
            {
                "Text": "数据安全",
                "Value": "data_security"
            }
        ],
        "DispositionTypeList": [
            {
                "Text": "紧急风险治理",
                "Value": "emergency"
            },
            {
                "Text": "边界管控",
                "Value": "expose"
            },
            {
                "Text": "云资产加固",
                "Value": "asset_weakness"
            },
            {
                "Text": "安全防护提升",
                "Value": "safety_protection"
            },
            {
                "Text": "深度优化",
                "Value": "optimize"
            }
        ],
        "ProviderList": [
            {
                "Text": "阿里云",
                "Value": "alibaba"
            },
            {
                "Text": "亚马逊云",
                "Value": "aws"
            },
            {
                "Text": "华为云",
                "Value": "huawei"
            },
            {
                "Text": "微软云",
                "Value": "azure"
            },
            {
                "Text": "谷歌云",
                "Value": "gc"
            },
            {
                "Text": "腾讯云",
                "Value": "tencent"
            }
        ],
        "RequestId": "da381e6c-32fc-41b5-9f2b-a88c546e5392",
        "RiskLevelList": [
            {
                "Text": "严重",
                "Value": "critical"
            },
            {
                "Text": "高危",
                "Value": "high"
            },
            {
                "Text": "中危",
                "Value": "medium"
            },
            {
                "Text": "低危",
                "Value": "low"
            }
        ],
        "RuleList": [
            {
                "CheckType": "network_security",
                "DispositionType": "optimize",
                "InstanceType": "clb_instance",
                "Provider": "tencent",
                "RiskFixAdvance": "https://xxx",
                "RiskInfluence": "TLS 1.1及以下版本的协议已被证明存在安全漏洞，如BEAST、CRIME和POODLE等攻击。这些漏洞可能会被攻击者利用，从而导致数据泄露或者被恶意篡改。如果您的负载均衡器（Load Balancer，LB）使用的是TLS 1.1或以下版本的协议，那么它可能会面临这些安全风险。",
                "RiskLevel": "medium",
                "RiskTitle": "负载均衡启用TLS1.1及以下版本高危策略",
                "RuleID": "tc_200"
            }
        ],
        "TotalCount": 294
    }
}
```

