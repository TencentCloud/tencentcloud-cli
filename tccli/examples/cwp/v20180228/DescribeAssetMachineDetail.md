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
            "Quuid": "24ab84ea-99d9-4ec0-b8fc-f68553191066",
            "Uuid": "24ab84ea-99d9-4ec0-b8fc-f68553191066",
            "MachineIp": "172.16.0.13",
            "MachineName": "activity-cvm-2023-10-08",
            "ProjectId": 0,
            "OsInfo": "CentOS 7.9 64位",
            "Cpu": "Intel(R) Xeon(R) Platinum 8361HC CPU @ 2.60GHz",
            "MemSize": 8,
            "MemLoad": "23.87",
            "DiskSize": 148,
            "DiskLoad": "38.67",
            "PartitionCount": 1,
            "MachineWanIp": "139.199.156.164",
            "CpuSize": 4,
            "CpuLoad": "低",
            "CpuLoadVul": "低",
            "ProtectLevel": 2,
            "RiskStatus": "未知",
            "ProtectDays": 393,
            "BuyTime": "2024-01-23 22:29:15",
            "EndTime": "2025-02-23 22:27:32",
            "CoreVersion": "3.10.0-1160.99.1.el7.x86_64",
            "OsType": "linux",
            "AgentVersion": "5.2.1.72",
            "InstallTime": "2023-10-08 11:25:11",
            "BootTime": "2024-01-23 09:23:04",
            "LastLiveTime": "2024-09-19 21:23:13",
            "Producer": "Tencent Cloud",
            "SerialNumber": "24ab84ea-99d9-4ec0-b8fc-f68553191066",
            "DeviceVersion": "CVM",
            "Status": 0,
            "NetCards": [
                {
                    "Name": "eth0",
                    "Mac": "52:54:00:b2:54:c0",
                    "Ip": "172.16.0.13",
                    "Ipv6": "2001:db8:85a3::8a2e:370:**",
                    "GateWay": "172.16.0.1",
                    "DnsServer": "183.60.82.98,183.60.83.19"
                }
            ],
            "Disks": [
                {
                    "Name": "/dev/vda1",
                    "Size": 100,
                    "Percent": 60,
                    "Type": "ext4",
                    "Path": "/data",
                    "Used": 19
                }
            ],
            "OfflineTime": "2020-10-01 00:00:00",
            "InstanceId": "ins-dusahs86",
            "UpdateTime": "2024-11-03 04:07:17",
            "FirstTime": "2024-01-25 13:12:10",
            "MachineExtraInfo": {
                "WanIP": "139.199.156.164",
                "PrivateIP": "172.16.0.13",
                "NetworkType": 1,
                "NetworkName": "vpc-8fs960h1",
                "InstanceID": "ins-dusahs86",
                "HostName": "activity-cvm-2023-10-08"
            }
        },
        "RequestId": "454e1f90-6e84-4492-a0ce-460c7515502d"
    }
}
```

