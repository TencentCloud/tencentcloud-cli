**Example 1: 查询2025年1月漏洞情报**

查询2025年1月漏洞情报

Input: 

```
tccli csip DescribeMandatoryVulSet --cli-unfold-argument  \
    --Year 2025 \
    --Month 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Level": "中危",
                "SubmitTime": "2025-01-28 02:15:00",
                "VULID": "CVE-2025-24367",
                "VULName": "Cacti 任意文件创建致远程代码执行漏洞"
            },
            {
                "Level": "严重",
                "SubmitTime": "2025-01-23 20:15:00",
                "VULID": "CVE-2025-23006",
                "VULName": "SonicWall SMA1000 远程命令执行漏洞"
            },
            {
                "Level": "严重",
                "SubmitTime": "2025-01-22 05:15:00",
                "VULID": "CVE-2025-21535",
                "VULName": "WebLogic Server T3/IIOP远程命令执行漏洞"
            },
            {
                "Level": "严重",
                "SubmitTime": "2025-01-15 23:15:00",
                "VULID": "CVE-2024-12084",
                "VULName": "Rsync 堆缓冲区溢出漏洞"
            },
            {
                "Level": "高危",
                "SubmitTime": "2025-01-14 22:15:00",
                "VULID": "CVE-2024-55591",
                "VULName": "Fortinet FortiOS/FortiProxy 身份认证绕过漏洞（CVE-2024-55591）"
            },
            {
                "Level": "中危",
                "SubmitTime": "2025-01-09 15:15:00",
                "VULID": "CVE-2024-53704",
                "VULName": "SonicOS SSLVPN 认证绕过漏洞"
            },
            {
                "Level": "严重",
                "SubmitTime": "2025-01-09 07:15:00",
                "VULID": "CVE-2025-0282",
                "VULName": "Ivanti 缓冲区溢出远程代码执行漏洞"
            },
            {
                "Level": "高危",
                "SubmitTime": "2025-01-07 06:15:00",
                "VULID": "CVE-2024-46981",
                "VULName": "Redis 远程代码执行漏洞（CVE-2024-46981）"
            }
        ],
        "RequestId": "20ac5451-d699-40fc-a0f8-aaad768ba37d",
        "Total": 8
    }
}
```

