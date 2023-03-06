**Example 1: 主机风险top5**



Input: 

```
tccli cwp DescribeBaselineHostRiskTop --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "HostRiskTop5": [
            {
                "HostId": "36a78a1e-7711-4e7f-9fbe-c7afab78cd78",
                "HostName": "jaryzhou-编码测试",
                "SeriousCount": 0,
                "HighCount": 32,
                "MediumCount": 126,
                "LowCount": 45
            },
            {
                "HostId": "a0770b41-9697-4a1d-8150-b8fa247b6189",
                "HostName": "功能测试ubuntu20漏洞修复v_txmitan",
                "SeriousCount": 0,
                "HighCount": 33,
                "MediumCount": 125,
                "LowCount": 44
            },
            {
                "HostId": "cc0e8a25-7169-4b5c-a929-2b4cccbfce10",
                "HostName": "功能测试ubuntu18漏洞修复v_txmitan",
                "SeriousCount": 0,
                "HighCount": 17,
                "MediumCount": 123,
                "LowCount": 43
            },
            {
                "HostId": "69796250-2a3a-40ef-b418-676e677019a4",
                "HostName": "piperpeng-test2",
                "SeriousCount": 0,
                "HighCount": 25,
                "MediumCount": 116,
                "LowCount": 23
            },
            {
                "HostId": "dbf3dcd4-179a-4bc6-86e4-15439f4cc898",
                "HostName": "漏洞yhvs编译机-linux",
                "SeriousCount": 0,
                "HighCount": 25,
                "MediumCount": 117,
                "LowCount": 21
            }
        ],
        "RequestId": "fc13bcdc-464f-4f94-a985-239e499d0bc0"
    }
}
```

