**Example 1: 获取漏洞受影响机器列表**

获取漏洞受影响机器列表

Input: 

```
tccli cwp DescribeImpactedHosts --cli-unfold-argument  \
    --VulId 1001 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "ImpactedHosts": [
            {
                "IsProVersion": true,
                "Id": 4,
                "VulId": 1001,
                "MachineIp": "10.10.12.12",
                "MachineName": "机器名称",
                "VulStatus": "FIXED",
                "Uuid": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
                "Description": "漏洞描述",
                "LastScanTime": "2018-03-19 17:38:56"
            }
        ],
        "TotalCount": 10
    }
}
```

