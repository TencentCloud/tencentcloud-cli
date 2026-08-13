**Example 1: 查询已修复漏洞列表**



Input: 

```
tccli csip DescribeVulFixedList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --MemberId mem-tencent-****************
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "VulId": 10001,
                "VulName": "CVE-2024-12345",
                "Level": "HIGH",
                "VRPRatingInfo": {
                    "Result": "URGENT",
                    "Remark": "该漏洞存在在野利用",
                    "Stage": [
                        {
                            "Stage": "威胁活跃度",
                            "Result": "高"
                        }
                    ]
                },
                "VulCategory": "LINUX",
                "CveId": "CVE-2024-12345",
                "MachineName": "web-server-01",
                "InstanceId": "ins-abc12345",
                "ComponentCount": 2,
                "Components": [
                    "openssl 1.1.1 /usr/lib/libssl.so",
                    "openssl 1.1.1 /usr/bin/openssl"
                ],
                "LatestFixTime": "2025-06-26T10:05:00+08:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

