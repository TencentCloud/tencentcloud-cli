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
        "MachineIp": "abc",
        "ProtectDays": 1,
        "MachineOs": "abc",
        "MachineName": "abc",
        "MachineStatus": "abc",
        "InstanceId": "abc",
        "MachineWanIp": "abc",
        "Quuid": "abc",
        "Uuid": "abc",
        "IsProVersion": true,
        "ProVersionOpenDate": "abc",
        "MachineType": "abc",
        "MachineRegion": "abc",
        "PayMode": "abc",
        "FreeMalwaresLeft": 1,
        "FreeVulsLeft": 1,
        "AgentVersion": "abc",
        "ProVersionDeadline": "abc",
        "HasAssetScan": 1,
        "ProtectType": "abc",
        "RequestId": "abc"
    }
}
```

