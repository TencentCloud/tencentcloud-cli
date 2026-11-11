**Example 1: 查询主机漏洞风险事件列表**



Input: 

```
tccli csip DescribeHostVulRiskEventList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --MemberId mem-tencent-*********f66e429
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "UUID": "8f3c4c74-8cc9-4ddf-b66f-2d20f1a9a001",
                "RiskID": 1000000000001,
                "VulID": 12345,
                "VulName": "OpenSSL 远程代码执行漏洞",
                "CVEID": "CVE-2024-12345",
                "Category": "LINUX",
                "Level": "HIGH",
                "VPRLevel": "URGENT",
                "CheckMethod": "POC",
                "RiskStatus": "PENDING",
                "SupportFix": true,
                "LatestScanTime": "2026-09-18T06:00:00+08:00",
                "InstanceID": "ins-5ijxpaa6",
                "AppID": 1251234567
            }
        ],
        "TotalCount": 1,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

