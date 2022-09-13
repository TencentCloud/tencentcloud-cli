**Example 1: 示例**



Input: 

```
tccli cwp DescribeLicenseBindList --cli-unfold-argument  \
    --LicenseId 1 \
    --LicenseType 0 \
    --ResourceId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "de41ce31-f2c0-49a9-a476-57051a5c7c6c",
        "TotalCount": 1,
        "List": [
            {
                "MachineName": "云服务器",
                "MachineWanIp": "1.1.1.1",
                "MachineIp": "1.1.1.1",
                "Quuid": "xxxx-xxxx-xxx-xxxx",
                "Uuid": "xxxx-xxxx-xxx-xxxx",
                "Tags": [
                    "标签"
                ],
                "AgentStatus": "OFFLINE",
                "IsUnBind": true,
                "IsSwitchBind": true
            }
        ]
    }
}
```

