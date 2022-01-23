**Example 1: 获取机器详情**

本接口（DescribeMachineInfo）用于获取机器详细情况。

Input: 

```
tccli cwp DescribeMachineInfo --cli-unfold-argument  \
    --Uuid UUID
```

Output: 
```
{
    "Response": {
        "ProVersionDeadline": "xx",
        "IsProVersion": true,
        "MachineOs": "xx",
        "Uuid": "xx",
        "RequestId": "xx",
        "HasAssetScan": 1,
        "InstanceId": "xx",
        "MachineName": "xx",
        "FreeVulsLeft": 1,
        "MachineIp": "xx",
        "PayMode": "xx",
        "AgentVersion": "xx",
        "MachineRegion": "xx",
        "ProtectDays": 1,
        "Quuid": "xx",
        "FreeMalwaresLeft": 1,
        "MachineStatus": "xx",
        "MachineWanIp": "xx",
        "MachineType": "xx",
        "ProVersionOpenDate": "xx",
        "ProtectType": "BASIC_VERSION"
    }
}
```

