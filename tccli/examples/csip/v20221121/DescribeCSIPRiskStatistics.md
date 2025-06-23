**Example 1: 获取风险中心风险概况**



Input: 

```
tccli csip DescribeCSIPRiskStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "CFGHighLevel": 46,
            "CFGTotal": 333,
            "LastScanTime": "2025-04-11 00:00:09",
            "PortHighLevel": 1,
            "PortTotal": 66,
            "ServerHighLevel": 0,
            "ServerTotal": 6,
            "VULHighLevel": 31,
            "VULTotal": 596,
            "WeakPasswordHighLevel": 0,
            "WeakPasswordTotal": 0,
            "WebsiteHighLevel": 0,
            "HostBaseLineRiskTotal": 0,
            "HostBaseLineRiskHighLevel": 0,
            "PodBaseLineRiskTotal": 0,
            "PodBaseLineRiskHighLevel": 0,
            "WebsiteTotal": 15
        },
        "RequestId": "14a5d202-861d-4669-8ca7-592c0acd2dc9"
    }
}
```

