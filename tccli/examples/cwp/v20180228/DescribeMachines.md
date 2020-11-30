**Example 1: 获取区域主机列表**

本接口 (DescribeMachines) 用于获取区域主机列表。

Input: 

```
tccli cwp DescribeMachines --cli-unfold-argument  \
    --MachineType CVM \
    --MachineRegion ap-shanghai \
    --Filters.0.Name Keywords \
    --Filters.0.Values 10.0.1.1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Machines": [
            {
                "MachineName": "ccs_cls-i4vyo8qa_node",
                "MachineIp": "172.16.0.4",
                "MachineWanIp": "193.112.57.245",
                "MachineOs": "ubuntu16.04.1 LTSx86_64",
                "MachineStatus": "OFFLINE",
                "Quuid": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
                "Uuid": "",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": 0,
                "Tag": [],
                "MalwareNum": 0,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "SAFE",
                "InstanceState": "TERMINATED_PRO_VERSION"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c30f35cb-2f3e-94f5-59ae-316e0f32e660"
    }
}
```

