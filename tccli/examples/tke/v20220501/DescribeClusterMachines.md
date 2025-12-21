**Example 1: 查询原生节点列表**



Input: 

```
tccli tke DescribeClusterMachines --cli-unfold-argument  \
    --Limit 0 \
    --ClusterId cls-123 \
    --Filters.0.Values 789 \
    --Filters.0.Name cls-123 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "1231",
        "Machines": [
            {
                "ExpiredTime": "123",
                "SystemDisk": {
                    "AutoFormatAndMount": true,
                    "MountTarget": "123",
                    "DiskSize": 0,
                    "FileSystem": "123",
                    "DiskType": "123"
                },
                "LanIP": "123",
                "DisplayName": "123",
                "InstanceType": "123",
                "Zone": "123",
                "InstanceFamily": "123",
                "MachineName": "123",
                "IsProtectedFromScaleIn": true,
                "InternetAccessible": {
                    "BandwidthPackageId": "123",
                    "MaxBandwidthOut": 0,
                    "ChargeType": "123"
                },
                "PayMode": "123",
                "InstanceChargeType": "123",
                "RenewFlag": "123",
                "LoginStatus": "123",
                "Memory": 1,
                "GPU": 1,
                "MachineState": "123",
                "CPU": 1,
                "CreatedAt": "123"
            }
        ]
    }
}
```

