**Example 1: 获取区域主机列表**

本接口 (DescribeMachines) 用于获取区域主机列表。

Input: 

```
tccli cwp DescribeMachineList --cli-unfold-argument  \
    --MachineType CVM \
    --MachineRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Machines": [
            {
                "MachineName": "ccs_cls-i4vyo8qa_node",
                "MachineIp": "0.0.0.0",
                "MachineWanIp": "0.0.0.0",
                "MachineOs": "ubuntu16.04.1 LTSx86_64",
                "MachineStatus": "OFFLINE",
                "Quuid": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
                "Uuid": "",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": 0,
                "Tag": [],
                "MalwareNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "SAFE",
                "InstanceState": "TERMINATED_PRO_VERSION",
                "ProjectId": 1,
                "HasAssetScan": 1,
                "LicenseStatus": 0,
                "InvasionNum": 0,
                "BaselineNum": 0,
                "RegionInfo": {
                    "RegionCode": "gz",
                    "Region": "ap-guangzhuo",
                    "RegionId": 1,
                    "RegionName": "广州",
                    "RegionNameEn": "chine guangzhou"
                },
                "MachineType": "CVM"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c30f35cb-2f3e-94f5-59ae-316e0f32e660"
    }
}
```

