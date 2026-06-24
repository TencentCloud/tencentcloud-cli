**Example 1: 1**



Input: 

```
tccli csip DescribeCWPMachineDetail --cli-unfold-argument  \
    --InstanceId ins-4ty8h8gy \
    --MemberId mem-a01
```

Output: 
```
{
    "Response": {
        "MachineDetail": {
            "AgentStatus": "ONLINE",
            "AgentVersion": "5.3.4.16",
            "AppId": 260199982,
            "AssetTypeName": "CVM",
            "BootTime": 1780303890,
            "BuyTime": 1779676766,
            "CloudFromEnum": "Tencent",
            "CloudTags": [
                {
                    "TagKey": "test_label",
                    "TagValue": "value2"
                }
            ],
            "CoreVersion": "3.10.0-1160.119.1.el7.x86_64",
            "Cpu": "AMD EPYC 9K65 192-Core Processor",
            "CpuLoad": "低",
            "CpuSize": 2,
            "DeviceVersion": "CVM",
            "Disks": [
                {
                    "Name": "/dev/vda1",
                    "Path": "/",
                    "Percent": 15.25454,
                    "Size": 50267,
                    "Type": "ext4",
                    "Used": 7668
                }
            ],
            "EndTime": 0,
            "ExposedStatus": "UNEXPOSED",
            "InstallTime": 1779245512,
            "InstanceID": "ins-4ty8h8gy",
            "InstanceStatus": "RUNNING",
            "KernelVersion": "3.10.0-1160.119.1.el7.x86_64",
            "LatestLiveTime": 1780506639,
            "LatestOfflineTime": 1780490597,
            "MachineIp": "172.16.16.4",
            "MachineName": "change_centos_tat_no_agent",
            "MachineOs": "CentOS 7.8 64位",
            "MachineStatus": "RUNNING",
            "MachineWanIp": "",
            "MemSize": 1966,
            "MemoryLoad": "30.87",
            "NetCards": [
                {
                    "DnsServer": "183.60.83.19,183.60.82.98",
                    "Gateway": "172.16.16.1",
                    "Ip": "172.16.16.4",
                    "Ipv6": "",
                    "Mac": "52:54:00:e1:d7:ac",
                    "Name": "eth0"
                }
            ],
            "OsByAgent": "CentOS Linux release 7.8.2003 (Core)",
            "PayMode": "PREPAID",
            "ProjectId": 0,
            "ProtectDays": 19,
            "ProtectType": "ULTIMATE",
            "Quuid": "62740df1-aaaf-4787-a0aa-d3ddd72c635a",
            "RegionInfo": {
                "Region": "ap-guangzhou",
                "RegionCode": "gz",
                "RegionId": 1,
                "RegionName": "华南地区（广州）",
                "RegionNameEn": "South China (Guangzhou)"
            },
            "Remark": "测试一下备注",
            "SerialNumber": "62740df1-aaaf-4787-a0aa-d3ddd72c635a",
            "TagItems": [
                {
                    "Color": "blue",
                    "Description": "测试自动打标策略打标签",
                    "ID": 132,
                    "TagKey": "委派管理员标签key1",
                    "TagValue": "value2"
                }
            ],
            "TagModifyInfo": {
                "AppID": 260199982,
                "AssetType": "cvm_instance",
                "InstanceID": "ins-4ty8h8gy",
                "Provider": "tencent"
            },
            "Uuid": "62740df1-aaaf-4787-a0aa-d3ddd72c635a",
            "VpcCidrBlock": "172.16.0.0/16",
            "VpcId": "vpc-8amv7xvn",
            "VpcName": "Default-VPC"
        },
        "RequestId": "d9dd67d5-eccd-4f60-8d31-d7820ff3a07c"
    }
}
```

