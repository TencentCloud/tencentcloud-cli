**Example 1: 获取漏洞紧急通知信息**

获取漏洞紧急通知信息

Input: 

```
tccli cwp DescribeVulEmergentMsg --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "EmergentMsgList": [
            {
                "VulId": 100488,
                "PublishTime": "2020-03-13 00:00:00",
                "Name": "Windows SMB远程代码执行漏洞",
                "NameEn": "Windows SMB remote exec"
            }
        ]
    }
}
```

**Example 2: kb和漏洞紧急信息**

kb和漏洞紧急信息

Input: 

```
tccli cwp DescribeVulEmergentMsg --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EmergentMsgList": [
            {
                "KbId": 0,
                "KbNumber": "",
                "Name": "Redis 远程代码执行漏洞(CVE-2025-32023)",
                "NameEn": "Redis remote code execution vulnerability (CVE-2025-32023)",
                "PublishTime": "2025-07-07 11:18:57",
                "SupportDefense": 0,
                "SupportFix": 0,
                "VulId": 55275
            },
            {
                "KbId": 1536,
                "KbNumber": "KB5051972",
                "Name": "2025-02 Cumulative Security Update for Internet Explorer 11 for Windows Server 2012 for x64-based systems (KB5051972)",
                "NameEn": "",
                "PublishTime": "",
                "SupportDefense": 0,
                "SupportFix": 1,
                "VulId": 0
            }
        ],
        "RequestId": "d49c3490-8b74-4f01-9d92-d1060215b061"
    }
}
```

