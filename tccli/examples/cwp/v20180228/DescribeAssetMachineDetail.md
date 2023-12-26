**Example 1: 获取资产管理主机资源详细信息**



Input: 

```
tccli cwp DescribeAssetMachineDetail --cli-unfold-argument  \
    --Quuid 7dc822ab-1eaa-d469-67e2-0eed63e8be9c \
    --Uuid 7dc822ab-1eaa-d469-67e2-0eed63e8be9c
```

Output: 
```
{
    "Response": {
        "MachineDetail": {
            "Quuid": "7dc822ab-1eaa-d469-67e2-0eed63e8be9c",
            "Uuid": "7dc822ab-1eaa-d469-67e2-0eed63e8be9c",
            "MachineIp": "172.16.255.135",
            "MachineName": "aaa_worker",
            "ProjectId": 0,
            "OsInfo": "TencentOS Server 3.1 (TK4)",
            "Cpu": "",
            "MemSize": 0,
            "MemLoad": "",
            "DiskSize": 0,
            "DiskLoad": "",
            "PartitionCount": 0,
            "MachineWanIp": "172.16.255.135",
            "CpuSize": 0,
            "CpuLoad": "",
            "ProtectLevel": 2,
            "RiskStatus": "未知",
            "ProtectDays": 0,
            "BuyTime": "2023-12-26 10:30:02",
            "EndTime": "2024-01-10 10:51:11",
            "CoreVersion": "",
            "OsType": "",
            "AgentVersion": "5.1.0.150",
            "InstallTime": "2023-12-26 10:22:03",
            "BootTime": "",
            "LastLiveTime": "2023-12-26 10:28:44",
            "Producer": "",
            "SerialNumber": "",
            "DeviceVersion": "",
            "Status": 0,
            "CpuLoadVul": "50",
            "FirstTime": "2023-12-26 10:28:44",
            "NetCards": [],
            "Disks": [],
            "OfflineTime": "",
            "InstanceId": "ins-aaaa",
            "UpdateTime": "--",
            "MachineExtraInfo": {
                "WanIP": "172.16.255.135",
                "PrivateIP": "172.16.255.135",
                "NetworkType": 1,
                "NetworkName": "vpc-aaaa",
                "InstanceID": "ins-aaaa",
                "HostName": "aaa_worker"
            }
        },
        "RequestId": "c063defb-30b0-4667-b042-e06ecaa19f09"
    }
}
```

