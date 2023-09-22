**Example 1: 获取区域主机列表**

本接口 (DescribeMachines) 用于获取区域主机列表。

Input: 

```
tccli cwp DescribeMachines --cli-unfold-argument  \
    --Limit 10 \
    --MachineRegion ap-shanghai \
    --MachineType CVM \
    --Filters.0.Values 10.0.1.1 \
    --Filters.0.Name Keywords \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Machines": [
            {
                "MachineName": "test",
                "MachineOs": "CentOS 7.6 64位",
                "Uuid": "3377add2-ee61-4c9a-99a3-81d259dfc11a",
                "Quuid": "3377add2-ee61-4c9a-99a3-81d259dfc11a",
                "MachineIp": "1.1.1.1",
                "MachineWanIp": "1.1.1.1",
                "InstanceState": "NORMAL",
                "InstanceId": "ins-111",
                "ProjectId": 0,
                "VpcId": "",
                "IsProVersion": false,
                "MachineStatus": "ONLINE",
                "PayMode": "",
                "Tag": [],
                "CloudTags": null,
                "MalwareNum": 0,
                "VulNum": 0,
                "BaselineNum": 0,
                "CyberAttackNum": 0,
                "InvasionNum": 3,
                "SecurityStatus": "RISK",
                "RegionInfo": {
                    "Region": "ap-nanjing",
                    "RegionName": "华东地区（南京）",
                    "RegionId": 33,
                    "RegionCode": "nj",
                    "RegionNameEn": "East China (Nanjing)"
                },
                "MachineType": "CVM",
                "LicenseStatus": 0,
                "HasAssetScan": 0,
                "KernelVersion": "3.10.0-1160.88.1.el7.x86_64",
                "ProtectType": "BASIC_VERSION",
                "IsAddedOnTheFifteen": 1,
                "IpList": "1.1.1.1",
                "Remark": "",
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "1.1.1.1",
                    "NetworkType": 1,
                    "NetworkName": "vpc-111",
                    "InstanceID": "ins-111",
                    "HostName": ""
                }
            }
        ],
        "RequestId": "621b6063-12b2-43fa-809e-5481c8374c0a",
        "TotalCount": 1
    }
}
```

