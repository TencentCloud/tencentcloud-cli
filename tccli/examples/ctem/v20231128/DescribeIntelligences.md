**Example 1: 查看漏洞情报**

查看漏洞情报

Input: 

```
tccli ctem DescribeIntelligences --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "BannerCount": 0,
                "InsertTime": "2023-06-06 16:48:11",
                "LastScanTime": "",
                "LastTaskInstanceId": "",
                "LastTaskStatus": "",
                "RiskLevel": 3,
                "Tags": "",
                "VulAssetCount": 0,
                "VulComponents": "据官方描述，在 GitLab CE/EE 15.11 和 16.0 之前的版本中，存在一个存储型 XSS 漏洞，攻击者可以通过精心构造的合并请求，绕过内容安全策略（CSP）的限制，在客户端上注入恶意脚本，从而窃取用户的敏感信息或者执行恶意操作。",
                "VulId": "SC-2023-0677",
                "VulName": "GitLab 存储型XSS漏洞（CVE-2023-2442）",
                "VulOverview": "GitLab 官方发布安全通告，披露了其 GitLab CE/EE 存在存储型 XSS 漏洞，漏洞编号CVE-2023-2442。可窃取用户的敏感信息或者执行恶意操作。",
                "XscanBannerPluginId": "80079",
                "XscanPocPluginId": "80080"
            },
            {
                "BannerCount": 0,
                "InsertTime": "2024-03-15 00:00:00",
                "LastScanTime": "",
                "LastTaskInstanceId": "",
                "LastTaskStatus": "",
                "RiskLevel": 1,
                "Tags": "Tags",
                "VulAssetCount": 0,
                "VulComponents": "VulComponents",
                "VulId": "SC-2024-1450",
                "VulName": "NodeBB 远程代码执行漏洞（CVE-2023-26045）",
                "VulOverview": "Atlassian 官方发布安全通告，披露了其 Bamboo 存在远程代码执行漏洞，漏洞编号CVE-2023-22506。可导致经过身份验证的远程攻击者执行任意代码等危害。",
                "XscanBannerPluginId": "",
                "XscanPocPluginId": ""
            },
            {
                "BannerCount": 0,
                "InsertTime": "2024-03-18 22:11:19",
                "LastScanTime": "",
                "LastTaskInstanceId": "",
                "LastTaskStatus": "",
                "RiskLevel": 2,
                "Tags": "11,22",
                "VulAssetCount": 0,
                "VulComponents": "spring,docker",
                "VulId": "SC-2024-1437",
                "VulName": "Spring Security 安全绕过漏洞（CVE-2024-22257）",
                "VulOverview": "Spring 官方发布安全通告，披露了其 Spring Security 存在安全绕过漏洞，漏洞编号CVE-2024-22257。可导致远程攻击者绕过安全限制未经授权访问和操作资源等危害。",
                "XscanBannerPluginId": "",
                "XscanPocPluginId": ""
            }
        ],
        "RequestId": "9766fffd-a415-46c2-8a70-a6405d4f0e0d",
        "Total": 3
    }
}
```

