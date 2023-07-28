**Example 1: 查询批量导入机器信息**



Input: 

```
tccli cwp DescribeImportMachineInfo --cli-unfold-argument  \
    --MachineList 0.0.0.0 \
    --ImportType Ip \
    --IsQueryProMachine True
```

Output: 
```
{
    "Response": {
        "EffectiveMachineInfoList": [
            {
                "MachineName": "机器名称",
                "MachinePublicIp": "0.0.0.0",
                "MachinePrivateIp": "0.0.0.0",
                "MachineTag": null,
                "CloudTags": null,
                "Quuid": "310eb617-ed1f-4dbb-a3df-xxxxxxx",
                "Uuid": "310eb617-ed1f-4dbb-a3df-xxxxxxx",
                "KernelVersion": "4.18.0-80.el8.x86_64",
                "MachineStatus": "OFFLINE",
                "LicenseOrder": null,
                "VulNum": 508,
                "InstanceID": "ins-xxxxxxxx"
            }
        ],
        "InvalidMachineList": [],
        "RequestId": "fa0c6429-2e91-498b-8dce-fc1487b7829e"
    }
}
```

