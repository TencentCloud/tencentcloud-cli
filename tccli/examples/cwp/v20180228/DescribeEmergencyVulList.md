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
                "VulId": 8,
                "Level": 4,
                "VulName": "Struts2 S2-013远程代码执行漏洞(CVE-2013-1966)",
                "PublishDate": "2013-05-23 00:00:00",
                "Status": 0,
                "LastScanTime": "",
                "Progress": 0
            },
            {
                "VulId": 9,
                "Level": 4,
                "VulName": "Struts2 S2-019远程代码执行漏洞(CVE-2013-4316)",
                "PublishDate": "2013-09-26 00:00:00",
                "Status": 0,
                "LastScanTime": "",
                "Progress": 0
            },
            {
                "VulId": 18,
                "Level": 4,
                "VulName": "OpenSSL Heartbleed漏洞(CVE-2014-0160)",
                "PublishDate": "2014-04-07 00:00:00",
                "Status": 0,
                "LastScanTime": "",
                "Progress": 0
            }
        ],
        "RequestId": "djaiodhajdhaj",
        "TotalCount": 35,
        "ExistsRisk": true
    }
}
```

