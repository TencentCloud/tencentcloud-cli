**Example 1: 查询可修复主机列表**



Input: 

```
tccli csip DescribeVulFixableMachineList --cli-unfold-argument  \
    --VulIds 10001 10002 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "VulIds": [
                    10001
                ],
                "InstanceId": "ins-a1b2c3d4",
                "MachineName": "web-server-01",
                "MachineIp": "10.0.0.100",
                "PublicIp": "203.0.113.10",
                "OsType": "linux",
                "OsName": "CentOS 7.9",
                "MachineStatus": "ONLINE",
                "SupportAutoFix": 1,
                "FixStatus": 0,
                "LatestFixTime": "2025-06-25T15:00:00+08:00",
                "NotFixableReason": "",
                "FixCommands": [
                    "sudo yum update zlib-devel zlib"
                ],
                "Components": [
                    "zlib-devel",
                    "zlib"
                ],
                "TagItems": [],
                "AppId": 1251234567,
                "PayVersion": "ULTIMATE"
            }
        ],
        "TotalCount": 1,
        "FixableCount": 1,
        "NotFixableCount": 0,
        "VulSummary": [
            {
                "VulId": 10001,
                "VulName": "OpenSSL 远程代码执行漏洞",
                "CveId": "CVE-2024-12345",
                "AffectedCount": 1,
                "NeedReboot": false,
                "FixSwitch": true
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

