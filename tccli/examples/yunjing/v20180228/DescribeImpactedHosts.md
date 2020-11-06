**Example 1: Getting affected server list**

This example shows you how to get the list of servers affected by a vulnerability.

Input: 

```
tccli yunjing DescribeImpactedHosts --cli-unfold-argument  \
    --VulId 1001 \
    --VulType WEB \
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
                "Id": 4,
                "VulId": 1001,
                "MachineIp": "10.10.12.12",
                "MachineName": "Server name",
                "VulStatus": "FIXED",
                "Uuid": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
                "Description": "Vulnerability description",
                "LastScanTime": "2018-03-19 17:38:56"
            }
        ],
        "TotalCount": 10
    }
}
```

