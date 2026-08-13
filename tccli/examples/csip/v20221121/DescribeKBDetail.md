**Example 1: 获取KB详情**



Input: 

```
tccli csip DescribeKBDetail --cli-unfold-argument  \
    --KBID 20001
```

Output: 
```
{
    "Response": {
        "KBDetail": {
            "ID": 20001,
            "Number": "KB5030211",
            "Name": "Windows Server 2019 累积更新",
            "ReferUrl": "https://support.microsoft.com/help/5030211",
            "PublishTime": "2025-06-25 14:00:00",
            "NeedRestart": true,
            "RelateVulList": [
                {
                    "VulID": 10001,
                    "VulName": "Windows 内核提权漏洞",
                    "CVEID": "CVE-2025-0001",
                    "Label": [
                        {
                            "Name": "IN_THE_WILD",
                            "Level": "HIGH",
                            "Remark": "已检测到真实利用行为"
                        }
                    ],
                    "CvssScore": 8.8,
                    "Level": "HIGH",
                    "PublishTime": "2025-06-20 00:00:00"
                }
            ],
            "RelateVulCount": 1
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

