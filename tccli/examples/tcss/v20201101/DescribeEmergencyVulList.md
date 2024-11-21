**Example 1: 查询应急漏洞列表**



Input: 

```
tccli tcss DescribeEmergencyVulList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CVEID": "CVE-2024-47176",
                "CVSSV3Score": 0,
                "Category": "OTHER",
                "DefenceHostCount": 0,
                "DefenceScope": "",
                "DefenceStatus": "",
                "DefendedCount": 0,
                "ID": 0,
                "LatestFoundTime": "",
                "Level": "HIGH",
                "Name": "cups-browsed 远程代码执行漏洞",
                "PocID": "pcmgr-521425",
                "Status": "NOT_SCAN",
                "SubmitTime": "2024-09-27 06:15:00",
                "Tags": [
                    "POC",
                    "SYS"
                ]
            }
        ],
        "RequestId": "a3fbabbb-7c7b-45dd-9219-a0b3ca9bc932",
        "TotalCount": 241
    }
}
```

