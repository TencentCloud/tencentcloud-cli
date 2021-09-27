**Example 1: 获取资产管理主机资源详细信息**



Input: 

```
tccli cwp DescribeAssetMachineDetail --cli-unfold-argument  \
    --Quuid xx \
    --Uuid xx
```

Output: 
```
{
    "Response": {
        "MachineDetail": {
            "Uuid": "xx",
            "PartitionCount": 1,
            "SerialNumber": "xx",
            "DiskLoad": "xx",
            "EndTime": "xx",
            "MachineIp": "xx",
            "InstallTime": "xx",
            "Status": 1,
            "UpdateTime": "xx",
            "MachineWanIp": "xx",
            "InstanceId": "xx",
            "MachineName": "xx",
            "LastLiveTime": "xx",
            "Cpu": "xx",
            "BootTime": "xx",
            "BuyTime": "xx",
            "AgentVersion": "xx",
            "OfflineTime": "xx",
            "OsType": "xx",
            "DeviceVersion": "xx",
            "OsInfo": "xx",
            "MemLoad": "xx",
            "ProjectId": 1,
            "Disks": [
                {
                    "Used": 1,
                    "Name": "xx",
                    "Percent": 0.0,
                    "Path": "xx",
                    "Type": "xx",
                    "Size": 1
                }
            ],
            "CoreVersion": "xx",
            "CpuLoad": "xx",
            "DiskSize": 1,
            "MemSize": 1,
            "RiskStatus": "xx",
            "Producer": "xx",
            "CpuSize": 1,
            "ProtectDays": 1,
            "Quuid": "xx",
            "NetCards": [
                {
                    "DnsServer": "xx",
                    "Ip": "xx",
                    "Mac": "xx",
                    "Ipv6": "xx",
                    "GateWay": "xx",
                    "Name": "xx"
                }
            ],
            "ProtectLevel": 1
        },
        "RequestId": "xx"
    }
}
```

