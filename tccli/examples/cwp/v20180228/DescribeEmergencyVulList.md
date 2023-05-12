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
                "VulId": 1,
                "Level": 1,
                "VulName": "abc",
                "PublishDate": "abc",
                "Category": 1,
                "Status": 1,
                "LastScanTime": "abc",
                "Progress": 1,
                "CveId": "abc",
                "CvssScore": 0,
                "Labels": "abc",
                "HostCount": 1,
                "IsSupportDefense": 1,
                "DefenseAttackCount": 1
            }
        ],
        "TotalCount": 1,
        "ExistsRisk": true,
        "RequestId": "abc"
    }
}
```

