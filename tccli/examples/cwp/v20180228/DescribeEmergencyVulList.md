**Example 1: 应急漏洞列表**

应急漏洞列表

Input: 

```
tccli cwp DescribeEmergencyVulList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "VulId": 105374,
                "Level": 4,
                "VulName": "Apache OFBiz SSRF到远程代码执行漏洞（CVE-2024-45507）",
                "PublishDate": "2024-09-04 00:00:00",
                "Category": 2,
                "Status": 2,
                "LastScanTime": "2024-10-21 14:27:07",
                "Progress": 0,
                "CveId": "CVE-2024-45507",
                "CvssScore": 9.8,
                "Labels": "远程利用",
                "HostCount": 0,
                "IsSupportDefense": 0,
                "DefenseAttackCount": 0,
                "Method": 1,
                "AttackLevel": 0,
                "DefenseState": false
            }
        ],
        "TotalCount": 1,
        "ExistsRisk": true,
        "RequestId": "e5b4724c-49af-46ab-bd84-cdbae897e7e0"
    }
}
```

