**Example 1: 示例**

DescribeLicenseBindList

Input: 

```
tccli cwp DescribeLicenseBindList --cli-unfold-argument  \
    --LicenseId 1 \
    --LicenseType 0 \
    --ResourceId cdbae897e7e0
```

Output: 
```
{
    "Response": {
        "RequestId": "de41ce31-f2c0-49a9-a476-57051a5c7c6c",
        "TotalCount": 1,
        "List": [
            {
                "MachineName": "测试机器",
                "MachineWanIp": "10.0.0.0",
                "MachineIp": "10.0.0.0",
                "Quuid": "f6481aac-78f7-403e-867d-553c4af8b025",
                "Uuid": "f6481aac-78f7-403e-867d-553c4af8b025",
                "Tags": [
                    "dev"
                ],
                "AgentStatus": "ONLINE",
                "IsUnBind": false,
                "IsSwitchBind": false,
                "MachineExtraInfo": {
                    "WanIP": "10.0.0.0",
                    "PrivateIP": "10.0.0.0",
                    "NetworkType": 0,
                    "NetworkName": "dev",
                    "InstanceID": "ins-onxyg5w",
                    "HostName": "dev-one"
                }
            }
        ]
    }
}
```

