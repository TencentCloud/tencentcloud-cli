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
                "MachineName": "stone",
                "MachineOs": "Windows",
                "MachineStatus": "ONLINE",
                "Uuid": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
                "Quuid": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
                "VulNum": 0,
                "MachineIp": "172.16.20.1",
                "IsProVersion": true,
                "MachineWanIp": "1.2.2.3",
                "PayMode": "PREPAY",
                "MalwareNum": 0,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "tag1",
                        "TagId": 1
                    }
                ],
                "BaselineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "SAFE",
                "InvasionNum": 0,
                "RegionInfo": {
                    "RegionCode": "gz",
                    "Region": "ap-guangzhuo",
                    "RegionId": 1,
                    "RegionName": "广州",
                    "RegionNameEn": "chine guangzhou"
                },
                "InstanceState": "TERMINATED_PRO_VERSION",
                "LicenseStatus": 1,
                "ProjectId": 0,
                "HasAssetScan": 1,
                "MachineType": "CVM",
                "KernelVersion": "6.4",
                "ProtectType": "BASIC_VERSION",
                "CloudTags": [
                    {
                        "TagKey": "tag1",
                        "TagValue": "tag2"
                    }
                ],
                "IsAddedOnTheFifteen": 1,
                "IpList": "1.2.3.4",
                "VpcId": "vpc-intc",
                "MachineExtraInfo": {
                    "WanIP": "49.233.15.7",
                    "PrivateIP": "172.18.16.41",
                    "NetworkType": 0,
                    "NetworkName": "vpc-9m7rhl6w",
                    "InstanceID": "ins-7m0suost",
                    "HostName": "txy-app-pre-node1"
                },
                "InstanceId": "vpc-intc",
                "Remark": "remark"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fbd6ea2c-1894-47b0-bf3e-095c78138f76"
    }
}
```

